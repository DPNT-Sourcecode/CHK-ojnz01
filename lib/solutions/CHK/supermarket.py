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

        for product in self.offer_dict:
            if "offer" in product:
                offer_unit = product["offer"]["unit"]
                offer_price = product["offer"]["final_price"]
            price_per_unit = product["price"]

        return final_result


