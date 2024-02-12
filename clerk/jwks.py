from clerk.client import Service


class JWKSService(Service):
    endpoint = "jwks"

    async def retrieve_jwks(self) -> dict:
        """Retrieve JWKS"""
        async with self._client.get(self.endpoint) as r:
            jwks = await r.json()
            return jwks