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

        product_info = self.offer_dict.get(product)
        if product_info:
            product_offer = product_info.get("offer")
            if product_offer:
                for offer_item in product_offer:
                    offer_unit_temp = product_offer["unit"]

                    if offer_unit and (unit >= offer_unit) and unit < offer_unit_temp:
                        break
                    else:
                        offer_unit = offer_unit_temp
                        offer_price = product_offer.get("final_price", None)
                        offer_free_item = product_offer.get("free_item", None)

            price_per_unit = product_info["price"]
        else:
            return -1

        if offer_unit and offer_price:
            item_offer, remain_unit = divmod(unit, offer_unit)
            final_offer = offer_price * item_offer

            if remain_unit >= 1:
                final_offer += price_per_unit * remain_unit
        elif offer_unit and free_item:
            self.free_item[offer_free_item] = unit // offer_unit
            final_offer = price_per_unit * unit
        else:
            final_offer = price_per_unit * unit

        return final_offer

    def getfree_items(self):
        return self.free_item

