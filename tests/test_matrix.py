"""
Unit tests for LMEK matrix operations.
"""

import unittest
import numpy as np
from lmek import MatrixCalculator


class TestMatrixCalculator(unittest.TestCase):
    """Test cases for MatrixCalculator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = MatrixCalculator()
    
    def test_rref_simple(self):
        """Test RREF calculation with a simple matrix."""
        matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
        result = self.calc.rref(matrix)
        
        # Check that result is in RREF form
        # First non-zero element in each row should be 1
        self.assertAlmostEqual(result[0, 0], 1.0)
        self.assertAlmostEqual(result[1, 1], 1.0)
        self.assertAlmostEqual(result[2, 2], 1.0)
    
    def test_rref_identity(self):
        """Test RREF of identity matrix."""
        matrix = np.eye(3)
        result = self.calc.rref(matrix)
        np.testing.assert_array_almost_equal(result, matrix)
    
    def test_determinant(self):
        """Test determinant calculation."""
        matrix = [[4, 7], [2, 6]]
        det = self.calc.determinant(matrix)
        self.assertAlmostEqual(det, 10.0)
    
    def test_determinant_singular(self):
        """Test determinant of singular matrix."""
        matrix = [[1, 2], [2, 4]]
        det = self.calc.determinant(matrix)
        self.assertAlmostEqual(det, 0.0, places=10)
    
    def test_inverse(self):
        """Test matrix inverse."""
        matrix = np.array([[4, 7], [2, 6]], dtype=float)
        inv = self.calc.inverse(matrix)
        
        # Check A * A^-1 = I
        product = np.dot(matrix, inv)
        np.testing.assert_array_almost_equal(product, np.eye(2))
    
    def test_eigenvalues(self):
        """Test eigenvalue calculation."""
        matrix = [[3, 1], [1, 3]]
        eigenvals = self.calc.eigenvalues(matrix)
        
        # Known eigenvalues are 4 and 2
        expected = np.array([4.0, 2.0])
        np.testing.assert_array_almost_equal(sorted(eigenvals), sorted(expected))
    
    def test_solve_system(self):
        """Test solving linear system."""
        A = [[2, 1], [1, 3]]
        b = [5, 7]
        
        x = self.calc.solve_system(A, b)
        
        # Verify solution
        A_arr = np.array(A)
        b_arr = np.array(b)
        result = np.dot(A_arr, x)
        np.testing.assert_array_almost_equal(result, b_arr)


if __name__ == '__main__':
    unittest.main()
