def fib_mod(n, mod):
    if n == 0:
        return 0
    def mult(A, B):
        return [
            [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]
        ]

    def matrix_pow(mat, power):
        result = [[1, 0], [0, 1]] 
        while power > 0:
            if power % 2 == 1:
                result = mult(result, mat)
            mat = mult(mat, mat)
            power //= 2
        return result
    M = [[1, 1], [1, 0]]
    if n == 1:
        return 1 % mod
    
    result_matrix = matrix_pow(M, n - 1)
    return result_matrix[0][0]

caso = 1
while True:
    try:
        entrada = input().strip()
        if not entrada:
            continue
        n, b = map(int, entrada.split())
        if n == 0 and b == 0:
            break
        
        fib_n_plus_1 = fib_mod(n + 1, b)

        chamadas = (2 * fib_n_plus_1 - 1 + b) % b
        
        print(f"Case {caso}: {n} {b} {chamadas}")
        caso += 1
    except (EOFError, ValueError):
        break