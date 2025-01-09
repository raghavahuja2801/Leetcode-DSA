def strassen_matrix_multiplication(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11, A12, A21, A22 = [[A[i][j] for j in range(mid)] for i in range(mid)], \
                          [[A[i][j] for j in range(mid, n)] for i in range(mid)], \
                          [[A[i][j] for j in range(mid)] for i in range(mid, n)], \
                          [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11, B12, B21, B22 = [[B[i][j] for j in range(mid)] for i in range(mid)], \
                          [[B[i][j] for j in range(mid, n)] for i in range(mid)], \
                          [[B[i][j] for j in range(mid)] for i in range(mid, n)], \
                          [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    M1 = strassen_matrix_multiplication(A11, subtract_matrices(B12, B22))
    M2 = strassen_matrix_multiplication(add_matrices(A11, A12), B22)
    M3 = strassen_matrix_multiplication(add_matrices(A21, A22), B11)
    M4 = strassen_matrix_multiplication(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiplication(add_matrices(A11, A22), add_matrices(B11, B22))
    M6 = strassen_matrix_multiplication(subtract_matrices(A12, A22), add_matrices(B21, B22))
    M7 = strassen_matrix_multiplication(subtract_matrices(A11, A21), add_matrices(B11, B12))

    C11 = add_matrices(subtract_matrices(add_matrices(M5, M4), M2), M6)
    C12 = add_matrices(M1, M2)
    C21 = add_matrices(M3, M4)
    C22 = add_matrices(subtract_matrices(M5, M3), add_matrices(M1, M7))

    return combine_matrices(C11, C12, C21, C22)

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def combine_matrices(C11, C12, C21, C22):
    # Combine the 4 sub-matrices into one
    pass

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(strassen_matrix_multiplication(A, B))  # Output: Matrix product
