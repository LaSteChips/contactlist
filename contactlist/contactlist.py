import sys
import sqlite3
import re
format_tel = "[0][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
format_email = "^[\w\.]+@([\w-]+\.)+[\w-]{2,9}$"
conn = sqlite3.connect('contact')
cur = conn.cursor()

def Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse):
    try:
        Insert_clients ='''INSERT INTO Contact VALUES(?,?,?,?,?,?)'''
        inserer = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
        cur.execute(Insert_clients, inserer)
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def list(): 
    try:
        sql = '''Select * from Contact'''
        result = cur.execute(sql)
        result = cur.fetchall()
        print("Il y a ", len(result), "contacts")
        for row in result:
            print("\n")
            print("nom", row[0])
            print("prénom", row[1])
            print("surnom", row[2])
            print("téléphone", row[3])
            print("mail", row[4])
            print("adresse", row[5])
            print("\n")
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def man():
    print("\n")
    print("\n")
    print("\n")
    print("Bonjour,")
    print("Voici les commandes possible d'effectuer ci-dessous.")
    print('\n')
    print("En tapant 1, vous pouvez ajouter un utilisateurs dans votre base de données, il vous faudra juste connaitre :")
    print("son Nom, son Prenom, lui donner un Surnom, son numéro de Téléphone, son adresse mail et son adresse.")
    print("En tapant 2, vous pouvez afficher toute la liste des contact que vous avez ajouter récemment.")
    print("En tapant 3, vous pouvez effectuer une recherche de manière plus précise (pour chercher un contact précis par exemple).")
    print("en tapant 4, vous pouvez réafficher cette interface d'aide.")
    print("En tapant 5, vous pouvez effacer un contact.")
    print("En tapant 6, vous pouvez modifier la donnée d'un des contacts")    

def search(zone, rechercher):
    try:
        if zone == "Nom":
            select = "Select * from Contact WHERE Nom LIKE ?"
        if zone == "Prénom":
            select = "Select * from Contact WHERE Prenom LIKE ?"
        if zone == "Téléphone":
            select = "Select * from Contact WHERE Téléphone LIKE ?"
        if zone == "Surnom":
            select = "Select * from Contact WHERE Surnom LIKE ?"
        if zone == "Email":
            select = "Select * from Contact WHERE Email LIKE ?"
        if zone == "Adresse":
            select = "Select * from Contact WHERE Adresse LIKE ?"
        utile = ('%'+rechercher+'%', )
        result = cur.execute(select, utile)
        result = cur.fetchall()
        for row in result:
            print("\n")
            print("nom", row[0])
            print("prénom", row[1])
            print("surnom", row[2])
            print("téléphone", row[3])
            print("mail", row[4])
            print("adresse", row[5])
            print("\n")
        conn.commit()
    except sqlite3.Error as error:
        print("Erreur dans la base de données", error)

def interact():
    choix = None
    print("Bienvenue dans le mode d'aide,")
    print("voici toutes les commandes que vous pouvez utilisé sur cette base de donnée.")
    while choix != "Au revoir.":
        print("Tapez 1 pour ajouter un contact ")
        print("Tapez 2 pour afficher la liste des contacts ")
        print("Tapez 3 pour rechercher un ou plusieurs contacts ")
        print("Tapez 4 pour avoir l'aide ")
        print("Tapez 5 pour supprimer un contact ")
        print("Tapez 6 pour modifier les informations d'un contact ")
        choix = input("Que souaihtez vous faire ? : ")
        if choix == "1":
            Nom= input('Quel est son nom ? : ')
            Prenom= input('Quel est son prénom ? : ')
            Surnom= input('Quel est surnom lui donnez vous ? : ')
            Telephone= input('Quel est son numéro de téléphone ? (veuillez respecter le format "0x-xx-xx-xx-xx"): ')
            Email = input('Quel est son Email ? (veuillez respecter le format "XXX.XXX@XXX.XXX"): ')
            Adresse= input("Quel est son adresse ? : ")
            Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            try: 
                Telephone_test = re.match(format_tel, Telephone)
                while Telephone_test == None:
                    print("La norme de téléphone n'est pas respecter, veillez a ce que le numero de telephone ressemble a ceci: 0x-xx-xx-xx-xx (n'oubliez pas les '-' entre chaque numéro)")
                    Telephone = input('Recommencez ici : ')
                    Telephone_test = re.match(format_tel, Telephone)
            except:
                print("")
            try: 
                Email_test = re.match(format_email, Email)
                while Email_test == None:
                    print("La norme de de l'email n'est pas respecter, veillez a ce que le mail ressemble a ceci:  XXX.XXX@XXX.XXX")
                    Email = input('Recommencez ici : ')
                    Email_test = re.match(format_email, Email)
            except:
                print("")
            print("Ajouter avec succès.")
            print("\n")      
        if choix == "2":    
            list()   
            print("\n")
        if choix == "3":
            zone = input("Sur quel zone spécifique (Nom/Prenom/Surnom/Téléphone/Email/Adresse) recherche-tu ? : ")
            rechercher = input("Quel donnée recherche tu ? ")
            search(zone, rechercher) 
            print("\n")
        if choix =="4":
            man()
            print("\n")
        if choix =="5":
            Nom= input('Quel est le nom de votre contact que vous voulez supprimer ?: ')
            Prenom= input('Quel est le prénom du contact que vous voulez supprimer ? : ')
            Surnom= input('Quel est le surnom du contact que vous voulez supprimer ? : ')
            Telephone= input('Quel est le numéro de téléphone du contact que vous voulez supprimer ? : ')
            Email= input('Quel est l Email du contact que vous voulez supprimer ? : ')
            Adresse= input("Quel est l'adresse du contact que vous voulez supprimer ? : ")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Suppression réussie.")
            print("\n")
        if choix =="6":
            Loca_update = input("Quel est la colonne a modifier (Nom/Prenom/Surnom/Téléphone/Email/Adresse): ")
            New_data = input("Quel est la nouvelle donnée : ")
            Nom= input('Quel est le nom de votre contact à mettre a jour : ')
            Prenom= input('Quel est le prénom de votre contact a mettre a jour : ')
            Surnom= input('Quel est le surnom de votre contact a mettre a jour : ')
            Telephone= input('Quel est le numéro de téléphone de votre contact a mettre a jour : ')
            Email= input('Quel est l Email de votre contact a mettre a jour : ')
            Adresse= input("Quel est l'adresse de votre contact a mettre a jour : ")
            maj(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse)
            try: 
                Telephone_test = re.match(format_tel, Telephone)
                while Telephone_test == None:
                    print("La norme de téléphone n'est pas respecter, veillez a ce que le numero de telephone ressemble a ceci: 0x-xx-xx-xx-xx (n'oubliez pas les '-' entre chaque numéro)")
                    Telephone = input('Recommencez ici : ')
                    Telephone_test = re.match(format_tel, Telephone)
            except:
                print("")
            try: 
                Email_test = re.match(format_email, Email)
                while Email_test == None:
                    print("La norme de de l'email n'est pas respecter, veillez a ce que le mail ressemble a ceci:  XXX.XXX@XXX.XXX")
                    Email = input('Recommencez ici : ')
                    Email_test = re.match(format_email, Email)
            except:
                print("")
            print("\n")

