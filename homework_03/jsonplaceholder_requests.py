"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_data() -> tuple:
    result = await asyncio.gather(
        fetch_json(url=USERS_DATA_URL),
        fetch_json(url=POSTS_DATA_URL)
    )

    return tuple(result)
