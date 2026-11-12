# Order Pricing & Coupon Engine (ADA-06 Target Repository)

Servicio ligero de cálculo de precios de órdenes, impuestos y aplicación de cupones de descuento para comercio electrónico, utilizado como repositorio de ingeniería de software para **ADA-06 (MCP Tool Integration with GitHub)**.

## Estructura del Proyecto

```text
.
├── README.md
├── REQUIREMENTS.md
├── SPEC.md
├── ARCHITECTURE.md
├── src/
│   ├── __init__.py
│   └── pricing.py
└── tests/
    └── test_pricing.py
```

## Ejecución de pruebas

```bash
python -m unittest discover -s tests
```
