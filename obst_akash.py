def optimal_cost(keys, frequency):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal with frequencies
    for i in range(n):
        dp[i][i] = frequency[i]

    # Compute optimal costs
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            
            freq_sum = sum(frequency[i:j + 1])

            for r in range(i, j + 1):
                cost = freq_sum + (dp[i][r - 1] if r > i else 0) + (dp[r + 1][j] if r < j else 0)
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]




keys = [10, 12, 20]
frequency = [34, 8, 50]

print("Cost of Optimal BST is", optimal_cost(keys, frequency))
