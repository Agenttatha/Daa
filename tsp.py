import sys

def tsp(dist, setOfCities, city, n, dp):
    if setOfCities == (1 << n) - 1:
        return dist[city][0]
    
    if dp[setOfCities][city] != -1:
        return dp[setOfCities][city]
    
    ans = sys.maxsize
    
    for choice in range(n):
        if (setOfCities & (1 << choice)) == 0:
            subprob = dist[city][choice] + tsp(dist, setOfCities | (1 << choice), choice, n, dp)
            ans = min(ans, subprob)
    
    dp[setOfCities][city] = ans
    return ans


if __name__ == '__main__':
    dist = [
        [0, 20, 42, 25],
        [20, 0, 30, 34],
        [42, 30, 0, 10],
        [25, 34, 10, 0]
    ]
    n = 4
    
    dp = [[-1] * n for _ in range(1 << n)]
    
    print(tsp(dist, 1, 0, n, dp))
