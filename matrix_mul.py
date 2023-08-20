import sys


def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    parenthesis = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * \
                    dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    parenthesis[i][j] = k

    return dp, parenthesis


def print_optimal_parenthesis(parenthesis, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesis(parenthesis, i, parenthesis[i][j])
        print_optimal_parenthesis(parenthesis, parenthesis[i][j] + 1, j)
        print(")", end="")


# Example usage
dimensions = [30, 35, 15, 5, 10, 20, 25]
dp, parenthesis = matrix_chain_multiplication(dimensions)
print(dp, end=" ")
print(parenthesis)

print("Minimum number of scalar multiplications:", dp[0][len(dimensions) - 2])
print("Optimal parenthesis placement:")
print_optimal_parenthesis(parenthesis, 0, len(dimensions) - 2)
