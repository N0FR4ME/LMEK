"""
Unit tests for LMEK function plotter.
"""

import unittest
import numpy as np
from lmek import FunctionPlotter
import os


class TestFunctionPlotter(unittest.TestCase):
    """Test cases for FunctionPlotter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.plotter = FunctionPlotter()
    
    def test_plot_function_save(self):
        """Test plotting and saving a function."""
        save_path = "/tmp/test_plot.png"
        
        # Remove file if it exists
        if os.path.exists(save_path):
            os.remove(save_path)
        
        self.plotter.plot_function(
            lambda x: x**2,
            (-5, 5),
            show=False,
            save_path=save_path
        )
        
        # Check that file was created
        self.assertTrue(os.path.exists(save_path))
        
        # Clean up
        if os.path.exists(save_path):
            os.remove(save_path)
    
    def test_plot_multiple_functions(self):
        """Test plotting multiple functions."""
        save_path = "/tmp/test_multi_plot.png"
        
        if os.path.exists(save_path):
            os.remove(save_path)
        
        functions = [
            (lambda x: x, "linear"),
            (lambda x: x**2, "quadratic")
        ]
        
        self.plotter.plot_multiple_functions(
            functions,
            (-5, 5),
            show=False,
            save_path=save_path
        )
        
        self.assertTrue(os.path.exists(save_path))
        
        if os.path.exists(save_path):
            os.remove(save_path)
    
    def test_plot_symbolic(self):
        """Test plotting symbolic expression."""
        save_path = "/tmp/test_symbolic.png"
        
        if os.path.exists(save_path):
            os.remove(save_path)
        
        self.plotter.plot_symbolic(
            "sin(x)",
            (-np.pi, np.pi),
            show=False,
            save_path=save_path
        )
        
        self.assertTrue(os.path.exists(save_path))
        
        if os.path.exists(save_path):
            os.remove(save_path)
    
    def test_plot_parametric(self):
        """Test parametric plotting."""
        save_path = "/tmp/test_parametric.png"
        
        if os.path.exists(save_path):
            os.remove(save_path)
        
        self.plotter.plot_parametric(
            lambda t: np.cos(t),
            lambda t: np.sin(t),
            (0, 2*np.pi),
            show=False,
            save_path=save_path
        )
        
        self.assertTrue(os.path.exists(save_path))
        
        if os.path.exists(save_path):
            os.remove(save_path)


if __name__ == '__main__':
    unittest.main()
