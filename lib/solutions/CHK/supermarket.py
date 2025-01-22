from typing import Dict


class Promotion:

    def __init__(self, offer_dict, product_name) -> None:
        self.price = None
        self.offer_details_dict = None
        self.free_item = {}

        promo_dict = offer_dict.get(product_name, None)
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
                    print(f"---> {minimum_items}, {quantity}")
                    if minimum_items and minimum_items < quantity:
                        self.free_item = {}
                    else:
                        self.free_item[offer_item["free_item"]] = (
                            quantity // offer_item["unit"]
                        )

        return total_cost, remain_quantity


class Calculator:

    def __init__(self, offer_dict: Dict) -> None:
        self.offer_dict = offer_dict
        self.free_item = {}

    def calculate_total_bill(self, product: str, unit: int) -> int:
        total_sum = 0
        product_promotion = Promotion(self.offer_dict, product)
        if product_promotion.offer_details_dict:
            total_sum = self.get_product_offer(unit, product_promotion)

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

