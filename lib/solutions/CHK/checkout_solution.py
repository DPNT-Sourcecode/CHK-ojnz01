# noinspection PyUnusedLocal
# skus = unicode string
from solutions.CHK.supermarket import Calculator

supermaker_offer_dict = {
    "A": {"price": 50, "offer": {"unit": 3, "final_price": 130}},
    "B": {"price": 30, "offer": {"unit": 2, "final_price": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
}


def checkout(skus: str):

    final_price = -1
    final_price_item = 0

    if skus:
        item_list = skus.split(",").
        for x in set(item_list):
            total_item = item_list.count(x)
            calculator = Calculator(supermaker_offer_dict)
            final_price_item += calculator.calculate_final_offer(x, total_item)

    return final_price_item



