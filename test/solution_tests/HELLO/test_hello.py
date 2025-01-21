import pytest
from solutions.HLO import hello_solution


class TestHello:

    @pytest.mark.parametrize("input", [("testing"), ("none_works")])
    def test_hello(self, input):
        assert hello_solution.hello(input) == "Hello, World!"

    def test_empty_hello(self):
        assert hello_solution.hello(None) == None



