import asyncio


async def my_sleep():
    await asyncio.sleep(10)


async def main():
    await my_sleep()

asyncio.run(main())
