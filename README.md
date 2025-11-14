# LMEK - Linear Mathematic Analysis and Electrical Circuits Calculator

A comprehensive Python calculator with graphing/plotting functionality designed for linear mathematic analysis and electrical circuits courses.

## Features

### 1. Matrix Operations
- **RREF (Reduced Row Echelon Form)** calculation
- Determinant calculation
- Matrix inverse
- Eigenvalues computation
- Linear system solver

### 2. Function Plotting
- Plot mathematical functions over specified intervals
- Multiple functions on the same graph
- Parametric curve plotting
- Symbolic expression plotting using mathematical notation
- Save plots to files

### 3. Electrical Circuits Analysis
- **Ohm's Law** calculations
- Power calculations (P = V×I, P = V²/R, P = I²×R)
- Series and parallel resistance
- Voltage and current dividers
- RC and RL time constants
- Capacitor voltage calculations
- AC circuit impedance
- RC circuit response plotting

## Installation

```bash
# Clone the repository
git clone https://github.com/N0FR4ME/LMEK.git
cd LMEK

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Quick Start

### Matrix Operations

```python
from lmek import MatrixCalculator
import numpy as np

calc = MatrixCalculator()

# Calculate RREF of a matrix
matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
rref = calc.rref(matrix)
print("RREF:", rref)

# Calculate determinant
matrix2 = [[4, 7], [2, 6]]
det = calc.determinant(matrix2)
print("Determinant:", det)

# Calculate eigenvalues
matrix3 = [[3, 1], [1, 3]]
eigenvals = calc.eigenvalues(matrix3)
print("Eigenvalues:", eigenvals)
```

### Function Plotting

```python
from lmek import FunctionPlotter
import numpy as np

plotter = FunctionPlotter()

# Plot a simple function
plotter.plot_function(lambda x: x**2, (-5, 5), label="y = x²")

# Plot using symbolic notation
plotter.plot_symbolic("sin(x) + cos(x)", (-2*np.pi, 2*np.pi))

# Plot multiple functions
functions = [
    (lambda x: np.sin(x), "sin(x)"),
    (lambda x: np.cos(x), "cos(x)")
]
plotter.plot_multiple_functions(functions, (-2*np.pi, 2*np.pi))
```

### Circuit Analysis

```python
from lmek import CircuitAnalyzer

analyzer = CircuitAnalyzer()

# Ohm's Law: Given V=12V and R=4Ω, find I
result = analyzer.ohms_law(voltage=12, resistance=4)
print(f"Current: {result['current']} A")

# Series resistance
total = analyzer.series_resistance(10, 20, 30)
print(f"Total series resistance: {total} Ω")

# Parallel resistance
total = analyzer.parallel_resistance(10, 20)
print(f"Total parallel resistance: {total} Ω")

# Voltage divider
vout = analyzer.voltage_divider(vin=12, r1=10, r2=20)
print(f"Output voltage: {vout} V")

# Plot RC circuit response
analyzer.plot_rc_response(v0=0, vf=12, tau=0.1, 
                         title="Capacitor Charging")
```

## Command Line Interface

LMEK also provides a CLI for quick calculations:

```bash
# Matrix operations
python -m lmek.cli matrix rref "[[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]]"
python -m lmek.cli matrix det "[[4,7],[2,6]]"
python -m lmek.cli matrix eigen "[[3,1],[1,3]]"

# Plotting
python -m lmek.cli plot function "x**2" -5 5
python -m lmek.cli plot function "sin(x)" -3.14 3.14 --save plot.png

# Circuit analysis
python -m lmek.cli circuit ohms --voltage 12 --resistance 4
python -m lmek.cli circuit power --voltage 12 --current 3
python -m lmek.cli circuit series 10 20 30
python -m lmek.cli circuit parallel 10 20
```

## Examples

The `examples/` directory contains comprehensive examples:

- `matrix_examples.py` - Matrix operations and RREF calculations
- `plotting_examples.py` - Various plotting scenarios
- `circuit_examples.py` - Electrical circuit analysis

Run them with:
```bash
python examples/matrix_examples.py
python examples/plotting_examples.py
python examples/circuit_examples.py
```

## Testing

Run the test suite:

```bash
python -m unittest discover tests
```

## Dependencies

- numpy >= 1.24.0
- matplotlib >= 3.7.0
- scipy >= 1.10.0
- sympy >= 1.12

## Use Cases

### Linear Algebra Course
- Solving systems of linear equations
- Matrix transformations
- Finding eigenvalues and eigenvectors
- Visualizing linear transformations

### Electrical Circuits Course
- DC circuit analysis
- AC circuit analysis with complex impedance
- Transient response of RC/RL circuits
- Power calculations

### General Mathematics
- Plotting functions to understand behavior
- Parametric curves
- Multiple function comparison

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
