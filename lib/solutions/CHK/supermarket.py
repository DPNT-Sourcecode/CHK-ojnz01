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
        update_item_unit = None

        product_info = self.offer_dict.get(product)
        if product_info:
            product_offer = product_info.get("offer")
            if product_offer:
                product_offer = sorted(
                    product_offer, key=lambda x: x["unit"], reverse=True
                )
                update_item_unit = unit
                temp_total_count = 0
                for offer_item in product_offer:

                    if "final_price" in offer_item:
                        total_count, new_item_count = self._calculate_single_offer(
                            offer_free_item, update_item_unit
                        )

                        update_item_unit -= new_item_count
                        temp_total_count += total_count

                    # remainder = divmod(offer_unit_temp, unit)
                    # if (
                    #     offer_unit
                    #     and (remainder >= offer_unit)
                    #     and unit < offer_unit_temp
                    # ):
                    #     break
                    # else:
                    #     offer_unit = offer_unit_temp
                    # offer_price = offer_item.get("final_price", None)
                    elif "free_item" in offer_item:
                        offer_free_item = offer_item.get("free_item", None)

            price_per_unit = product_info["price"]
        else:
            return -1

        if update_item_unit:
            remain_unit = unit - update_item_unit
            if remain_unit >= 1:
                final_offer += price_per_unit * remain_unit

        elif offer_unit and offer_free_item:
            self.free_item[offer_free_item] = unit // offer_unit
            final_offer = price_per_unit * unit
        else:
            final_offer = price_per_unit * unit

        return final_offer

    def _calculate_single_offer(self, offer, number_unit):
        offer_cal = 0

        item_offer, remainder_unit = divmod(offer["unit"], number_unit)
        final_offer = offer["final_price"] * item_offer

        return final_offer, remainder_unit

    def getfree_items(self):
        return self.free_item

