# Net-Monitor-Dashboard

Tableau de bord et outil de surveillance réseau en temps réel, conçu pour auditer la disponibilité des hôtes critiques et l'état des ports de services stratégiques.

## 📂 Structure du Projet
- `collector/` : Contient les scripts de sonde et d'analyse bas niveau.
  - `monitor.py` : Script principal de scan et de vérification des flux TCP.
- `config.json` : Fichier de configuration centralisé définissant les cibles et les ports à surveiller.

## 🛠️ Outils & Technologies Utilisés
- **Langage :** Python 3 (programmation orientée réseau)
- **Protocoles :** Sockets TCP, Résolution réseau
- **Format de configuration :** JSON
- **Environnement de développement :** Visual Studio Code

---

## 🔍 Architecture & Fonctionnement

Ce projet automatise le diagnostic de l'infrastructure en combinant un fichier de configuration modulaire et un script de test de connectivité.

### 1. Fichier de Configuration (`config.json`)
- Permet de déclarer dynamiquement les machines cibles (par nom, adresse IP) et la liste des ports associés à auditer (ex: services Web, SSH, Bases de données, DNS).

### 2. Moteur de Collecte (`collector/monitor.py`)
- **Connexions Sockets :** Utilise des requêtes de test bas niveau pour tenter d'établir un échange de type handshake sur les ports ciblés avec un délai d'attente (*timeout*) maîtrisé.
- **Journalisation de l'État :** Analyse les retours de connexion pour distinguer en temps réel les services actifs (`OUVERT [OK]`) des services injoignables ou filtrés (`FERMÉ/BLOQUÉ [ALERTE]`).

---

## 🚀 Guide d'Exécution

Pour lancer une session de surveillance réseau depuis votre environnement local :

1. Se placer dans le répertoire du projet :
   ```bash
   cd Net-Monitor-Dashboard
   python collector/monitor.py
   cd Net-Monitor-Dashboard/web
   python app.py