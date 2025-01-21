from solutions.CHK.supermarket import Calculator

offer_dict_r2 = {
    "A": {
        "price": 50,
        "offer": [{"unit": 3, "final_price": 130}, {"unit": 5, "final_price": 200}],
    },
    "B": {"price": 30, "offer": [{"unit": 2, "final_price": 45}]},
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {"price": 40, "offer": {"unit": 2, "free_item": "B"}},
}


def checkout_chk_r2(skus: str):
    final_price_item = 0
    calculator = Calculator(offer_dict_r2)

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
                    break
                total_item = item_list.count(x)

                final_price_item += calculator.calculate_final_offer(x, total_item)

        except ValueError as exec:
            final_price_item = -1

    return final_price_item
