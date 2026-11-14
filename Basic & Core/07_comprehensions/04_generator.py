# Generators are used for saving the memory
# Generator comprehension -->> (expression for item in iterable if condition)
# What is the difference between list and generator comprehension 
# LIST [x for x in items]   ----  GENERATOR (x for x in items)
# [x for x in items] --> It makes entire list into the memory, It generate immediatly and store everything in memory
# (x for x in items) --> It gives you one item at a time like a stream. 
# Generator objects needs to be consume, it will not give you all at once.


# find out sales above 5.5
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
total_cups = (sale for sale in daily_sales if sale > 5)
print(total_cups) # generator object -->> <generator object <genexpr> at 0x000001C2BBAF9490>

# It is very memory efficiant operation, because it will not read all memory at once, it will read one by one
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)

