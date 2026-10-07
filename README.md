# DevPulse

**An Asynchronous API & Infrastructure Health Monitoring Tool with Terminal UI and Webhook Alerts**

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Features](#-key-features) • [Installation](#%EF%B8%8F-installation) • [Configuration](#%EF%B8%8F-configuration) • [Usage](#-usage) • [Contributing](#-contributing)

---

</div>

## About DevPulse

**DevPulse** is a modern, lightweight CLI application built with **Python 3**, **`httpx`**, and **`rich`**. It asynchronously monitors microservices, API endpoints, and web servers in real time, displaying vital stats such as HTTP status codes, response latencies, and uptime state on a dynamic terminal interface. 

When a monitored endpoint experiences downtime or returns an unexpected status code, DevPulse instantly sends automated alert notifications via Discord or Slack webhooks.

---

##  Key Features

- **Asynchronous Execution**: Pings dozens of endpoints concurrently without blocking or suffering from network latency bottlenecks using `httpx` and `asyncio`.
- **Real-time Live Terminal Dashboard**: Clean, responsive, and color-coded table UI rendered directly in your terminal using `rich`.
-  **Simple YAML Configuration**: Easily define targeted endpoints, expected status codes, check intervals, and custom request timeouts.
-  **Webhook Alerts**: Instant crisis notification support for **Discord** and **Slack** webhooks when an endpoint fails.
-  **Fault Tolerant**: Handles connection timeouts, DNS failures, and HTTP errors gracefully.

---

## Project Architecture

```text
devpulse/
│
├── devpulse/
│   ├── __init__.py        # Package initializer
│   ├── monitor.py         # Asynchronous health check logic using httpx
│   └── notifier.py        # Webhook notification handler
│
├── config.yaml            # Service configuration & target definitions
├── main.py                # Main entry point and CLI runner
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## Prerequisites & Dependencies

Make sure you have **Python 3.9+** installed on your system.

Core dependencies:
- **`httpx`**: Modern asynchronous HTTP client.
- **`rich`**: Rich text and beautiful terminal formatting.
- **`pyyaml`**: YAML file parser for configurations.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/devpulse.git
   cd devpulse
   ```

2. **Create and Activate a Virtual Environment**
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/venv
     ```
   - **Windows**:
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

##  Configuration

Customize your targets in the `config.yaml` file located in the root directory.

### Example `config.yaml`

```yaml
# Global monitoring interval (in seconds)
check_interval: 5

# List of endpoints to monitor
services:
  - name: "Google Main Search"
    url: "https://www.google.com"
    expected_status: 200
    timeout: 3.0

  - name: "JSONPlaceholder Test API"
    url: "https://jsonplaceholder.typicode.com/posts/1"
    expected_status: 200
    timeout: 2.0

  - name: "Failing Test Endpoint"
    url: "https://httpbin.org/status/500"
    expected_status: 200
    timeout: 3.0

# Alert Settings (Optional)
notifications:
  webhook_url: "https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK_URL"
```

### Configuration Parameters Explained

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `check_interval` | `integer` | Frequency of checks in seconds across all endpoints. |
| `name` | `string` | Display name of the service in the CLI table. |
| `url` | `string` | Target HTTP/HTTPS URL endpoint. |
| `expected_status` | `integer` | Target HTTP status code considered as `ONLINE` (e.g., `200`). |
| `timeout` | `float` | Maximum time in seconds to wait for a response before marking as timed out. |
| `webhook_url` | `string` | Discord or Slack webhook URL for automated alerts (leave empty to disable). |

---

## Usage

Run the monitor using the main script:

```bash
python main.py
```

To stop monitoring, press `Ctrl + C` in your terminal.

---

## Webhook Setup

### Discord Webhook Integration
1. Open your Discord server settings -> **Integrations** -> **Webhooks**.
2. Create a new webhook and copy the Webhook URL.
3. Paste the URL into `notifications.webhook_url` inside `config.yaml`.

### Slack Webhook Integration
1. Create a Slack App in your workspace and enable **Incoming Webhooks**.
2. Copy the generated Webhook URL.
3. Paste the URL into `notifications.webhook_url` inside `config.yaml`.

---

## Roadmap & Future Improvements

- [ ] Export uptime metrics to **Prometheus** / **Grafana**.
- [ ] Historical uptime logs saved to a local SQLite database or JSON file.
- [ ] Email notifications via SMTP.
- [ ] Support for TCP and Ping (ICMP) protocol checks.
- [ ] Dockerized deployment support (`Dockerfile` + `docker-compose`).

---

## Contributing

Contributions are always welcome! If you'd like to improve DevPulse:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AwesomeFeature`)
3. Commit your Changes (`git commit -m 'Add some AwesomeFeature'`)
4. Push to the Branch (`git push origin feature/AwesomeFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <sub>Created with ❤️ for developers and system administrators.</sub>
</div>
