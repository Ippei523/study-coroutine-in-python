import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)