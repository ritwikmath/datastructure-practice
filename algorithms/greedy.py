def max_profit(prices):
    min_price = float("inf")
    max_profit = 0
    min_price_index = -1
    max_profit_index = -1
    temp_min_index = -1

    for key, price in enumerate(prices):
        # min_price = min(min_price, price)
        
        if price < min_price:
            min_price = price
            temp_min_index = key
        
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
            max_profit_index = key
            min_price_index = temp_min_index

        # max_profit = max(max_profit, price - min_price)
    
    return max_profit, min_price_index, max_profit_index


# Example usage
prices = [7, 10, 9, 3, 6, 9, 2]
print(max_profit(prices))  # Output: 8