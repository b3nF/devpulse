import asyncio
import time
from typing import Dict, Any, List
import httpx

class HealthChecker:
    def __init__(self, services: List[Dict[str, Any]]):
        self.services = services

    async def check_service(self, client: httpx.AsyncClient, service: Dict[str, Any]) -> Dict[str, Any]:
        url = service.get("url")
        name = service.get("name")
        expected_status = service.get("expected_status", 200)
        timeout = service.get("timeout", 5.0)

        start_time = time.perf_counter()
        try:
            response = await client.get(url, timeout=timeout)
            latency = (time.perf_counter() - start_time) * 1000
            is_up = response.status_code == expected_status

            return {
                "name": name,
                "url": url,
                "status_code": response.status_code,
                "latency_ms": round(latency, 2),
                "is_up": is_up,
                "error": None
            }
        except Exception as e:
            latency = (time.perf_counter() - start_time) * 1000
            return {
                "name": name,
                "url": url,
                "status_code": None,
                "latency_ms": round(latency, 2),
                "is_up": False,
                "error": str(e)
            }

    async def check_all(self) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            tasks = [self.check_service(client, s) for s in self.services]
            return await asyncio.gather(*tasks)
