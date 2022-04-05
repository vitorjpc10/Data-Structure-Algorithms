prices = [7,1,5,3,6,4]

leftP = 0 #Buy
rightP = 1 #Sell
max_profit = 0

while rightP < len(prices):
     
     currentProfit = prices[rightP] - prices[leftP] #our current Profit
     
     if prices[leftP] < prices[rightP]:
          if currentProfit > max_profit:
               max_profit = currentProfit
     else:
          leftP = rightP
          
     rightP += 1
     
print(max_profit)

