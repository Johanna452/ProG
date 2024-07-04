import mysql.connector

#PROJECTS
def addNewProject(nomProjet,description,objectifs) :
    try:
        database = mysql.connector.connect(host="localhost", user="root", password="", database="progest")
        cursor = database.cursor()
        cursor.execute("INSERT INTO projet VALUES (%s,%s,%s)", (nomProjet, description, objectifs))
        database.commit()
        database.close()
        return True
    except:#erreur
        return False

def getAllProjects():
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    cursor.execute("SELECT nomProjet FROM projet")
    nomProjet = cursor.fetchall()
    return nomProjet

#USERS
def addNewUser(mail,mdp,username):
    try:
        database = mysql.connector.connect(host="localhost", user="root", password="", database="progest")
        cursor = database.cursor()
        cursor.execute("INSERT INTO utilisateur VALUES (%s,%s,%s)",(mail,mdp,username))
        database.commit()
        database.close()
        return True
    except:
        return False

def getUser():
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    cursor.execute("SELECT username FROM utilisateur")
    users = cursor.fetchall()
    return users