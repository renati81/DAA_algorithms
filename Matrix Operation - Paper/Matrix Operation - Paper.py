import numpy as np

def lup_decomposition(A):
    """
    Perform LUP decomposition on the given matrix A.
    Returns:
        L (Lower triangular matrix)
        U (Upper triangular matrix)
        P (Permutation matrix)
    """
    n = A.shape[0]
    U = A.copy()  # Create a copy of A for U
    L = np.eye(n, dtype=float)  # Initialize L as identity matrix
    P = np.eye(n, dtype=float)  # Initialize P as identity matrix

    for k in range(n - 1):
        # Pivoting: Find the row with the largest value in column k (below or at diagonal)
        pivot_row = np.argmax(np.abs(U[k:, k])) + k
        if pivot_row != k:
            # Swap rows in U and P
            U[[k, pivot_row], :] = U[[pivot_row, k], :]
            P[[k, pivot_row], :] = P[[pivot_row, k], :]
            if k > 0:
                # Swap rows in L (only columns before k)
                L[[k, pivot_row], :k] = L[[pivot_row, k], :k]

        # Gaussian elimination: Update L and U
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]

    return L, U, P

# Example usage
if __name__ == "__main__":
    A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    L, U, P = lup_decomposition(A)

    print("L (Lower Triangular Matrix):")
    print(L)
    print("\nU (Upper Triangular Matrix):")
    print(U)
    print("\nP (Permutation Matrix):")
    print(P)
