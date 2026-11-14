# Yield is used for get the data, but anyone want to send the data to yeild then below methods are usefull
# 


# How it is working -->> we define the function
# then "order = yield" value is not going to fill because it is expecting to fill via yield
# "order = yield" So nothing will given then it will pause the execution and not move forward.
# when you call this "next(stall)" it starts the function and it will print first line but next yield not not fullfill so it will pause the execution
# when you send the value "stall.send("Masala chai")" -->> send will directly interact with your generator and yield value will get fullfill and execution will start -->> while loop
# "order = yield" line number 19 --> again we are pausing the program, otherwise it will go infinite loop, becuse of while loop 
def chai_customer():
    print("Welcom! What cha would you like?")
    order = yield # can store value in yield using variable
    while True:
        print(f"Preparing: {order}")

        # If you don't write this then loop will go in infinite mode.
        # Because we are using while loop.
        order = yield 


stall = chai_customer()
next(stall) # start the generator

stall.send("Masala chai")
stall.send("Ginger chai")

