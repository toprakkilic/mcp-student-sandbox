# Mystery Module

## Overview

`mystery_module.py` is a Python module that provides functionality to solve quadratic equations of the form `ax² + bx + c = 0`. It calculates the roots (solutions) using the quadratic formula.

## Features

- Solves quadratic equations
- Handles real and complex roots (returns `None` for complex roots)
- Returns both roots as a tuple

## Installation

No special installation required. Ensure you have Python 3.x installed. The module uses the built-in `math` library.

## Usage

Import the module and call the `fn_x` function with coefficients `a`, `b`, and `c`.

### Example

```python
import mystery_module

# Solve x² - 5x + 6 = 0
roots = mystery_module.fn_x(1, -5, 6)
print(roots)  # Output: (3.0, 2.0)

# Solve x² + 2x + 1 = 0 (perfect square)
roots = mystery_module.fn_x(1, 2, 1)
print(roots)  # Output: (-1.0, -1.0)

# Solve x² + x + 1 = 0 (complex roots)
roots = mystery_module.fn_x(1, 1, 1)
print(roots)  # Output: None
```

## API Reference

### `fn_x(a, b, c)`

Calculates the roots of the quadratic equation `ax² + bx + c = 0`.

**Parameters:**
- `a` (float): Coefficient of x² (must not be zero)
- `b` (float): Coefficient of x
- `c` (float): Constant term

**Returns:**
- `tuple` of two floats: The two roots (x1, x2) if real
- `None`: If discriminant is negative (complex roots)

**Raises:**
- No exceptions raised, but assumes `a != 0`

## Mathematical Background

The quadratic formula is:
```
x = [-b ± sqrt(b² - 4ac)] / 2a
```

Where the discriminant `d = b² - 4ac` determines the nature of roots:
- `d > 0`: Two distinct real roots
- `d = 0`: One real root (repeated)
- `d < 0`: Two complex roots

## Limitations

- Only handles real coefficients
- Does not return complex roots (returns `None` instead)
- Assumes `a ≠ 0` (division by zero not handled)

## Contributing

Feel free to submit issues or pull requests for improvements, such as adding complex number support or better error handling.

## License

This project is for educational purposes. No specific license applied.