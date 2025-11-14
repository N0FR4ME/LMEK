"""
Example: Matrix Operations - RREF Calculation

Demonstrates how to calculate the Reduced Row Echelon Form (RREF) of matrices.
"""

from lmek import MatrixCalculator
import numpy as np


def main():
    calc = MatrixCalculator()
    
    print("=" * 60)
    print("LMEK Calculator - Matrix RREF Examples")
    print("=" * 60)
    
    # Example 1: System of linear equations
    print("\nExample 1: System of Linear Equations")
    print("Solve the system:")
    print("  2x + y - z = 8")
    print("  -3x - y + 2z = -11")
    print("  -2x + y + 2z = -3")
    
    matrix1 = np.array([
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
    ], dtype=float)
    
    print("\nAugmented matrix:")
    print(matrix1)
    
    rref1 = calc.rref(matrix1)
    print("\nRREF:")
    print(rref1)
    print("\nSolution: x =", rref1[0, 3], ", y =", rref1[1, 3], ", z =", rref1[2, 3])
    
    # Example 2: 4x4 matrix
    print("\n" + "=" * 60)
    print("Example 2: 4x4 Matrix")
    
    matrix2 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ], dtype=float)
    
    print("\nOriginal matrix:")
    print(matrix2)
    
    rref2 = calc.rref(matrix2)
    print("\nRREF:")
    print(rref2)
    
    # Example 3: Determinant and inverse
    print("\n" + "=" * 60)
    print("Example 3: Determinant and Inverse")
    
    matrix3 = np.array([
        [4, 7],
        [2, 6]
    ], dtype=float)
    
    print("\nMatrix:")
    print(matrix3)
    
    det = calc.determinant(matrix3)
    print(f"\nDeterminant: {det}")
    
    if det != 0:
        inv = calc.inverse(matrix3)
        print("\nInverse:")
        print(inv)
        
        # Verify: A * A^-1 = I
        print("\nVerification (A * A^-1):")
        print(np.dot(matrix3, inv))
    
    # Example 4: Eigenvalues
    print("\n" + "=" * 60)
    print("Example 4: Eigenvalues")
    
    matrix4 = np.array([
        [3, 1],
        [1, 3]
    ], dtype=float)
    
    print("\nMatrix:")
    print(matrix4)
    
    eigenvals = calc.eigenvalues(matrix4)
    print("\nEigenvalues:")
    print(eigenvals)
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
