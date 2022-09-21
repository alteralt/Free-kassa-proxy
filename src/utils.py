import aiohttp
from pydantic import HttpUrl


async def request(method: str, url: HttpUrl, **kwargs) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession() as session:
        response = await session.request(method, url, **kwargs)
        await response.read()

    return response
