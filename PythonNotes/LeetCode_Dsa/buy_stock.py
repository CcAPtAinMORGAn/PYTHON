

prices = [7,2,1,5,3,4,6]

n = len(prices)

buy_price = prices[0]

profit = 0

buy_position = 0



for i in range(n):
  if(buy_price > prices[i]):
    
    buy_price = prices[i]
    
    buy_position = i
            
  profit = max(profit, prices[i] - buy_price)
  
print("Buy at position",buy_position)

print(profit)

# buy price = 7
# profit = 0
# profit = max(0 , 7 - 7)
# profit = 0


# buy price = 2
# profit = 0
# profit = max(0 , 2 - 2)
# profit = 0

# buy price = 1
# profit = 0
# profit = max(0 , 1 - 1)
# profit = 0

# buy price = 1
# profit = 0
# profit = max(0 , 5 - 1)
# profit = 4

# buy price = 1
# profit = 4
# profit = max(4 , 3 - 1)
# profit = 4

# buy price = 1
# profit = 4
# profit = max(4 , 4 - 1)
# profit = 4

# buy price = 1
# profit = 4
# profit = max(4 , 6 - 1)
# profit = 5


# prices = [7,2,1,5,3,4,6]















