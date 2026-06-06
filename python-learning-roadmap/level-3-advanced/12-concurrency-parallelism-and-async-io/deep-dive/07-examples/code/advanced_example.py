import asyncio

async def fetch(name: str) -> str:
    await asyncio.sleep(1)
    return f"response:{name}"

async def main():
    results = await asyncio.gather(fetch("a"), fetch("b"), fetch("c"))
    print(results)

asyncio.run(main())
