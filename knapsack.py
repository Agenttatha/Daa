# Given N items with their corresponding weights and values, and a package of capacity C, choose either the entire item or fractional part of the item among these N unique items to fill the package such that the package has maximum value.

# a dynamic approach
# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    print(K)

    # Table in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
                print(K[i][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


val = [15, 17, 22, 28]
wt = [5, 10, 22, 34]
W = 64
n = len(val)
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
print(K)
# print(knapSack(W, wt, val, n))
