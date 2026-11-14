import asyncio
import requests
import aiohttp # async web request

# my endpoint takes 3 seconds of delay
# https://httpbin.org/delay/3


    # Session is used to hit the url
async def fetch_url(session, url):
    # Session is defined in aiohttp, you can check the documentation
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    # It will create 3 request url in an array
    urls = ["https://httpbin.org/delay/3"] * 3

    # Need to create a session before getting a data from url
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        
        # Gathering reference of task
        #  *task --> it will work as spread operator
        # e.g. [t1, t2, t3]
        # await asyncio.gather(t1, t2, t3)
        await asyncio.gather(*tasks)


asyncio.run(main())