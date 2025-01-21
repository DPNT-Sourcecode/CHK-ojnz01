from typing import Dict


class Calculator:

    def __init__(self, offer_dict: Dict) -> None:
        self.offer_dict = offer_dict

    def calculate_final_offer(self, product: str, unit: int) -> int:
        final_result = 0
        offer_info = {}

        for product in self.offer_dict:
            if "offer" in product:
                offer_unit = product["offer"]["unit"]
                offer_price = product["offer"]["unit"]

        return final_result

