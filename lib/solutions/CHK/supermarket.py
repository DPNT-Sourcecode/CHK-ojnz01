from typing import Dict


class BundlePromotion:
    def __init__(self, bundle_list, bundle_total_cost, max_items) -> None:
        self.items_bundle = bundle_list
        self.total_cost = bundle_total_cost
        self.max_items = max_items
        self.list_items = []

    def insert_purchased_items(self, product_list):
        self.list_items.append(product_list)

    def calculate_bundle_cost(self):
        cost_count = 0
        count_item = 0
        max_cost = 0

        self.list_items = sorted(self.list_items, key=lambda x: x["price"])
        total_item_list = [
            item for sublist in self.list_items for item in sublist.get("items", [])
        ]
        price_mapping_dict = {
            sublist["items"][0]: sublist.get("price", 0)
            for sublist in self.list_items
            if sublist.get("items")
        }

        for item in total_item_list:
            cost_count += price_mapping_dict[item]
            count_item += 1
            if count_item >= self.max_items:
                if cost_count > self.total_cost:
                    max_cost += self.total_cost
                    cost_count = 0
                count_item = 0

        cost_count += max_cost
        return cost_count


class Promotion:

    def __init__(self, offer_dict, product_name) -> None:
        self.price = None
        self.offer_details_dict = None
        self.free_item = {}
        self.bundle_promo_info = {}
        self.product_name = product_name

        promo_dict = offer_dict.get(self.product_name, None)
        if promo_dict:
            self.price = promo_dict.get("price", None)
            temp_offer_dict_obj = promo_dict.get("offer", None)
            self.offer_details_dict = (
                sorted(temp_offer_dict_obj, key=lambda x: x["unit"], reverse=True)
                if temp_offer_dict_obj
                else None
            )

    def multi_buy(self, quantity: int):
        price_result = 0
        total_cost = 0
        remain_quantity = quantity

        if self.offer_details_dict:
            for offer_item in self.offer_details_dict:
                if "final_price" in offer_item:
                    item_offer, remainder_unit = divmod(
                        remain_quantity, offer_item["unit"]
                    )
                    total_cost += offer_item["final_price"] * item_offer
                    remain_quantity = remainder_unit
                elif "free_item" in offer_item:

                    minimum_items = (
                        offer_item["min_items"] if "min_items" in offer_item else None
                    )

                    if minimum_items and minimum_items > quantity:
                        self.free_item = {}
                    else:
                        item = offer_item["free_item"]
                        free_unit = offer_item["unit"]
                        group_size = free_unit + len(item)

                        if item != self.product_name:
                            paid_items = quantity // offer_item["unit"]
                            self.free_item[item] = paid_items
                        else:
                            full_group = quantity // group_size
                            remaining = min(quantity % group_size, free_unit)
                            paid_items = full_group * free_unit + remaining

                            self.free_item[item] = quantity - paid_items

                elif "multi_item" in offer_item:
                    self._setup_multi_promo_obj(quantity, offer_item)

        return total_cost, remain_quantity

    def _setup_multi_promo_obj(self, quantity, offer_item):
        promo_item_list = offer_item["multi_item"]
        if self.product_name in promo_item_list:
            self.bundle_promo_info = {
                "bundle_header": promo_item_list,
                "total_price": offer_item.get("total_price", 0),
                "total_unit": offer_item.get("unit", 0),
                "item_list": {
                    "price": self.price,
                    "items": list(self.product_name * quantity),
                },
            }

    def get_bundle_promo_info(self):
        return self.bundle_promo_info


class Calculator:

    def __init__(self, offer_dict: Dict) -> None:
        self.offer_dict = offer_dict
        self.free_item = {}
        self.bundle_promo = None

    def calculate_total_bill(self, product: str, unit: int) -> int:
        total_sum = 0
        product_promotion = Promotion(self.offer_dict, product)
        if product_promotion.offer_details_dict:
            total_sum = self.get_product_offer(unit, product_promotion)
            bundle_promo_info = product_promotion.get_bundle_promo_info()
            if not self.bundle_promo and bundle_promo_info:
                self.bundle_promo = BundlePromotion(
                    bundle_promo_info["bundle_header"],
                    bundle_promo_info["total_price"],
                    bundle_promo_info["total_unit"],
                )
                self.bundle_promo.insert_purchased_items(bundle_promo_info["item_list"])
            elif self.bundle_promo and bundle_promo_info:
                self.bundle_promo.insert_purchased_items(bundle_promo_info["item_list"])

        elif not product_promotion.offer_details_dict and product_promotion.price:
            total_sum = product_promotion.price * unit
        else:
            total_sum = -1

        return total_sum

    def get_product_offer(self, total_unit, promotion):
        final_offer, remain_unit = promotion.multi_buy(total_unit)
        self.free_item.update(promotion.free_item)

        if remain_unit and remain_unit >= 1:
            final_offer += promotion.price * remain_unit
        elif remain_unit and remain_unit <= 0:
            final_offer = promotion.price * total_unit

        return final_offer

    def calculate_total_with_offer(self, prod_total_dict):
        total = 0
        for item, values in prod_total_dict.items():
            promotion_dict = Promotion(self.offer_dict, item)
            current_values = values["cost"]
            if item in self.free_item:
                updated_unit = values["count"] - self.free_item[item]
                promoted_price = self.get_product_offer(updated_unit, promotion_dict)

                current_values = promoted_price

            total += current_values

        return total
