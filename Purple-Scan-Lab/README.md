# Purple-Scan-Lab

Projet d'apprentissage en cybersécurité combinant des approches offensives (Red Team) et défensives (Blue Team).

## Structure du projet
- `red-team/` : Scripts de reconnaissance et d'audit (ex: scanner de ports TCP).
- `blue-team/` : Futurs scripts de détection et de surveillance des flux.

## Outils utilisés
- Python 3 (Bibliothèque `socket`)
- Visual Studio Code

## Utilisation du scanner (Red Team)
1. Se placer dans le dossier : `cd red-team`
2. Lancer le script : `python scanner.py`

## ⚔️ Red Team - Reconnaissance & Balayage

La brique offensive implémente un outil de découverte réseau programmé pour identifier les services actifs et tester l'ouverture des ports d'une cible.

### Fonctionnement du Scanner (`/red-team/scanner.py`)
- **Connexions TCP ciblées :** Le script utilise des sockets pour tenter d'établir des connexions de type handshakes sur une liste de ports prédéfinis.
- **Analyse des retours :** 
  - Si la connexion aboutit, le port est considéré comme **ouvert** (service actif détecté).
  - Si la connexion échoue ou est refusée, le port est consigné comme **fermé**.
- **Horodatation :** Chaque exécution de scan est enregistrée avec un horodatage précis pour assurer la traçabilité des opérations de reconnaissance.

### 🧪 Scénario d'Utilisation Offensive
1. Se placer dans le dossier de la brique offensive :
   ```bash
   cd red-team

## 🛡️ Blue Team - Détection & Analyse

La brique défensive met en œuvre un script de surveillance (honeypot minimaliste) conçu pour détecter les activités de reconnaissance et les tentatives de balayage réseau.

### Fonctionnement du Détecteur (`/blue-team/detector.py`)
- **Écoute active :** Le script se positionne sur un port cible stratégique (`9999`) pour intercepter les connexions entrantes non autorisées.
- **Journalisation des alertes :** Dès qu'un socket distant tente d'établir une connexion, le script horodate l'événement et extrait instantanément les métadonnées de l'attaquant :
  - Adresse IP source (`client_address[0]`)
  - Port source (`client_address[1]`)
- **Fermeture défensive :** La connexion est immédiatement coupée (`client_socket.close()`) pour simuler un comportement de leurre et empêcher toute intrusion prolongée.

### 🧪 Scénario de Test Purple Team
1. Lancer l'écouteur défensif dans le terminal :
   ```bash
   cd blue-team
   python detector.py