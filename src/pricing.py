from dataclasses import dataclass
from typing import Iterable, Mapping, Optional


@dataclass(frozen=True)
class OrderItem:
    sku: str
    unit_price: float
    quantity: int


@dataclass(frozen=True)
class Coupon:
    code: str
    discount_percent: float
    max_discount_amount: Optional[float] = None
    min_subtotal: float = 0.0


@dataclass(frozen=True)
class OrderSummary:
    subtotal: float
    discount: float
    tax: float
    total: float


def calculate_subtotal(items: Iterable[OrderItem]) -> float:
    subtotal = 0.0
    for item in items:
        if item.quantity <= 0:
            raise ValueError(f"Invalid quantity for {item.sku}: {item.quantity}")
        if item.unit_price < 0:
            raise ValueError(f"Negative unit price for {item.sku}: {item.unit_price}")
        subtotal += item.unit_price * item.quantity
    return round(subtotal, 2)


def resolve_coupon(
    coupon_code: Optional[str], catalog: Mapping[str, Coupon]
) -> Optional[Coupon]:
    if not coupon_code:
        return None
    normalized_code = coupon_code.strip().upper()
    return catalog.get(normalized_code)


def calculate_discount(subtotal: float, coupon: Optional[Coupon]) -> float:
    if coupon is None:
        return 0.0
    if subtotal < coupon.min_subtotal:
        return 0.0
    if coupon.discount_percent < 0 or coupon.discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    raw_discount = subtotal * (coupon.discount_percent / 100.0)
    if coupon.max_discount_amount is not None:
        raw_discount = min(raw_discount, coupon.max_discount_amount)
    return round(raw_discount, 2)


def calculate_order_summary(
    items: Iterable[OrderItem],
    catalog: Mapping[str, Coupon],
    coupon_code: Optional[str] = None,
    tax_rate: float = 0.16,
) -> OrderSummary:
    if tax_rate < 0:
        raise ValueError("tax_rate cannot be negative")

    subtotal = calculate_subtotal(items)
    coupon = resolve_coupon(coupon_code, catalog)
    discount = calculate_discount(subtotal, coupon)
    taxable_amount = max(0.0, subtotal - discount)
    tax = round(taxable_amount * tax_rate, 2)
    total = round(taxable_amount + tax, 2)

    return OrderSummary(
        subtotal=subtotal,
        discount=discount,
        tax=tax,
        total=total,
    )
