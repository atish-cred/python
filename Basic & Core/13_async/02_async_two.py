import asyncio
import time

# async await --> SetTimeOut 2 seconds
async def brew(name):
    print(f"Brewing {name} chai")
    # await asyncio.sleep(2)
    # time.sleep(3)
    print(f"{name} is ready...")

async def main():
    # Work as promise.all
    await asyncio.gather(
        brew("Masala"),
        brew("Ginger"),
        brew("Lemon"),
    )

# Run / Call methods
asyncio.run(main())
