from database import Database
from auth import AuthManager

def main():
    db = Database()
    auth = AuthManager(db)

    print("=== Secure Auth Portal ===")
    
    while True:
        print("\n1. S'inscrire")
        print("2. Se connecter")
        print("3. Quitter")
        
        choice = input("Choisissez une option (1-3) : ").strip()
        
        if choice == "1":
            username = input("Nom d'utilisateur : ").strip()
            password = input("Mot de passe : ").strip()
            success, message = auth.register(username, password)
            print(f">> {message}")
            
        elif choice == "2":
            username = input("Nom d'utilisateur : ").strip()
            password = input("Mot de passe : ").strip()
            success, message = auth.login(username, password)
            print(f">> {message}")
            
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()