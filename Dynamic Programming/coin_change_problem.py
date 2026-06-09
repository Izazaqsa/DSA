
coin_numbers = int (input ("enter the number of coins you want in you list : "))
coins_list = []
for i in range (coin_numbers):
    coins = int(input("Enter coins : "))
    coins_list.append(coins)


amount = int (input ("enter the amount : "))


# creating empty, the above comment code is also the way to make it

ways = [[0]* (amount+1) for _ in range(coin_numbers+1)]
for i in range (coin_numbers+1):
    ways [i][0]=1

def finding_ways (coins,target):
    for i in range (1,coins+1):
        coin = coins_list[i-1]
        for j in range (target+1):
            if coin > j : 
                ways[i][j]= ways [i-1][j]
            else :
                ways[i][j]= ways[i-1][j] + ways[i][j-coin]

finding_ways(coin_numbers,amount)

print (f"the number of way for the amount {amount} are {ways[coin_numbers][amount]}")



# ------------------------------------------------------- #
# this is creating an empty list with zero but for this there is a short way which is in line 14 
# ways = []
# for i in range (coin_numbers):
#     rows = []
#     for j in range (amount):
#         rows.append(0)
#     ways.append(rows)
# -------------------------------------------------------- #