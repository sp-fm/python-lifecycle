import pytest

import python_lifecycle
from python_lifecycle.calculator import complex


class TestCalculator:
    @staticmethod
    def test_add():
        assert complex.Calculator.add(1, 2) == 3

    @staticmethod
    def test_sub():
        assert complex.Calculator.sub(2, 1) == 1

    @staticmethod
    def test_mul():
        assert complex.Calculator.mul(1, 2) == 2

    @staticmethod
    def test_div():
        assert complex.Calculator.div(2, 1) == pytest.approx(2)

    @staticmethod
    def test_div_zero(caplog):
        if python_lifecycle.ENV != "production":
            with pytest.raises(ZeroDivisionError) as excinfo:
                complex.Calculator.div(2, 0)
            assert str(excinfo.value) == "division by zero"
            assert "production" not in caplog.text
        else:
            with pytest.warns(RuntimeWarning) as record:
                complex.Calculator.div(2, 0)
            assert record[0].message == "division by zero"
            assert "production" in caplog.text
