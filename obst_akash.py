class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def optimal_cost(keys, frequency):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    root = [[None] * n for _ in range(n)]

    # Initialize the diagonal with frequencies
    for i in range(n):
        dp[i][i] = frequency[i]
        root[i][i] = TreeNode(keys[i])

    # Compute optimal costs and construct the BST
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')

            freq_sum = sum(frequency[i:j + 1])

            for r in range(i, j + 1):
                cost = freq_sum + (dp[i][r - 1] if r > i else 0) + (dp[r + 1][j] if r < j else 0)
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    root[i][j] = TreeNode(keys[r])

    # Traverse the optimal BST (in-order)
    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print(node.key, end=' ')
            in_order_traversal(node.right)

    print("Cost of Optimal BST is", dp[0][n - 1])
    print("Optimal BST:")
    in_order_traversal(root[0][n - 1])
    print()

keys = [10, 12, 20]
frequency = [34, 8, 50]

optimal_cost(keys, frequency)
