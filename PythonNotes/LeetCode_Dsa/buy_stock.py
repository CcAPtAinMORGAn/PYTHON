

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
