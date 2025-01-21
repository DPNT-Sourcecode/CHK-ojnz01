import pytest
from solutions.CHK.checkout_solution import checkout
from solutions.CHK.supermarket import Calculator


Discount_offer_dict = {
    "A": {"price": 50, "offer": {"unit": 3, "final_price": 130}},
    "B": {"price": 30, "offer": {"unit": 2, "final_price": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
}


@pytest.mark.parametrize(
    "skus, result",
    [
        ("A, A, A, B, C", 180),
        ("", -1),
        ("test", -1),
        ("A, A, A, B, B, B, C, D", 240),
        ("A, B, C, D", 115),
    ],
)
def test_checkout(skus, result):
    checkout_test = checkout(skus)

    assert checkout_test == result


@pytest.mark.parametrize(
    "item, total_unit, result_total", [("A", 3, 130), ("B", 3, 75), ("C", 4, 80)]
)
def test_calculator(item, total_unit, result_total):
    test_calculator_obj = Calculator(Discount_offer_dict)

    offer_result = test_calculator_obj.calculate_final_offer(item, total_unit)

    assert offer_result == result_total
