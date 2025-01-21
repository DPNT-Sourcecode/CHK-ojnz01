import pytest
from solutions.SUM import sum_solution


class TestSum:

    @pytest.mark.parametrize("x, y, result_sum", [(1, 2, 3), (3, 5, 8), (4, 10, 14)])
    def test_sum(self, x, y, result_sum):
        assert sum_solution.compute(x, y) == result_sum


