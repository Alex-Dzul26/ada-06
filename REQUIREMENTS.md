# Requirements Specification (REQUIREMENTS.md)

## Functional Requirements

- **REQ-01 (Subtotal Calculation):** El sistema debe calcular el subtotal sumando `unit_price * quantity` para cada línea de artículo válida (`quantity > 0` y `unit_price >= 0`).
- **REQ-02 (Percentage Coupon Application):** El sistema debe permitir aplicar un cupón porcentual (`0 <= discount_percent <= 100`) sobre el subtotal.
- **REQ-03 (Maximum Coupon Cap):** Cuando un cupón define un límite máximo de descuento (`max_discount_amount`), el descuento efectivo no debe exceder dicho tope.
- **REQ-04 (Case-Insensitive Coupon Code Validation):** Los códigos de cupón deben normalizarse (sin espacios laterales y en mayúsculas) antes de validarse contra el catálogo de cupones activos.
- **REQ-05 (Tax Calculation Post-Discount):** El impuesto (`tax_rate`) debe calcularse sobre el monto resultante después de aplicar el descuento, redondeado a 2 decimales.
- **REQ-06 (Non-Negative Final Total):** Ningún cálculo de orden puede producir un total negativo (`total >= 0.0`).
