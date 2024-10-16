import asyncio
import time

from say_after import say_after

# async def main():
#     await say_after(1, 'hello')
#     await say_after(2, 'world')

# async def main():
#     task1 = asyncio.create_task(say_after(1, 'hello'))
#     task2 = asyncio.create_task(say_after(2, 'world'))
    
#     print(f"started at {time.strftime('%X')}")
#     await task1
#     await task2
#     print(f"finished at {time.strftime('%X')}")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, 'hello'))
        tg.create_task(say_after(2, 'world'))
        print(f"started at {time.strftime('%X')}")
    
    print(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())
