"""
Example: Function Plotting

Demonstrates how to plot mathematical functions over intervals.
"""

from lmek import FunctionPlotter
import numpy as np
import math


def main():
    plotter = FunctionPlotter()
    
    print("=" * 60)
    print("LMEK Calculator - Function Plotting Examples")
    print("=" * 60)
    
    # Example 1: Simple polynomial
    print("\nExample 1: Plotting y = x² in interval [-5, 5]")
    plotter.plot_function(
        lambda x: x**2,
        (-5, 5),
        label="y = x²",
        title="Quadratic Function",
        show=False,
        save_path="/tmp/quadratic.png"
    )
    print("Saved to /tmp/quadratic.png")
    
    # Example 2: Trigonometric functions
    print("\nExample 2: Plotting multiple trigonometric functions")
    functions = [
        (lambda x: np.sin(x), "sin(x)"),
        (lambda x: np.cos(x), "cos(x)"),
        (lambda x: np.tan(x) if abs(np.tan(x)) < 10 else np.nan, "tan(x)")
    ]
    plotter.plot_multiple_functions(
        functions,
        (-2*np.pi, 2*np.pi),
        title="Trigonometric Functions",
        show=False,
        save_path="/tmp/trig_functions.png"
    )
    print("Saved to /tmp/trig_functions.png")
    
    # Example 3: Using symbolic expressions
    print("\nExample 3: Plotting symbolic expression 'exp(-x**2/2)'")
    plotter.plot_symbolic(
        "exp(-x**2/2)",
        (-3, 3),
        title="Gaussian Function",
        show=False,
        save_path="/tmp/gaussian.png"
    )
    print("Saved to /tmp/gaussian.png")
    
    # Example 4: Parametric curve (circle)
    print("\nExample 4: Plotting parametric circle")
    plotter.plot_parametric(
        lambda t: np.cos(t),
        lambda t: np.sin(t),
        (0, 2*np.pi),
        label="Unit Circle",
        title="Parametric Plot: Unit Circle",
        show=False,
        save_path="/tmp/circle.png"
    )
    print("Saved to /tmp/circle.png")
    
    # Example 5: Complex function
    print("\nExample 5: Plotting complex function 'x*sin(x)'")
    plotter.plot_symbolic(
        "x*sin(x)",
        (-10, 10),
        title="Product of Linear and Sinusoidal Functions",
        show=False,
        save_path="/tmp/complex_func.png"
    )
    print("Saved to /tmp/complex_func.png")
    
    print("\n" + "=" * 60)
    print("All plots saved to /tmp/ directory")
    print("=" * 60)


if __name__ == "__main__":
    main()
