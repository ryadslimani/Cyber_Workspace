import socket
import sys
from datetime import datetime

def run_detector(host="127.0.0.1", port=9999):
    # Création du socket serveur (Blue Team)
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        listener.bind((host, port))
        listener.listen(5)
        print(f"[*] Blue Team Detector actif sur {host}:{port}")
        print("[*] En attente d'activités suspectes (Scans/Connexions)...")
        
        while True:
            client_socket, client_address = listener.accept()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[ALERTE SECU] [{timestamp}] Connexion entrante détectée !")
            print(f" > Adresse IP suspecte : {client_address[0]}")
            print(f" > Port source : {client_address[1]}")
            
            # On coupe immédiatement la connexion pour simuler un honeypot défensif
            client_socket.close()
            
    except KeyboardInterrupt:
        print("\n[!] Arrêt du détecteur par l'utilisateur.")
        listener.close()
        sys.exit()

if __name__ == "__main__":
    run_detector()