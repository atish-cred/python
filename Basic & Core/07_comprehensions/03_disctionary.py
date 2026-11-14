# Dictionary comprehension -->> {expression for item in iterable if condition} 
# Main difference between set and disctionary, is how you store the value.

tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

# It will store as key value pair -->> tea:Price and price / 80,  like object how we stored
tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items() }
print(tea_prices_usd)


# print(tea_prices_inr.items())
# for tea, price in tea_prices_inr.items():
#     print(tea, price)
