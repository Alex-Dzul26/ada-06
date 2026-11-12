import unittest
from src.pricing import Coupon, OrderItem, calculate_order_summary


class TestOrderPricing(unittest.TestCase):
    def setUp(self):
        self.catalog = {
            "SAVE10": Coupon(code="SAVE10", discount_percent=10.0),
            "SAVE20CAP50": Coupon(
                code="SAVE20CAP50",
                discount_percent=20.0,
                max_discount_amount=50.0,
                min_subtotal=100.0,
            ),
        }

    def test_order_without_coupon(self):
        items = [OrderItem(sku="BOOK-1", unit_price=200.0, quantity=2)]
        summary = calculate_order_summary(items, self.catalog, tax_rate=0.16)
        self.assertEqual(summary.subtotal, 400.0)
        self.assertEqual(summary.discount, 0.0)
        self.assertEqual(summary.tax, 64.0)
        self.assertEqual(summary.total, 464.0)

    def test_order_with_percentage_coupon(self):
        items = [OrderItem(sku="LAPTOP-STAND", unit_price=500.0, quantity=1)]
        summary = calculate_order_summary(
            items, self.catalog, coupon_code="SAVE10", tax_rate=0.16
        )
        self.assertEqual(summary.subtotal, 500.0)
        self.assertEqual(summary.discount, 50.0)
        self.assertEqual(summary.tax, 72.0)
        self.assertEqual(summary.total, 522.0)


if __name__ == "__main__":
    unittest.main()
