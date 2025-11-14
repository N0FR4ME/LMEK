"""
Function plotting module for LMEK calculator.

Provides plotting functionality for mathematical functions in specified intervals.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Optional, List
import sympy as sp


class FunctionPlotter:
    """Plotter for mathematical functions."""
    
    def __init__(self):
        """Initialize the FunctionPlotter."""
        self.figure = None
        self.ax = None
    
    def plot_function(self, 
                     func: Callable[[float], float],
                     interval: Tuple[float, float],
                     num_points: int = 1000,
                     label: Optional[str] = None,
                     title: str = "Function Plot",
                     xlabel: str = "x",
                     ylabel: str = "y",
                     grid: bool = True,
                     show: bool = True,
                     save_path: Optional[str] = None) -> None:
        """
        Plot a function over a specified interval.
        
        Args:
            func: Function to plot (takes float, returns float)
            interval: Tuple (start, end) defining the interval
            num_points: Number of points to evaluate
            label: Label for the plot legend
            title: Plot title
            xlabel: Label for x-axis
            ylabel: Label for y-axis
            grid: Whether to show grid
            show: Whether to display the plot
            save_path: Optional path to save the figure
            
        Examples:
            >>> plotter = FunctionPlotter()
            >>> plotter.plot_function(lambda x: x**2, (-5, 5), label="y = x²")
        """
        x = np.linspace(interval[0], interval[1], num_points)
        y = np.array([func(xi) for xi in x])
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=label if label else "f(x)")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if grid:
            plt.grid(True, alpha=0.3)
        if label:
            plt.legend()
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()
    
    def plot_multiple_functions(self,
                               functions: List[Tuple[Callable, str]],
                               interval: Tuple[float, float],
                               num_points: int = 1000,
                               title: str = "Multiple Functions",
                               xlabel: str = "x",
                               ylabel: str = "y",
                               grid: bool = True,
                               show: bool = True,
                               save_path: Optional[str] = None) -> None:
        """
        Plot multiple functions on the same graph.
        
        Args:
            functions: List of tuples (function, label)
            interval: Tuple (start, end) defining the interval
            num_points: Number of points to evaluate
            title: Plot title
            xlabel: Label for x-axis
            ylabel: Label for y-axis
            grid: Whether to show grid
            show: Whether to display the plot
            save_path: Optional path to save the figure
        """
        x = np.linspace(interval[0], interval[1], num_points)
        
        plt.figure(figsize=(10, 6))
        
        for func, label in functions:
            y = np.array([func(xi) for xi in x])
            plt.plot(x, y, label=label)
        
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if grid:
            plt.grid(True, alpha=0.3)
        plt.legend()
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()
    
    def plot_parametric(self,
                       x_func: Callable[[float], float],
                       y_func: Callable[[float], float],
                       t_interval: Tuple[float, float],
                       num_points: int = 1000,
                       label: Optional[str] = None,
                       title: str = "Parametric Plot",
                       xlabel: str = "x",
                       ylabel: str = "y",
                       grid: bool = True,
                       show: bool = True,
                       save_path: Optional[str] = None) -> None:
        """
        Plot a parametric curve.
        
        Args:
            x_func: Function for x-coordinate
            y_func: Function for y-coordinate
            t_interval: Parameter interval (t_start, t_end)
            num_points: Number of points to evaluate
            label: Label for the plot
            title: Plot title
            xlabel: Label for x-axis
            ylabel: Label for y-axis
            grid: Whether to show grid
            show: Whether to display the plot
            save_path: Optional path to save the figure
        """
        t = np.linspace(t_interval[0], t_interval[1], num_points)
        x = np.array([x_func(ti) for ti in t])
        y = np.array([y_func(ti) for ti in t])
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=label if label else "parametric curve")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if grid:
            plt.grid(True, alpha=0.3)
        if label:
            plt.legend()
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()
    
    @staticmethod
    def plot_symbolic(expression: str,
                     interval: Tuple[float, float],
                     variable: str = 'x',
                     num_points: int = 1000,
                     title: Optional[str] = None,
                     show: bool = True,
                     save_path: Optional[str] = None) -> None:
        """
        Plot a symbolic mathematical expression.
        
        Args:
            expression: Mathematical expression as string (e.g., "sin(x) + x**2")
            interval: Tuple (start, end) defining the interval
            variable: Variable name (default 'x')
            num_points: Number of points to evaluate
            title: Plot title
            show: Whether to display the plot
            save_path: Optional path to save the figure
        """
        x_sym = sp.Symbol(variable)
        expr = sp.sympify(expression)
        func = sp.lambdify(x_sym, expr, 'numpy')
        
        x = np.linspace(interval[0], interval[1], num_points)
        y = func(x)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f"y = {expression}")
        plt.title(title if title else f"Plot of {expression}")
        plt.xlabel(variable)
        plt.ylabel("y")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()
