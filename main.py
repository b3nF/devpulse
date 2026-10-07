import asyncio
import sys
import yaml
from rich.console import Console
from rich.table import Table
from rich.live import Live
from devpulse.monitor import HealthChecker
from devpulse.notifier import Notifier

console = Console()

def load_config(config_path: str = "config.yaml"):
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        console.print("[bold red]Hata:[/bold red] `config.yaml` dosyası bulunamadı.")
        sys.exit(1)

def build_table(results) -> Table:
    table = Table(title="DevPulse - Altyapı ve API Sağlık Durumu", title_style="bold cyan")
    table.add_column("Servis Adı", style="bold white")
    table.add_column("URL", style="dim")
    table.add_column("Durum", justify="center")
    table.add_column("HTTP Kodu", justify="center")
    table.add_column("Gecikme (ms)", justify="right")

    for res in results:
        status_str = "[bold green]ONLINE[/bold green]" if res["is_up"] else "[bold red]OFFLINE[/bold red]"
        code_str = str(res["status_code"]) if res["status_code"] is not None else "N/A"
        latency_str = f"{res['latency_ms']} ms"

        table.add_row(
            res["name"],
            res["url"],
            status_str,
            code_str,
            latency_str
        )
    return table

async def main():
    config = load_config()
    services = config.get("services", [])
    interval = config.get("check_interval", 5)
    webhook_url = config.get("notifications", {}).get("webhook_url", "")

    checker = HealthChecker(services)
    notifier = Notifier(webhook_url)

    console.print("[bold green]DevPulse İzleme Başlatılıyor... Çıkış için Ctrl+C[/bold green]\n")

    try:
        with Live(console=console, refresh_per_second=2) as live:
            while True:
                results = await checker.check_all()

                for res in results:
                    if not res["is_up"]:
                        reason = res["error"] if res["error"] else f"Beklenmeyen HTTP Kodu: {res['status_code']}"
                        await notifier.send_alert(res["name"], res["url"], reason)

                live.update(build_table(results))
                await asyncio.sleep(interval)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]DevPulse durduruldu.[/bold yellow]")

if __name__ == "__main__":
    asyncio.run(main())
