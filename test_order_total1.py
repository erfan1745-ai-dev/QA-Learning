import pytest


def calculate_total(item_price, delivery_fee):
    if item_price < 0 or delivery_fee < 0:
        raise ValueError("Price and delivery fee cannot be negative")

    return item_price + delivery_fee


@pytest.mark.parametrize(
    "item_price, delivery_fee, expected_total",
    [
        pytest.param(250000, 30000, 280000, id="with-delivery-fee"),
        pytest.param(250000, 0, 250000, id="without-delivery-fee"),
        pytest.param(0, 0, 0, id="both-values-zero"),
    ],
)
def test_order_total(item_price, delivery_fee, expected_total):
    total = calculate_total(item_price, delivery_fee)

    assert total == expected_total


@pytest.mark.parametrize(
    "item_price, delivery_fee",
    [
        pytest.param(-1000, 30000, id="negative-item-price"),
        pytest.param(250000, -5000, id="negative-delivery-fee"),
    ],
)
def test_order_total_rejects_negative_values(item_price, delivery_fee):
    with pytest.raises(ValueError):
        calculate_total(item_price, delivery_fee)