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
    "F": {"price": 10, "offer": [{"unit": 2, "free_item": "F", "min_items": 3}]},
    "G": {
        "price": 20,
    },
    "H": {
        "price": 10,
        "offer": [{"unit": 5, "final_price": 45}, {"unit": 10, "final_price": 80}],
    },
    "I": {
        "price": 35,
    },
    "J": {
        "price": 60,
    },
    "K": {"price": 80, "offer": [{"unit": 2, "final_price": 150}]},
    "L": {
        "price": 90,
    },
    "M": {
        "price": 15,
    },
    "N": {"price": 40, "offer": [{"unit": 3, "free_item": "M"}]},
    "O": {
        "price": 10,
    },
    "P": {
        "price": 50,
        "offer": [{"unit": 5, "final_price": 200}],
    },
    "Q": {
        "price": 30,
        "offer": [{"unit": 3, "final_price": 80}],
    },
    "R": {
        "price": 50,
        "offer": [{"unit": 3, "free_item": "Q"}],
    },
    "S": {
        "price": 30,
        "offer": [
            {"unit": 3, "multi_item": ["S", "T", "X", "Y", "Z"], "total_price": 45}
        ],
    },
    "T": {
        "price": 20,
        "offer": [
            {"unit": 3, "multi_item": ["S", "T", "X", "Y", "Z"], "total_price": 45}
        ],
    },
    "U": {
        "price": 40,
        "offer": [{"unit": 3, "free_item": "U", "min_items": 4}],
    },
    "V": {
        "price": 50,
        "offer": [{"unit": 2, "final_price": 90}, {"unit": 3, "final_price": 130}],
    },
    "W": {
        "price": 20,
    },
    "X": {
        "price": 90,
        "offer": [
            {"unit": 3, "multi_item": ["S", "T", "X", "Y", "Z"], "total_price": 45}
        ],
    },
    "Y": {
        "price": 10,
        "offer": [
            {"unit": 3, "multi_item": ["S", "T", "X", "Y", "Z"], "total_price": 45}
        ],
    },
    "Z": {
        "price": 50,
        "offer": [
            {"unit": 3, "multi_item": ["S", "T", "X", "Y", "Z"], "total_price": 45}
        ],
    },
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

                prod_item_dict[x] = {}
                prod_item_dict[x]["count"] = total_item
                prod_item_dict[x]["cost"] = calculator.calculate_total_bill(
                    x, total_item
                )

            final_price_item = calculator.calculate_total_with_offer(prod_item_dict)

        except ValueError as exec:
            final_price_item = -1

    return final_price_item

