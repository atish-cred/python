import asyncio

# async await --> SetTimeOut 2 seconds
async def brew_chai():
    print(f"Brewing chai...")
    await asyncio.sleep(2)
    print(f"Chai is ready")

# Run / Call methods
asyncio.run(brew_chai())
