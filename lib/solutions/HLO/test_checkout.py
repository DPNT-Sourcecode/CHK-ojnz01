import pytest
from solutions.CHK.checkout_solution import checkout
from solutions.CHK.supermarket import Calculator


Discount_offer_dict = {
    "A": {"price": 50, "offer": {"unit": 3, "final_price": 130}},
    "B": {"price": 30, "offer": {"unit": 2, "final_price": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
}


@pytest.mark.parametrize("skus, result", [("A, A, A, B, C", 190)])
def test_checkout(skus, result):
    checkout_test = checkout(skus)

    assert checkout_test == result


def test_calculator():
    test_calculator_obj = Calculator(Discount_offer_dict)

    offer_result = test_calculator_obj.calculate_final_offer("A", 3)

    assert offer_result == 130

