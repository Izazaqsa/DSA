coins_amount = int (input("enter amount of coins : "))
coins_list = []
for i in range (coins_amount):
    coins = int (input ("enter coin type : "))
    coins_list.append(coins)

target= int (input ("enter the target amount : "))

# creating the empty 2D list
INF = float ('inf')
min_coins= [[INF] * (target+1) for _ in range (coins_amount+1) ]

for i in range (coins_amount+1):
    min_coins[i][0]= 0

numbers = 0 
for i in range (1,coins_amount+1):
    coin_value = coins_list [i-1]
    for j in range (1,target + 1):
        if coin_value > j:
            min_coins[i][j]= min_coins[i-1][j]
        else : 
            min_coins[i][j] = min ((min_coins[i-1][j], 1 + min_coins[i][j-coin_value]))

answer = min_coins[coins_amount][target]
if answer == INF:
    print (f"The answer is not found !")
else : 
    print (f"The minimum number of coins are {answer}")


print ("printing the whole table of the dynamic programming")
print (min_coins)
print ()
print ()
i = coins_amount 
j = target 
choosen_coins = []
while i > 0 and j > 0 : 
    if min_coins [i][j] == min_coins [i-1][j]:
        i -= 1
    else: 
        coin = coins_list[i-1]
        choosen_coins.append(coin)
        j -= coin
    
print ("choose coins are : ", choosen_coins)