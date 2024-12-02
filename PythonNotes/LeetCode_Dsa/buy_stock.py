
prices = [7,2,1,5,3,4,6]

n = len(prices)

x = prices[0]

profit = 0

for i in range(n):
  if( prices[i] < x ):
    
    x = prices[i]
  
  
  if(profit < prices[i] - x):
    profit = prices[i] - x
  
print(profit)
  
  
print(x)


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















