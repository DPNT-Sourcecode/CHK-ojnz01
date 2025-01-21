from typing import Dict


class Calculator:

    def __init__(self, offer_dict: Dict) -> None:
        self.offer_dict = offer_dict
        self.free_item = {}

    def calculate_final_offer(self, product: str, unit: int) -> int:
        final_offer = 0
        price_per_unit = 0
        offer_unit = None
        offer_price = None
        offer_free_item = None
        update_item_unit = -1

        product_info = self.offer_dict.get(product)
        if product_info:
            product_offer = product_info.get("offer")
            if product_offer:
                product_offer = sorted(
                    product_offer, key=lambda x: x["unit"], reverse=True
                )
                update_item_unit = unit
                final_offer = self.get_product_offer(
                    unit, product_offer, product_info["price"]
                )

        else:
            return -1

        return final_offer

    def get_product_offer(self, unit, product_offer, price_per_unit):
        offer_unit = None
        update_item_unit = unit
        temp_total_count = 0
        final_offer = 0

        for offer_item in product_offer:

            if "final_price" in offer_item:
                total_count, remain_offer_unit = self._calculate_single_offer(
                    offer_item, unit
                )

                update_item_unit = remain_offer_unit
                temp_total_count += total_count

            elif "free_item" in offer_item:

                self.free_item[offer_item["free_item"]] = unit // offer_item["unit"]

        if update_item_unit and update_item_unit >= 1:
            final_offer += price_per_unit * update_item_unit
        elif update_item_unit and update_item_unit <= 0:
            final_offer = price_per_unit * unit

        return final_offer

    def _calculate_single_offer(self, offer, number_unit):
        offer_cal = 0

        item_offer, remainder_unit = divmod(number_unit, offer["unit"])
        final_offer = offer["final_price"] * item_offer

        return final_offer, remainder_unit

    def getfree_items(self):
        return self.free_item
