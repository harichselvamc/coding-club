# Linear Algebra

## dot()- it can calculate the dot product of two arrays
## det()- it can calculate determinant of a matrix
## solve()- it can solve linear matrix equation
## inv()- it can calculate the multiplicative inverse of the matrix
## trace()- it calculates the sum of diagonal elements
## rank()- it returns the rank of the matrix
## eig() - it computes the eigenvalues and right eigenvectors of a square array.
import numpy as np

# Find the determinant
c = np.identity(5)
print(np.linalg.det(c))

coeffs  = np.array([[2, 6], [5, 3]])
dependentvars = np.array([6, -9])
solution = np.linalg.solve(coeffs, dependentvars)
print(solution)