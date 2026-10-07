import httpx

class Notifier:
    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url

    async def send_alert(self, service_name: str, url: str, reason: str):
        if not self.webhook_url:
            return

        payload = {
            "content": f"🚨 **DevPulse Uyarısı**: `{service_name}` ({url}) erişilemez durumda!\nNeden: `{reason}`"
        }

        try:
            async with httpx.AsyncClient() as client:
                await client.post(self.webhook_url, json=payload)
        except Exception as e:
            print(f"[Uyarı] Webhook bildirimi gönderilemedi: {e}")
