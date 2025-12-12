import sys
import math
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, multiply, divide, square, square_root, logarithm, sin, cos, percentage

def test_add():
    assert add(5, 6) == 11

def test_sub():
    assert sub(10, 5) == 5

def test_multiply_basic():
    assert multiply(5, 6) == 30

def test_multiply_negative():
    assert multiply(-5, 6) == -30

def test_multiply_zero():
    assert multiply(0, 100) == 0
    assert multiply(100, 0) == 0

def test_multiply_floats():
    assert multiply(2.5, 4.0) == 10.0

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5

def test_divide_floats_and_fraction():
    assert divide(10.0, 2.0) == 5.0
    assert divide(1, 2) == 0.5
    assert divide(10, 3) == pytest.approx(10/3, rel=1e-3)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_square_and_square_root():
    assert square(5) == 25
    assert square(-5) == 25
    assert square(0) == 0
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(0) == 0
    assert square_root(2) == pytest.approx(math.sqrt(2), rel=1e-6)

def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-1)

def test_logarithm_defaults_and_bases():
    assert logarithm(100) == 2
    assert logarithm(10) == 1
    assert logarithm(1) == 0
    assert logarithm(8, 2) == 3
    assert logarithm(16, 2) == 4
    assert logarithm(math.e, math.e) == pytest.approx(1, rel=1e-6)

def test_logarithm_invalid_inputs():
    with pytest.raises(ValueError, match="Logarithm input must be positive"):
        logarithm(0)
    with pytest.raises(ValueError, match="Logarithm input must be positive"):
        logarithm(-5)
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
        logarithm(5, 0)
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
        logarithm(5, -2)
    with pytest.raises(ValueError, match="Logarithm base cannot be 1"):
        logarithm(5, 1)

def test_trigonometry():
    assert sin(0) == pytest.approx(0, abs=1e-6)
    assert sin(math.pi/2) == pytest.approx(1, abs=1e-6)
    assert sin(math.pi) == pytest.approx(0, abs=1e-6)
    assert cos(0) == pytest.approx(1, abs=1e-6)
    assert cos(math.pi) == pytest.approx(-1, abs=1e-6)
    assert -1 <= sin(1000) <= 1
    assert -1 <= cos(-1000) <= 1

def test_percentage_variants():
    assert percentage(100, 50) == 50
    assert percentage(100, 150) == 150
    assert percentage(100, 0.5) == 0.5
    assert percentage(0, 50) == 0
    assert percentage(-100, 50) == -50
    assert percentage(100, -50) == -50
    assert percentage(250.5, 20) == pytest.approx(50.1, rel=1e-9)
    assert percentage(1000000, 1) == 10000
