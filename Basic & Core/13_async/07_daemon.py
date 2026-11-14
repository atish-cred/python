import asyncio
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

# Daemon threads are background thread, it automatically shutdown when main thread is gone.
t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()
print("Main program done")

