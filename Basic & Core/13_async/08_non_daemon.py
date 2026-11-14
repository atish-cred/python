import asyncio
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

# Non Daemon threads are background thread, it will not automatically shutdown when main thread is gone.
# It will keep running until you stop the thread.
t = threading.Thread(target=monitor_tea_temp)
t.start()
print("Main program done")


# How to run for profiling
## Profiling
# Profiling does it show time spent in each function. It is very good for i/o functions and compute/memory heavy task.
# What profiling does -->> the amount of methods that you have it will tell you that where my main thread, or any thread spend amount of time in each one of them
# based on that you can optimize that perticular method/function
# --> -m CProfile    -s is an option as time    then your script path
# python -m cProfile -s time 08_non_daemon.python

