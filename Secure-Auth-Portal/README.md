# Secure-Auth-Portal

Application modulaire en Python conçue pour démontrer les bonnes pratiques en matière de gestion des identités, de contrôle d'accès rigoureux et de persistance sécurisée des données.

## 📂 Structure du Projet
- `main.py` : Point d'entrée de l'application et gestion de l'interface en ligne de commande (CLI).
- `auth.py` : Moteur de logique d'authentification et de sécurité cryptographique.
- `database.py` : Couche d'abstraction des données et gestion de la base SQLite.

## 🛠️ Outils & Technologies Utilisés
- **Langage :** Python 3 (programmation orientée modules)
- **Base de données :** SQLite (`secure_portal.db`)
- **Sécurité :** Hachage cryptographique SHA-256 et requêtes paramétrées anti-injection SQL
- **Environnement de développement :** Visual Studio Code

---

## 🔐 Architecture & Sécurité Applicative

Ce projet met en œuvre des standards stricts de développement sécurisé pour s'assurer qu'aucune information sensible n'est compromise lors des flux d'authentification.

### 1. Point d'Entrée et Interface (`main.py`)
- **Orchestration des flux :** Fait office de chef d'orchestre pour l'application en proposant un menu interactif clair en ligne de commande (CLI).
- **Expérience utilisateur :** Permet de basculer intuitivement entre les phases d'inscription, de connexion et la gestion des sessions de manière fluide et sécurisée.

### 2. Moteur d'Authentification (`auth.py`)
- **Intégrité des mots de passe :** Aucun mot de passe utilisateur n'est manipulé ou stocké en clair. Le module applique systématiquement un hachage cryptographique irréversible (algorithme **SHA-256**).
- **Vérification des accès :** Compare les empreintes numériques hachées lors des tentatives de connexion pour valider ou rejeter l'authentification en toute sécurité.

### 3. Couche Persistance & Base de Données (`database.py`)
- **Gestion SQLite :** Automatise la création, la configuration et la liaison avec le fichier de base de données local (`secure_portal.db`).
- **Blindage contre les Injections SQL :** Utilise exclusivement des **requêtes paramétrées** pour séparer le code SQL des données utilisateurs entrantes, neutralisant ainsi les risques d'injections malveillantes.

---

## 🚀 Guide d'Exécution & Scénario d'Utilisation

Pour lancer et tester l'application en local sur votre environnement de travail :

1. Se placer dans le répertoire du projet :
   ```bash
   cd Secure-Auth-Portal
   python main.py