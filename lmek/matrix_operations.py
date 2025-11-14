"""
Matrix operations module for LMEK calculator.

Provides matrix calculations including RREF (Reduced Row Echelon Form).
"""

import numpy as np
from typing import Union, List


class MatrixCalculator:
    """Calculator for matrix operations."""
    
    def __init__(self):
        """Initialize the MatrixCalculator."""
        pass
    
    @staticmethod
    def rref(matrix: Union[np.ndarray, List[List[float]]]) -> np.ndarray:
        """
        Calculate the Reduced Row Echelon Form (RREF) of a matrix.
        
        Args:
            matrix: Input matrix as numpy array or list of lists
            
        Returns:
            Matrix in reduced row echelon form
            
        Examples:
            >>> calc = MatrixCalculator()
            >>> matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
            >>> result = calc.rref(matrix)
        """
        # Convert to numpy array if needed
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix, dtype=float)
        else:
            matrix = matrix.astype(float)
        
        # Make a copy to avoid modifying the original
        A = matrix.copy()
        rows, cols = A.shape
        
        current_row = 0
        
        for col in range(cols):
            # Find pivot
            pivot_row = None
            for row in range(current_row, rows):
                if abs(A[row, col]) > 1e-10:  # Non-zero element
                    pivot_row = row
                    break
            
            if pivot_row is None:
                # No pivot in this column, move to next
                continue
            
            # Swap rows if needed
            if pivot_row != current_row:
                A[[current_row, pivot_row]] = A[[pivot_row, current_row]]
            
            # Scale pivot row to make pivot = 1
            A[current_row] = A[current_row] / A[current_row, col]
            
            # Eliminate all other entries in this column
            for row in range(rows):
                if row != current_row and abs(A[row, col]) > 1e-10:
                    A[row] = A[row] - A[row, col] * A[current_row]
            
            current_row += 1
            if current_row >= rows:
                break
        
        # Clean up near-zero values
        A[np.abs(A) < 1e-10] = 0
        
        return A
    
    @staticmethod
    def determinant(matrix: Union[np.ndarray, List[List[float]]]) -> float:
        """
        Calculate the determinant of a square matrix.
        
        Args:
            matrix: Input square matrix
            
        Returns:
            Determinant value
        """
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix, dtype=float)
        
        return np.linalg.det(matrix)
    
    @staticmethod
    def inverse(matrix: Union[np.ndarray, List[List[float]]]) -> np.ndarray:
        """
        Calculate the inverse of a square matrix.
        
        Args:
            matrix: Input square matrix
            
        Returns:
            Inverse matrix
        """
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix, dtype=float)
        
        return np.linalg.inv(matrix)
    
    @staticmethod
    def eigenvalues(matrix: Union[np.ndarray, List[List[float]]]) -> np.ndarray:
        """
        Calculate eigenvalues of a square matrix.
        
        Args:
            matrix: Input square matrix
            
        Returns:
            Array of eigenvalues
        """
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix, dtype=float)
        
        return np.linalg.eigvals(matrix)
    
    @staticmethod
    def solve_system(A: Union[np.ndarray, List[List[float]]], 
                     b: Union[np.ndarray, List[float]]) -> np.ndarray:
        """
        Solve a linear system Ax = b.
        
        Args:
            A: Coefficient matrix
            b: Right-hand side vector
            
        Returns:
            Solution vector x
        """
        if not isinstance(A, np.ndarray):
            A = np.array(A, dtype=float)
        if not isinstance(b, np.ndarray):
            b = np.array(b, dtype=float)
        
        return np.linalg.solve(A, b)
