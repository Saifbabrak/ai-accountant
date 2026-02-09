import httpx


async def authenticate(uri: str, client_id: str, client_secret: str, api_key: str) -> dict:
    data = {
        "grant_type": "password",
        "scope": "read write",
        "username": api_key,
        "password": api_key,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            uri,
            data=data,
            auth=(client_id, client_secret),
        )
        response.raise_for_status()
        return response.json()
    
if __name__ == "__main__":
    import asyncio
    import os
    from dotenv import load_dotenv

    load_dotenv()

    uri = os.getenv("URI")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    api_key = os.getenv("API_KEY")

    print(asyncio.run(authenticate(uri, client_id, client_secret, api_key)))