def supprimer(Nom, Prenom, Surnom, Telephone, Email, Adresse):
    try:
        Delete ='''Delete from Contact where Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
        Suppr = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
        cur.execute(Delete, Suppr)
        conn.commit()  
    except sqlite3.Error as error:
        print("Il y a une erreur avec la communication avec la base de données.", error)

def maj(Loca_update,New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse):
    if Loca_update == "Nom":
        Cmd ='''UPDATE Contact SET Nom = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Prenom":
        Cmd ='''UPDATE Contact SET Prenom = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Surnom":
        Cmd ='''UPDATE Contact SET Surnom = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Téléphone":
        Cmd ='''UPDATE Contact SET Téléphone = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Email":
        Cmd ='''UPDATE Contact SET Email = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Adresse":
        Cmd ='''UPDATE Contact SET Adresse = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    try:
        Update = (New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse)
        cur.execute(Cmd, Update)
        conn.commit()  
    except sqlite3.Error as error:
        print("y a un shmilblique mon petit gars ! ", error)

for arg in sys.argv:
    try:
        if sys.argv[1] == "new" :
            Nom= input('Quel est le nom de votre contact : ')
            Prenom= input('Quel est le prénom de votre contact : ')
            Surnom= input('Quel est le surnom de votre contact :')
            Telephone= input('Quel est le numéro de téléphone de votre contact : ')
            Email= input('Quel est l Email de votre contact ')
            Adresse= input("Quel est l'adresse de votre contact ")
            Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Contact ajouter avec succès.")
            break
              
        if sys.argv[1] == "list" :
            list()
            break

        if sys.argv[1] == "?":
            man()
            break
        if sys.argv[1] == "delete":
            Nom= input('Quel est le nom du contact ? :')
            Prenom= input('Quel est le prénom du contact ? :')
            Surnom= input('Quel est le surnom du contact ? :')
            Telephone= input('Quel est le numéro de téléphone du contact ? :')
            Email= input('Quel est l Email du contact ? :')
            Adresse= input("Quel est l'adresse du contact ? :")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Félicitation !")
            print("tu viens de rayer ce contact de la réalité B)")
            break
            
        if sys.argv[1] == "update":
            Loca_update = input("Quel colonne est à modifier (Nom/Prenom/Surnom/Téléphone/Email/Adresse) ? : ")
            New_data = input("Mais quel est donc ta nouvelle donnée ? : ")
            Nom= input('Par quel nom doit-il être mis a jour ? : ')
            Prenom= input('Par quel Prenom doit-il être mis a jour ? :')
            Surnom= input('Par quel Surnom doit-il être mis a jour ? :')
            Telephone= input('Par quel numéro de téléphone doit-il être mis a jour ? : ')
            Email= input('Par quel adresse Email doit-il être mis a jour ?: ')
            Adresse= input("Par quel adresse doit-il être mis a jour ? : ")
            maj(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse)
            break
        
        if sys.argv[1] == "search":
            rechercher = sys.argv[3]
            try:
                if sys.argv[2] == "--by-name" :
                    zone = "Nom"
                if sys.argv[2] == "--by-tel" :
                    zone = "Téléphone"
                if sys.argv[2] == "--by-email" :
                    zone = "Email"
                if sys.argv[2] == "--by-nickname" :
                    zone = "Surnom"
                if sys.argv[2] == "--by-firstname" :
                    zone = "Prenom"
                if sys.argv[2] == "--by-address" :
                    zone = "Adresse"
                search(zone, rechercher)
            except:
                    print ("Il y a une erreur dans la commande,")
                    print ("veuillez consulter le menu d'aide si vous en avez besoin.")
            break
    except:
            interact()
