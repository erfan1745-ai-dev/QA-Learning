import pytest
from delivery_calculator import calculate_order_total


@pytest.mark.parametrize(
    "cart_amount, expected_total",
    [
        pytest.param(499999, 529999, id="below-threshold"),
        pytest.param(500000, 500000, id="at-threshold"),
        pytest.param(500001, 500001, id="above-threshold"),
    ],
)
def test_calculate_order_total(cart_amount, expected_total):
    result = calculate_order_total(cart_amount)

    assert result == expected_total

def test_calculate_order_total_rejects_negative_amount():
    with pytest.raises(ValueError):
        calculate_order_total(-1000)