import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")


async def get_summary():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/team/summary")
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    import asyncio


    async def main():
        summary = await get_summary()
        print(summary)


    asyncio.run(main())
