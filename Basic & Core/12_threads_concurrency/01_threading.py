import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2) # 2 seconds

def brew_chai():
     for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3) # 3 seconds


# Creating threads --> needs to give the target
# Here we have created thread, but not invoked/started them, They just sits and wating for invoke 
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)


# Starting the thread
order_thread.start()
brew_thread.start()


# Wait for both to finish
# join method --> wait until the thread terminates.
# join means --> finish your work and come back and report to me.
order_thread.join()
brew_thread.join()


print("All orders taken and chai brewed")

# How it is working?
#  