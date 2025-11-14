"""
LMEK - Linear Mathematic Analysis and Electrical Circuits Calculator

A calculator with graphing/plotting functionality for linear mathematic analysis 
and electrical circuits.
"""

__version__ = "0.1.0"

from .matrix_operations import MatrixCalculator
from .function_plotter import FunctionPlotter
from .circuits import CircuitAnalyzer

__all__ = ["MatrixCalculator", "FunctionPlotter", "CircuitAnalyzer"]
