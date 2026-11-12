# Technical Specification (SPEC.md)

## Módulo `src/pricing.py`

### Estructuras de Datos
- `OrderItem(sku: str, unit_price: float, quantity: int)`
- `Coupon(code: str, discount_percent: float, max_discount_amount: float | None = None, min_subtotal: float = 0.0)`
- `OrderSummary(subtotal: float, discount: float, tax: float, total: float)`

### Reglas de Negocio y Criterios de Aceptación
1. **AC-01 (Normalización de Cupón - REQ-04):** Si el usuario ingresa `" save20 "`, debe coincidir con el cupón `"SAVE20"`.
2. **AC-02 (Tope de Descuento - REQ-03):** Si el subtotal es `$1,000.00`, el cupón es de `20%` (`$200.00` teórico) y `max_discount_amount = 50.0`, el descuento aplicado debe ser exactamente `$50.00`.
3. **AC-03 (Subtotal Mínimo):** Si `subtotal < coupon.min_subtotal`, el cupón no aplica (`discount = 0.0`) o lanza `ValueError` según modo estricto.
4. **AC-04 (Impuesto Post-Descuento - REQ-05):** `tax = round((subtotal - discount) * tax_rate, 2)`.
