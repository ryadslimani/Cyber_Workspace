import socket
import sys
from datetime import datetime

# Cible à scanner (127.0.0.1 pour votre propre machine)
target_host = "127.0.0.1"

# Liste des ports qu'on va tester (les plus courants)
ports_to_check = [21, 22, 80, 443, 3306, 8080, 9999]

print("-" * 50)
print(f"Scan de la cible : {target_host}")
print(f"Heure de début : {str(datetime.now())}")
print("-" * 50)

try:
    for port in ports_to_check:
        # Création du socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # Timeout d'une seconde pour aller vite
        
        # Tentative de connexion au port
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f"[+] Le port {port} est OUVERT")
        else:
            print(f"[-] Le port {port} est fermé")
            
        s.close()

except KeyboardInterrupt:
    print("\nArrêt du script par l'utilisateur.")
    sys.exit()