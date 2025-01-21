import pytest
from solutions.SUM import sum_solution


class TestSum:

    @pytest.mark.parametrize("x, y, result_sum", [(1, 2, 3), ()])
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

