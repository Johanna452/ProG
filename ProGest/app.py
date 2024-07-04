
from flask import Flask, render_template, request
from model import addNewProject,addNewUser,getAllProjects

app = Flask(__name__)

@app.route("/")
def index(): #afficher formulaire de connexion
    return render_template("index.html")


@app.route('/traitement', methods=['POST'])
def traitement():
    username = request.form.get('username')
    mdp = request.form.get('mdp')
    mail = request.form.get('mail')

    if username == 'admin':
        donnees = request.form
        nomProjet = donnees.get('nomProjet')
        description = donnees.get('description')
        objectifs = donnees.get('objectifs')
        addNewProject(nomProjet, description, objectifs)

        nomProjet = getAllProjects(),
        return render_template("home.html", nomProjet=nomProjet)

    else:
        return render_template("alert.html")


@app.route("/projet",methods=['GET'])
def projet(): #accéder au formulaire pour créer un projet
    return render_template("projet.html")

@app.route("/app", methods=['POST'])
def creer(): #créer un projet
        donnees = request.form
        nomProjet= donnees.get('nomProjet')
        description = donnees.get('description')
        objectifs = donnees.get('objectifs')
        addNewProject(nomProjet, description, objectifs)

        nomProjet = getAllProjects(),
        return render_template("home.html",nomProjet = nomProjet)


@app.route("/home",methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/taches",methods=['GET'])
def taches():
    return render_template("taches.html")

@app.route("/projet1")
def projet1():
    return render_template("projet1.html")


if __name__ == '__main__':
    app.run(debug=True)

app.run()