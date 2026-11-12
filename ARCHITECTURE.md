# Architecture Overview (ARCHITECTURE.md)

## Componentes Principales

1. **Domain Models (`src/pricing.py`):**
   - `OrderItem`: Representa cada línea de producto dentro de una orden.
   - `Coupon`: Define las reglas del descuento porcentual y restricciones (`max_discount_amount`, `min_subtotal`).
   - `OrderSummary`: Objeto de valor inmutable con el desglose financiero final (`subtotal`, `discount`, `tax`, `total`).
2. **Pricing Service (`calculate_order_summary` en `src/pricing.py`):**
   - Punto de entrada principal para el cálculo del resumen de orden.
   - Orquesta `calculate_subtotal`, `resolve_coupon` y `calculate_discount`.
3. **Test Suite (`tests/test_pricing.py`):**
   - Pruebas unitarias basadas en `unittest` que verifican el comportamiento del motor de precios.
