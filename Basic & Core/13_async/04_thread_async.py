import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# In this example we have creating concurrency blocking operation with thread
# and it will get handled by async operation
# Non async function will block the operation, because it is not async and time.sleep is used
# 
# run in executor -->> let's asyncio runs async function but in another thread
# Final -->> We are creating a thread with blocking operation (e.g. DB call) then that function will get handled but asyncio in different thread



# non async function
def check_stock(item):
    print(f"Checking {item} in store..")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"


# async function
async def main():
    # below method used for specifically for thread.
    loop = asyncio.get_running_loop()
    
    # It will execute thread one by one using below method 
    with ThreadPoolExecutor() as pool:
        # check_stock will become target here
        # 3rd params will be arguments -->> args
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)


asyncio.run(main())
