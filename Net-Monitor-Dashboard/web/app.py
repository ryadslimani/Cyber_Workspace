import json
import os
import socket
from flask import Flask, render_template_string

app = Flask(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def check_port(host, port, timeout=2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

# Template HTML ultra-moderne et épuré
TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Net-Monitor | Security Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #090d16;
            --card-bg: #111827;
            --border-color: #1f2937;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --accent-glow: rgba(59, 130, 246, 0.15);
            --success: #10b981;
            --danger: #ef4444;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 20px;
        }

        .wrapper {
            width: 100%;
            max-width: 1000px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 35px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 20px;
        }

        .logo-area h1 {
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: -0.025em;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo-area p {
            color: var(--text-muted);
            font-size: 0.875rem;
            margin-top: 4px;
        }

        .refresh-btn {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
            padding: 10px 18px;
            font-size: 0.875rem;
            font-weight: 600;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }

        .refresh-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4);
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 20px;
        }

        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .card:hover {
            border-color: #374151;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }

        .target-name {
            font-size: 1.1rem;
            font-weight: 600;
            color: #ffffff;
        }

        .target-ip {
            font-family: monospace;
            background: #1f2937;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        .ports-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .port-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0d131f;
            padding: 10px 14px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }

        .port-info {
            font-size: 0.9rem;
            font-weight: 500;
            color: #d1d5db;
        }

        .badge {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .badge-ok {
            background: rgba(16, 185, 129, 0.1);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }

        .badge-err {
            background: rgba(239, 68, 68, 0.1);
            color: var(--danger);
            border: 1px solid rgba(239, 68, 68, 0.2);
        }

        .dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
        }

        .badge-ok .dot { background-color: var(--success); box-shadow: 0 0 8px var(--success); }
        .badge-err .dot { background-color: var(--danger); box-shadow: 0 0 8px var(--danger); }
    </style>
</head>
<body>
    <div class="wrapper">
        <header>
            <div class="logo-area">
                <h1>🛡️ Net-Monitor Dashboard</h1>
                <p>Surveillance active et analyse de l'infrastructure réseau</p>
            </div>
            <a href="/" class="refresh-btn">🔄 Actualiser</a>
        </header>

        <div class="grid-container">
            {% for target in targets_data %}
            <div class="card">
                <div class="card-header">
                    <span class="target-name">{{ target.name }}</span>
                    <span class="target-ip">{{ target.host }}</span>
                </div>
                <div class="ports-list">
                    {% for port_info in target.ports_status %}
                    <div class="port-row">
                        <span class="port-info">Port TCP {{ port_info.port }}</span>
                        <div class="badge {% if port_info.status %}badge-ok{% else %}badge-err{% endif %}">
                            <span class="dot"></span>
                            {% if port_info.status %}Actif [OK]{% else %}Injoignable [Alerte]{% endif %}
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    config = load_config()
    targets_data = []
    
    for target in config["targets"]:
        ports_status = []
        for port in target["ports"]:
            status = check_port(target["host"], port)
            ports_status.append({"port": port, "status": status})
        
        targets_data.append({
            "name": target["name"],
            "host": target["host"],
            "ports_status": ports_status
        })
        
    return render_template_string(TEMPLATE, targets_data=targets_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)