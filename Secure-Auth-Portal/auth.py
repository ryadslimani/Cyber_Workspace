import hashlib

class AuthManager:
    def __init__(self, db):
        self.db = db

    def hash_password(self, password):
        """Hache le mot de passe avec SHA-256 pour le stockage sécurisé."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if not username or not password:
            return False, "Le nom d'utilisateur et le mot de passe sont obligatoires."
        
        password_hash = self.hash_password(password)
        success = self.db.add_user(username, password_hash)
        
        if success:
            return True, "Inscription réussie !"
        return False, "Ce nom d'utilisateur existe déjà."

    def login(self, username, password):
        user = self.db.get_user(username)
        if not user:
            return False, "Utilisateur inconnu."
        
        stored_hash = user[2]
        if stored_hash == self.hash_password(password):
            return True, "Connexion réussie !"
        return False, "Mot de passe incorrect."