size = int (input("enter the size : "))
items_weight = []

for i in range (size ):
    item = int (input("enter the weight : "))
    items_weight.append(item)

items_values = []
for i in range (size ):
    value = int (input("enter the value : "))
    items_values.append(value)

weight = int (input("enter the weight of the knapsack : "))

dp = [[0]* (weight+1) for _ in range (size+1)]
def knapsack (wt , val , W):
    n = len(wt)
    
    for i in range (1,n+1):
        for j in range (1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else : 
                dp[i][j] = dp[i-1][j]

    return dp[n][W]

def backtracking ( dp , wt, val , W):
    n = len(wt)
    i = n 
    j = W 
    selected_items = []
    while i > 0 and j > 0 : 
        if dp [i][j] == dp [i-1][j]: 
            i -= 1 
        else : 
            selected_items.append(i-1)
            j -= wt[i-1]
            i -= 1 
    return selected_items


answer =knapsack(items_weight,items_values, weight)
sel_items = backtracking (dp,items_weight,items_values, weight)
print (f"the maximum profit will be : {answer}")
print (f"the selected items are : {sel_items}")

# memorization approach 
memo = [[-1] * (weight+1) for _ in range (size+1)]
def bag (i,w):
    if i == 0 or w ==  0: 
        return 0 
    if memo[i][w] != -1 : 
        return memo[i][w]
    if items_weight[i-1] <=  w : 
        memo [i][w] = max (items_values[i-1] + bag (i-1 , w - items_weight[i-1]), bag (i-1,w))
    else : 
        memo [i][w]= bag (i-1 , w)
    return memo [i][w]