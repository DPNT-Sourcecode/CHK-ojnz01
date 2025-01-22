import pytest
from solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize(
    "skus, result",
    [
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
        ("AABEE", 180),
        ("AAAAAAAAA", 380),
        ("EEEEBB", 160),
        ("EEEEBBB", 190),
        ("AAAAAAAA", 330),
        ("ABCDEABCDE", 280),
        ("CCADDEEBBA", 280),
        ("FF", 20),
        ("AABF", 140),
        ("AABFFF", 150),
        ("FFFF", 30),
        ("FFFFFF", 40),
        ("ABCDEFABCDEF", 300),
        ("AAAAAEEBAAABBFFF", 475),
        ("FFABCDECBAABCABBAAAEEAAFF", 695),
        ("PPSVV", 220),
        ("LLLSPPVV", 490),
        ("UUUUUUUUU", 280),
        ("WWZHHHHHH", 95),
    ],
)
def test_checkout_r2(skus, result):
    checkout_test = checkout(skus)
    assert checkout_test == result



