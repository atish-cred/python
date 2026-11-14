## Thread - GIL
# If 2 threads wants to write / update the variable/anything into the memory then who will update/write first? or who should be doing this task first?
# To avoid this kind of behavior or to update the object/value in the same memory location. Python uses known as mutex.
# Mutex is nothing its a mututallt kind of exclusive lock that we have. It's a locking system. Basically once a thread reaches to up whoever gets this mutex lock, the other guy can not actually go ahead and touch this memory.
# That's why GIL does this. This is global interpreter lock.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing process...")

# Initialize the tread
tread1 = threading.Thread(target=brew_chai, name="Barista-1")
tread2 = threading.Thread(target=brew_chai, name="Barista-2")

# started threading
start = time.time()
tread1.start()
tread2.start()
tread1.join()
tread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")