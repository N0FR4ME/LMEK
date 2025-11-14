"""
Integration tests for LMEK calculator.

Tests that all components work together correctly.
"""

import unittest
import numpy as np
from lmek import MatrixCalculator, FunctionPlotter, CircuitAnalyzer
import os


class TestIntegration(unittest.TestCase):
    """Integration tests for LMEK."""
    
    def test_full_workflow_matrix_and_plot(self):
        """Test using matrix operations and plotting together."""
        # Calculate eigenvalues
        calc = MatrixCalculator()
        matrix = [[3, 1], [1, 3]]
        eigenvals = calc.eigenvalues(matrix)
        
        # Plot the eigenvalues as a function
        plotter = FunctionPlotter()
        save_path = "/tmp/integration_test.png"
        
        if os.path.exists(save_path):
            os.remove(save_path)
        
        # Plot a function using the eigenvalues
        plotter.plot_function(
            lambda x: eigenvals[0] * x + eigenvals[1],
            (-5, 5),
            label=f"y = {eigenvals[0]}x + {eigenvals[1]}",
            show=False,
            save_path=save_path
        )
        
        self.assertTrue(os.path.exists(save_path))
        
        if os.path.exists(save_path):
            os.remove(save_path)
    
    def test_circuit_analysis_workflow(self):
        """Test a complete circuit analysis workflow."""
        analyzer = CircuitAnalyzer()
        
        # Step 1: Calculate total resistance
        r_series = analyzer.series_resistance(10, 20)
        
        # Step 2: Calculate current using Ohm's law
        result = analyzer.ohms_law(voltage=12, resistance=r_series)
        current = result['current']
        
        # Step 3: Calculate power
        power_result = analyzer.power_calculation(voltage=12, current=current)
        
        # Verify power = V * I
        self.assertAlmostEqual(power_result['power'], 12 * current)
        
        # Step 4: RC time constant
        tau = analyzer.rc_time_constant(r_series, 100e-6)
        
        # Step 5: Plot RC response
        save_path = "/tmp/integration_rc.png"
        if os.path.exists(save_path):
            os.remove(save_path)
        
        analyzer.plot_rc_response(
            0, 12, tau,
            show=False,
            save_path=save_path
        )
        
        self.assertTrue(os.path.exists(save_path))
        
        if os.path.exists(save_path):
            os.remove(save_path)
    
    def test_solve_system_and_verify(self):
        """Test solving a system and verifying with RREF."""
        calc = MatrixCalculator()
        
        # System: 2x + y = 5, x + 3y = 7
        A = [[2, 1], [1, 3]]
        b = [5, 7]
        
        # Method 1: Direct solve
        x = calc.solve_system(A, b)
        
        # Method 2: Using RREF
        augmented = np.column_stack([A, b])
        rref = calc.rref(augmented)
        
        # Solutions should match
        np.testing.assert_array_almost_equal(x, rref[:, -1])
    
    def test_all_modules_import(self):
        """Test that all modules can be imported."""
        from lmek import MatrixCalculator, FunctionPlotter, CircuitAnalyzer
        
        # Verify instances can be created
        calc = MatrixCalculator()
        plotter = FunctionPlotter()
        analyzer = CircuitAnalyzer()
        
        self.assertIsNotNone(calc)
        self.assertIsNotNone(plotter)
        self.assertIsNotNone(analyzer)


if __name__ == '__main__':
    unittest.main()
