import sqlite3

print("APPLICATION CONSOLE POO-PYTHON DE GESTION DE CONTACTS")

with sqlite3.connect("dbcontacts.db") as connection:
    cursor = connection.cursor()
 
    
 # Pour la creation d'une table nommé contacte  
def create_table():
    cursor.execute("CREATE TABLE if not exists contacts (idcont INTEGER PRIMARY KEY AUTOINCREMENT,nomPrenom TEXT, email TEXT, telephone TEXT,adresse TEXT)")
    connection.commit()
create_table()

class Contact :
    def __init__(self,ajouter_contact,affichage_contacts,affichageUN_contact,supression_contact,modifier_contact) :
        self.ajouter_contact=ajouter_contact
        self.affichage_contacts=affichage_contacts
        self.affichageUN_contact=affichageUN_contact
        self.supression_contact=supression_contact
        self.modifier_contact=modifier_contact
        
        
    def ajouter_contact(self):
        cursor.execute("INSERT INTO contacts(nomPrenom, email, telephone,adresse) VALUES('Ishaka ISSA', 'issa@gmail.com', '778769084','Dakar')")
        cursor.execute("INSERT INTO contacts(nomPrenom, email, telephone,adresse) VALUES('Ishaka YOUSSOUF', 'yousef@gmail.com', '002693230484','Comores')")
        cursor.execute("INSERT INTO contacts(nomPrenom, email, telephone,adresse) VALUES('Ishaka FATIMA', 'isfatim@gmail.com','789087654' ,'Senegal')")
        cursor.execute("INSERT INTO contacts(nomPrenom, email, telephone,adresse) VALUES('Said ALI', 'said@gmail.com','002692568909','Comores')")
        connection.commit()
    print(ajouter_contact(cursor))
    print("Données ajouter avec succée.Merci !!!!!")
    
     # Permet d'afficher toutes les contacts
    def affichage_contacts():
        print("Afficher les contacts")
        rows = cursor.execute("SELECT * FROM contacts").fetchall()
        print(rows)
    print("Contactes listés.Merci !!!!!",affichage_contacts())
    
    #Permer de chercher un contacte c'est a dire afficher un seul contact
    def affichageUN_contact():
        print("Cherher et afficher un contacte s'il vous plait ")
        row = cursor.execute("SELECT * FROM contacts WHERE telephone = 778769084").fetchone()
        print(row)
    print("Merci !!!!!!!!",affichageUN_contact())  
    
    # Permet de suprimer un contact deja enregistrer
    def supression_contact():
        print("Suprime cette contacte s'il vous plais")
        telephone = "789087654"
        cursor.execute("DELETE FROM contacts WHERE telephone = ?",
        (telephone,))
    connection.commit()
    print("Le contacte est suprimer avec succée. Merci !!!",supression_contact())
    
    #Permer de modifier un contact
    def modifier_contact():
        print("Veuillez modifier cette contacte s'il vous plait")
        nvNum = "789769084"
        numAncien = "778769084"
        cursor.execute("UPDATE contacts SET telephone = ? WHERE telephone = ?",
        (nvNum, numAncien))
    connection.commit()
    print("Contacte modifier avec succée",modifier_contact())


    
        
    
    