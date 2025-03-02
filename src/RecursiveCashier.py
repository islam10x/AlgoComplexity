def minCoins(N,coins):
    if N in coins:
        return 1
    else:
        result= max((num for num in coins if num < N), default=None)
        return 1 + minCoins(N-result,coins)
def minCoinsOptimized(N,coins,memo={}):
    if N in memo:
        return memo[N]
    if N in coins:
        return 1
    else:
        memo[N] = max((num for num in coins if num < N), default=None)
        return 1 + minCoinsOptimized(N-memo[N],coins,memo)

print(minCoinsOptimized(47, {1,5,10,25}))

# O(N*len(coins)) complexity
