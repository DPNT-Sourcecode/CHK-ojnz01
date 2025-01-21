# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import islower
from solutions.CHK.supermarket import Calculator

supermaker_offer_dict = {
    "A": {"price": 50, "offer": {"unit": 3, "final_price": 130}},
    "B": {"price": 30, "offer": {"unit": 2, "final_price": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
}


def checkout(skus: str):

    final_price_item = 0
    calculator = Calculator(supermaker_offer_dict)

    if skus:
        try:
            item_list = skus.replace(",", "").strip()
            for x in set(item_list):
                if x.islower():
                    final_price_item = -1
                    break
                total_item = item_list.count(x)

                final_price_item += calculator.calculate_final_offer(x, total_item)

        except ValueError as exec:
            print("error")
            final_price_item = -1

    return final_price_item

