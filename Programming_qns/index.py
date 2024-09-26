import asyncio

async def get_products():
    print('getting products')
    await asyncio.sleep(2) # instaed of an actual api call added timeer to simulate the actual api call
    return {'name':'product1'}

async def get_orders():
    print('getting orders')
    await asyncio.sleep(2)
    return {'order1':'clothorder'}

async def task1():
    x = await get_products()
    print(x)

async def task2():
    y = await get_orders()
    print(y)

async def call_apis():
    ps = asyncio.create_task(task1())
    os = asyncio.create_task(task2())

    # await ps
    # await os

asyncio.run(call_apis())


"""
Event Loop is managing the await . managing the request when it gets the response it returns back to the same 
program and calls 
* RUns asynchornous tasks and callbacks and cordinates 
"""