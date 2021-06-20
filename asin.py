import asyncio
import httpx


async def download(query, current_page):
    header = {"Authorization": "API_KEY"}
    params = {"query": query, "per_page": 1, "page": current_page}
    url = f"https://api.pexels.com/v1/search"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get("photos"):
                print(item.get("src").get("original"))
        else:
            print(r.status_code)
    print(f'{query} = {current_page}')


async def main():
    queue = asyncio.Queue()
    query = input("Query ")
    page_count = int(input("Pages "))

    current_page = 0
    task_list = []
    while current_page < page_count:
        current_page += 1
        task = asyncio.create_task(download(query, current_page))
        task_list.append(task)

    await queue.join()
    await asyncio.gather(*task_list, return_exceptions=True)
        # await download(query, current_page)
    print('done')

asyncio.run(main())
