
import pytest


@pytest.mark.parametrize("skus, offer, result", [
    ("A, A, A, B, C", 
    { "A": { "price": 50, "offer": {"unit": 3, "final_price": 130}}, 
      "B": { "price": 30, "offer": {"unit": 2, "final_price": 45}},
      "C": { "price": 20}, 
      "D": { "price": 15}
    }, 
    190
    )
])
def test_checkout(skus, offer, result):
    