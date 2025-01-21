from typing import Dict


class Calculator:

    def __init__(self, offer_dict: Dict) -> None:
        self.offer_dict = offer_dict

    def calculate_final_offer(self, product: str, unit: int) -> int:
        final_result = 0
        offer_info = {}
        offer_unit = None
        offer_price = None
        price_per_unit = 0
        product_info = self.offer_dict.get(product)

        if product_info:

            if "offer" in product_info:
                offer_unit = product_info["offer"]["unit"]
                offer_price = product_info["offer"]["final_price"]
            price_per_unit = product_info["price"]

        if offer_unit and offer_price:
            item_offer = unit // offer_unit

        return final_result





