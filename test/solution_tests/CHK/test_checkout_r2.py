import pytest


OFFER_DISCOUNT_CHK_R1 = {
    "A": {"price": 50, "offer": {"unit": 3, "final_price": 130}},
    "B": {"price": 30, "offer": {"unit": 2, "final_price": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {"price": 40, "offer": {"unit": }}
}


@pytest.mark.parametrize("skus, result", [
    ("A, A, A, B, C", 180),
    ("", 0),
    ("test", -1),
    ("A, A, A, B, B, B, C, D", 240),
    ("A, B, C, D", 115),
    ("-", -1),
    ("BABDDCAC", 215),
    ("B", 30),
    ("AA", 100),
    ("AxA", -1),
    ({"test"}, -1),
]) 