import aiohttp
import threading
import requests
import time
import asyncio


def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time()
    elapsed = et-st
    print(elapsed)
    return json_array


class ThreadingDownLoader(threading.Thread):
    json_array = []
    def __init__(self,url):
        super().__init__()
        self.url = url
    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array
def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownLoader(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
        #print(t)
    et = time.time()
    elapsed = et - st
    print("Execution time :",elapsed)

async def get_data_async_but_as_wrapper(urls):
    st = time.time()
    json_array = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())
    et = time.time()
    elapsed = et-st
    print("Execution time :",elapsed)
    return json_array

async def get_data(session,url,json_array):
    async with session.get(url) as response:
        json_array.append(await response.json())

async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session,url,json_array)))
        await asyncio.gather(*tasks)

    et = time.time()
    elapsed = et - st
    print("Execution time :", elapsed)
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
#print(get_data_sync(urls) 34 sec
#get_data_threading(urls)  4 sec
#asyncio.run(get_data_async_but_as_wrapper(urls))  32 sec
#asyncio.run(get_data_async_concurrently(urls)) 3.5 sec

