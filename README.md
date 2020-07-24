Démarage

pip3 install -r requirements.txt
pip3 install Pygments
export FLASK_ENV=development
python3 nomfichier.py


Partie 1 : enregistrer le langage de programmation utilisé

-> python3 sharecode.py

Ajout d'un menu déroulant dans la page d'édition permettant de selectionner le code.



Partie 2 : Changez le procédé de stockage, plus de fichiers mais un SGBDR


-> python3 sharecodedb.py

Création d'un nouveau model : model_sqlite.py
Réécriture de toutes les fonctions pour fonctionner avec sqlite

Réécriture reçues depuis sqlite


Partie 3 : enregistrez les infos sur les utilisateurs qui publient du code

Allez sur http://localhost:5000/admin/

Nouvelle table users
Ajout de functions d'interaction avec la table edition
Ajout du template admin.html


Partie 4 : colorisation de code


Ajout du fichier functions
