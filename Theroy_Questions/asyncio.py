"""
Python's asyncio module is designed to help you write asynchronous programs, allowing you to perform 
I/O-bound tasks (like fetching data from APIs, reading from a file, or handling many network connections) 
more efficiently by not blocking the program while waiting for those operations to complete.

Real-World Example: Fetching Data from Multiple APIs Concurrently 

Suppose you need to fetch data from multiple APIs (e.g., to gather stock prices or weather data) 
at the same time. Using traditional blocking I/O, you would have to wait for one API request to finish 
before moving on to the next. With asyncio, you can issue all requests concurrently and await their results.

"""
import asyncio
import aiohttp

# List of API endpoints to fetch data from
api_urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3"
]

async def fetch_data(session,url):
    async with session.get(url) as response:
        return await response.json()
    
async def main():

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(url=url,session=session) for url in api_urls]

        results = await asyncio.gather(*tasks)

        for res in results:
            print(res)

# Run the main function using asyncio
asyncio.run(main())
