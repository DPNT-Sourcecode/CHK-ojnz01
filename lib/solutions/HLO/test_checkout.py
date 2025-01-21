
import pytest


@pytest.mark.parametrize("skus, offer, result", [
    ("A, A, A, B, C"), { "A": {"unit"}}
])