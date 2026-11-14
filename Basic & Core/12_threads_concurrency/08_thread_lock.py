# Using of lock to handle the shared state. Lock the perticular memory location
# You can call it this thread safe

import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(1000000):
        # counter += 1 # Without lock 
        with lock: # lock the perticular memory location
            counter += 1

# used comprehension to define the thread
threads = [threading.Thread(target=increament) for _ in range(10)]

# used comprehension to start the thread and join the thread 
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")

