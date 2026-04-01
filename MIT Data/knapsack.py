

dirt = (4, 0)
computer = (10, 30)
fork = (5, 1)
problem_set = (0, -10)

def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def metric1(item):
    return item[1]/item[0] if item[0] != 0 else float('inf') 

for item in [dirt, computer, fork, problem_set]:
    print(metric1(item))

def metric2(item):
    return  -item[0]

for item in [dirt, computer, fork, problem_set]:
    print(metric2(item))

def metric3(item):
    return item[1]

for item in [dirt, computer, fork, problem_set]:
    print(metric3(item))