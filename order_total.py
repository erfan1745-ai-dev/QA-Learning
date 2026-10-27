#import pytest

#def calculate_total(item_price, delivery_fee):
#    if item_price < 0 or delivery_fee < 0:
#        raise ValueError("Price and delivery fee cannot be negative")
#
#   return item_price + delivery_fee


#def test_order_total_with_delivery_fee():
#    total = calculate_total(250000, 30000)

#    assert total == 280000

#def test_order_total_without_delivery_fee():
 #   total = calculate_total(250000, 0)

  #  assert total == 250000

#def test_order_total_when_both_values_are_zero():
 #   total = calculate_total(0, 0)

  #  assert total == 0

#def test_order_total_rejects_negative_price():
 #   with pytest.raises(ValueError):
  #      calculate_total(-1000, 30000)

#def test_order_total_rejects_negative_delivery_fee():
 #   with pytest.raises(ValueError):
  #      calculate_total(250000, -5000)