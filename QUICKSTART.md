# LMEK Quick Reference Guide

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## Matrix Operations

### RREF (Reduced Row Echelon Form)
```python
from lmek import MatrixCalculator
calc = MatrixCalculator()
matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
rref = calc.rref(matrix)
```

**CLI:**
```bash
python -m lmek.cli matrix rref "[[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]]"
```

### Other Matrix Operations
```python
# Determinant
det = calc.determinant([[4, 7], [2, 6]])

# Inverse
inv = calc.inverse([[4, 7], [2, 6]])

# Eigenvalues
eigenvals = calc.eigenvalues([[3, 1], [1, 3]])

# Solve Ax = b
x = calc.solve_system([[2, 1], [1, 3]], [5, 7])
```

## Function Plotting

### Simple Function Plot
```python
from lmek import FunctionPlotter
plotter = FunctionPlotter()

# Using lambda
plotter.plot_function(lambda x: x**2, (-5, 5), label="y = x²")

# Using symbolic expression
plotter.plot_symbolic("sin(x) + cos(x)", (-6.28, 6.28))
```

**CLI:**
```bash
python -m lmek.cli plot function "sin(x)" -3.14 3.14 --save plot.png
```

### Multiple Functions
```python
functions = [
    (lambda x: np.sin(x), "sin(x)"),
    (lambda x: np.cos(x), "cos(x)")
]
plotter.plot_multiple_functions(functions, (-2*np.pi, 2*np.pi))
```

### Parametric Plot
```python
plotter.plot_parametric(
    lambda t: np.cos(t),  # x(t)
    lambda t: np.sin(t),  # y(t)
    (0, 2*np.pi)
)
```

## Circuit Analysis

### Ohm's Law (V = I × R)
```python
from lmek import CircuitAnalyzer
analyzer = CircuitAnalyzer()

# Find current given voltage and resistance
result = analyzer.ohms_law(voltage=12, resistance=4)
print(f"Current: {result['current']} A")
```

**CLI:**
```bash
python -m lmek.cli circuit ohms --voltage 12 --resistance 4
```

### Power Calculations
```python
# P = V × I
result = analyzer.power_calculation(voltage=12, current=3)

# P = V² / R
result = analyzer.power_calculation(voltage=12, resistance=4)

# P = I² × R
result = analyzer.power_calculation(current=3, resistance=4)
```

### Resistance Combinations
```python
# Series: R_total = R1 + R2 + R3 + ...
total = analyzer.series_resistance(10, 20, 30)  # 60Ω

# Parallel: 1/R_total = 1/R1 + 1/R2 + 1/R3 + ...
total = analyzer.parallel_resistance(10, 20)  # 6.67Ω
```

**CLI:**
```bash
python -m lmek.cli circuit series 10 20 30
python -m lmek.cli circuit parallel 10 20
```

### Voltage Divider
```python
# Vout = Vin × R2 / (R1 + R2)
vout = analyzer.voltage_divider(vin=12, r1=10, r2=20)  # 8V
```

### Current Divider
```python
# For two parallel resistors
i1, i2 = analyzer.current_divider(itotal=6, r1=10, r2=20)
```

### RC/RL Circuits
```python
# Time constant
tau_rc = analyzer.rc_time_constant(R=1000, C=100e-6)  # 0.1s
tau_rl = analyzer.rl_time_constant(R=100, L=10)  # 0.1s

# Capacitor voltage during charging/discharging
v = analyzer.capacitor_voltage(v0=0, vf=12, t=0.1, tau=0.1)

# Plot RC response
analyzer.plot_rc_response(v0=0, vf=12, tau=0.1)
```

### AC Circuit Impedance
```python
# RC impedance: Z = R + 1/(jωC)
Z_rc = analyzer.impedance_rc(R=1000, C=1e-6, frequency=1000)
print(f"Magnitude: {abs(Z_rc)}Ω")
print(f"Phase: {np.angle(Z_rc, deg=True)}°")

# RL impedance: Z = R + jωL
Z_rl = analyzer.impedance_rl(R=100, L=0.01, frequency=1000)
```

## Common Use Cases

### Solve a System of Linear Equations
```python
# System: 2x + y - z = 8
#         -3x - y + 2z = -11
#         -2x + y + 2z = -3

from lmek import MatrixCalculator
calc = MatrixCalculator()

# Create augmented matrix [A|b]
matrix = [[2, 1, -1, 8],
          [-3, -1, 2, -11],
          [-2, 1, 2, -3]]

rref = calc.rref(matrix)
print(f"x = {rref[0, 3]}")  # x = 2
print(f"y = {rref[1, 3]}")  # y = 3
print(f"z = {rref[2, 3]}")  # z = -1
```

### Analyze a Series RC Circuit
```python
from lmek import CircuitAnalyzer
analyzer = CircuitAnalyzer()

# Circuit parameters
V = 12  # Supply voltage
R = 1000  # Resistance (1kΩ)
C = 100e-6  # Capacitance (100μF)

# Calculate time constant
tau = analyzer.rc_time_constant(R, C)
print(f"Time constant: {tau}s")

# Plot charging curve
analyzer.plot_rc_response(v0=0, vf=V, tau=tau,
                         title="Capacitor Charging")
```

### Compare Multiple Functions
```python
from lmek import FunctionPlotter
import numpy as np

plotter = FunctionPlotter()

functions = [
    (lambda x: x, "Linear"),
    (lambda x: x**2, "Quadratic"),
    (lambda x: x**3, "Cubic")
]

plotter.plot_multiple_functions(
    functions,
    (-2, 2),
    title="Polynomial Comparison"
)
```

## Running Examples

```bash
# Matrix operations
python examples/matrix_examples.py

# Function plotting
python examples/plotting_examples.py

# Circuit analysis
python examples/circuit_examples.py
```

## Running Tests

```bash
# All tests
python -m unittest discover tests

# Specific test module
python -m unittest tests.test_matrix
python -m unittest tests.test_plotting
python -m unittest tests.test_circuits
python -m unittest tests.test_integration
```
