import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'), name='helloの表示')
    task2 = asyncio.create_task(say_after(2, 'world'), name='worldの表示')
    
    print(f"task1: {task1.get_name()}")
    print(f"task2: {task2.get_name()}")
    
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
    
if __name__ == '__main__':
    asyncio.run(main())