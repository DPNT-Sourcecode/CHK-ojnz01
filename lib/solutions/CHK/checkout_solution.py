from solutions.CHK.supermarket import Calculator

offer_dict_r2 = {
    "A": {
        "price": 50,
        "offer": [{"unit": 3, "final_price": 130}, {"unit": 5, "final_price": 200}],
    },
    "B": {"price": 30, "offer": [{"unit": 2, "final_price": 45}]},
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {"price": 40, "offer": [{"unit": 2, "free_item": "B"}]},
}


def checkout(skus: str):
    final_price_item = 0
    calculator = Calculator(offer_dict_r2)
    prod_item_dict = {}
    if skus:
        try:
            if not isinstance(skus, str):
                final_price_item = -1
                raise ValueError("Invalid type")

            item_list = skus.replace(",", "")
            item_list = item_list.replace(" ", "")
            for x in set(item_list):
                if x.islower() or not x.isalpha():
                    final_price_item = -1
                    raise ValueError("Invalid Input")

                total_item = item_list.count(x)

                prod_item_dict[x] = calculator.calculate_final_offer(x, total_item)

            # Check if there's any free item
            free_item_dict = calculator.getfree_items()
            for item, values in prod_item_dict.items():
                product_dict_offer = calculator.offer_dict.get(item, None)
                if item in free_item_dict:
                    free_item_unit = free_item_dict[item]
                    promoted_price = calculator.get_product_offer(
                        free_item_unit,
                        product_dict_offer.get("offer"),
                        product_dict_offer.get("price"),
                    )

                    values -= promoted_price
                    # values -= offer_dict_r2[item]["price"] * free_item_dict[item]

                final_price_item += values

        except ValueError as exec:
            final_price_item = -1

    return final_price_item


