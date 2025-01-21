from typing import Dict


class Calculator:

    def __init__(self, offer_dict: Dict) -> None:
        self.offer_dict = offer_dict

    def calculate_final_offer(self, product: str, unit: int) -> int:
        final_offer = 0
        price_per_unit = 0
        offer_unit = None
        offer_price = None
        free_item = None

        product_info = self.offer_dict.get(product)
        if product_info:
            product_offer = product_info.get("offer")
            if product_offer:
                for offer_item in product_offer:
                    offer_unit = product_offer["unit"]

                    offer_price = product_offer.get("final_price", None)
                    free_item = product_offer.get("free_item", None)

            price_per_unit = product_info["price"]
        else:
            return -1

        if offer_unit and offer_price:
            item_offer, remain_unit = divmod(unit, offer_unit)
            final_offer = offer_price * item_offer

            if remain_unit >= 1:
                final_offer += price_per_unit * remain_unit
        elif offer_unit and free_item:
            item_offer, remain_unit = divmod(unit, offer_unit)

        else:
            final_offer = price_per_unit * unit

        return final_offer


