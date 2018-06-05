"""Lecture des fichiers en python
Le but etant de faire comme en java mais synthetique
"""

import os
import pickle
from builtins import print


niveau_exception = 1
repertoire_courant = os.getcwd()

def test():
    print(repertoire_courant)

    nom_du_fichier = "c:/R/pycharm/pendu/data"
    fichier_a_ecrire = open(nom_du_fichier + ".txt","w")
    fichier_a_ecrire.write("Bonjour\n")
    fichier_a_ecrire.newlines
    fichier_a_ecrire.writelines("Premiere Ligne")
    fichier_a_ecrire.write(",Seconde ligne\n")
    fichier_a_ecrire.write("Troisieme ligne")

    fichier_a_ecrire.close()

    fichier_a_lire = open (nom_du_fichier +".txt" ,"r")
    tampon = fichier_a_lire.read()
    lignes = tampon.split("\n")
    print (lignes)
    position = 1
    for ligne in lignes:
        print (position, ":", ligne)
        position += 1

    fichier_a_lire.close()


def sauvegarde_dictionnaire(dico):
    """Sauvegarde le dictionnaire contenant la repartition des mot de la langue
    """
    nom_du_fichier="dictionnaire"
    liste_0= [1,2,3,4]
    liste_1= [5,6,7,8]
    liste_2= [9,10,11,12]
    with open (nom_du_fichier + ".obj", "wb") as fichier_binaire:
        conserve  = pickle.Pickler (fichier_binaire)
        conserve.dump(dico)
        conserve.dump(liste_0)
        conserve.dump(liste_1)
        conserve.dump(liste_2)

import traceback
def lecture_dictionnaire():
    """Renvoi le dictionnaire pour une analyse de la repartition des mots
    """

    with open (nom_du_fichier + ".obj","rb") as fichier_binaire:
        try:
            conserve = pickle.Unpickler(fichier_binaire)
            dico = conserve.load()
            retour_1 = conserve.load()
            retour_2 = conserve.load()
            retour_3 = conserve.load()

        except Exception as e:
            if (niveau_exception==1):
                print("Erreur de type: " + str(e))
            else :
                print(traceback.format_exc())
                print("Erreur de type: {}".format(e))

    print(retour_1)
    print(retour_2)
    print(retour_3)
