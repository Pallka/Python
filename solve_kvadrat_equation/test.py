from lab1 import solve_kvadrat_equation
import pytest

def test_no_solution():
    assert solve_kvadrat_equation(2, 2, 1) is None

def test_two_solutions():
    assert solve_kvadrat_equation(1, -5, 6) == (3.0, 2.0)

def test_one_solution():
    assert solve_kvadrat_equation(1, -6, 9) == (3.0, 3.0)

def test_zero_a():
    with pytest.raises(ValueError):
        solve_kvadrat_equation(0, 2, 1)
        