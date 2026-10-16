```python
def print_optimal_parens(split, i, j):
    if i == j:
        print("A" + str(i), end="")
        return

    print("(", end="")
    print_optimal_parens(split, i, split[i][j])
    print_optimal_parens(split, split[i][j] + 1, j)
    print(")", end="")


def matrix_chain_order(p, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j]
                        + p[i - 1] * p[k] * p[j])

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    print("Optimal parenthesization: ", end="")
    print_optimal_parens(split, 1, n)
    print()

    return dp[1][n]


p = [10, 30, 5, 60]
n = len(p) - 1

print("Minimum scalar multiplications:",
      matrix_chain_order(p, n))
```
