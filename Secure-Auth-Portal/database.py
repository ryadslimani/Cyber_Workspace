import sqlite3

class Database:
    def __init__(self, db_name="secure_portal.db"):
        self.db_name = db_name
        self.init_db()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        """Initialise la table des utilisateurs si elle n'existe pas."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_user(self, username, password_hash):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False  # L'utilisateur existe déjà

    def get_user(self, username):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user