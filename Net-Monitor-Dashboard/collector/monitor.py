import json
import os
import socket
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def check_port(host, port, timeout=2):
    """Teste si un port TCP est ouvert sur une cible donnée."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def run_checks():
    config = load_config()
    print(f"[*] --- Démarrage du scan réseau : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

    for target in config["targets"]:
        print(f"\n[Cible] {target['name']} ({target['host']})")
        for port in target["ports"]:
            status = check_port(target["host"], port)
            state_str = "OUVERT [OK]" if status else "FERMÉ/BLOQUÉ [ALERTE]"
            print(f"  -> Port {port}: {state_str}")

if __name__ == "__main__":
    run_checks()