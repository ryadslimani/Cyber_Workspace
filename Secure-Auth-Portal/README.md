# Cyber_Workspace

## 🛡️ Vue d'ensemble
Bienvenue sur **Cyber_Workspace**, un dépôt de portfolio professionnel regroupant des projets axés sur la cybersécurité, l'ingénierie des systèmes, le développement d'applications sécurisées et les méthodologies Red/Blue Team. Ce dépôt centralise différentes applications et scripts pour démontrer des compétences concrètes en programmation, durcissement des systèmes et conception d'architectures sécurisées.

---

## 📂 Structure du Dépôt

```text
Cyber_Workspace/
│
├── Purple-Scan-Lab/      # Scripts d'analyse offensive (Red Team) et de détection (Blue Team)
├── Secure-Auth-Portal/   # Module d'authentification sécurisée et gestion de base de données
└── README.md             # Documentation globale du portfolio

## 🛠️ Présentation Détaillée

### 2. Secure-Auth-Portal
* **Objectif stratégique** : Concevoir et implémenter une application modulaire en Python rigoureuse, illustrant les standards industriels en matière de sécurité logicielle, de contrôle d'accès et d'intégrité des données.
* **Architecture technique et modulaire** :
  * `main.py` : Point d'entrée principal de l'application proposant une interface interactive en ligne de commande (CLI) fluide et structurée pour orchestrer l'ensemble des flux utilisateurs.
  * `auth.py` : Moteur de gestion de la logique d'authentification et des sessions. Intègre un hachage cryptographique robuste des mots de passe (via l'algorithme SHA-256) afin de garantir qu'aucune donnée sensible ou information d'identification en clair ne transite ou ne soit stockée.
  * `database.py` : Couche d'interaction et d'abstraction avec une base de données SQLite (`secure_portal.db`). Utilise des requêtes paramétrées de manière stricte pour neutraliser l'exposition aux vulnérabilités courantes de type injections SQL.