import httpx

from base import AccountingIntegration

class DineroClient(AccountingIntegration):
    BASE_URL = "https://api.dinero.dk/v1"
    AUTH_URL = "https://authz.dinero.dk/dineroapi/oauth/token"

    def __init__(self, client_id: str, client_secret: str, api_key: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_key = api_key
        self.access_token: str | None = None
        self._client = httpx.AsyncClient()

    async def authenticate(self) -> None:
        data = {
            "grant_type": "password",
            "scope": "read write",
            "username": self.api_key,
            "password": self.api_key,
        }

        response = await self._client.post(
            self.AUTH_URL,
            data=data,
            auth=(self.client_id, self.client_secret),
        )
        response.raise_for_status()
        self.access_token = response.json()["access_token"]

    async def get_invoices(self, organization_id: str) -> dict:
        response = await self._request("GET", f"/{organization_id}/invoices")
        return response.json()

    async def get_saldo_report(self, organization_id: str, accounting_year: str) -> dict:
        response = await self._request("GET", f"/{organization_id}/{accounting_year}/reports/saldo")
        return response.json()

    async def _request(self, method: str, path: str, **kwargs) -> httpx.Response:
        if not self.access_token:
            raise RuntimeError("Not authenticated. Call authenticate() first.")

        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"

        response = await self._client.request(
            method,
            f"{self.BASE_URL}{path}",
            headers=headers,
            **kwargs,
        )
        response.raise_for_status()
        return response

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, _exc_type, _exc_val, _exc_tb):
        await self.close()


if __name__ == "__main__":
    import asyncio
    import os
    from dotenv import load_dotenv

    load_dotenv()

    async def main():
        client = DineroClient(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            api_key=os.getenv("API_KEY"),
        )
        await client.authenticate()
        #invoices = await client.get_invoices(os.getenv("ORGANIZATION_ID"))
        saldo = await client.get_saldo_report(os.getenv("ORGANIZATION_ID"), "2025")
        print(saldo)
        await client.close()

    asyncio.run(main())