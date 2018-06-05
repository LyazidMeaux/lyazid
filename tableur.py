# -*- coding: utf-8 -*-
from builtins import list, print, enumerate, len
import pandas as pd
from graphe import *


from tableur import *
from fichier import sauvegarde_dictionnaire
import os

caractere_francais = ["é","è","à","ç","â","ê"]

if __name__ == "__main__":
    fable = str() ;
    loup = open("fable.txt","r", encoding='utf-8')

    texte = loup.read()
    lignes = texte.split("\n")
    for ligne in lignes:
        print (ligne.strip() , "-")
        for lettre in ligne:

            if (lettre.lower() >="a" and lettre.lower()<="z"):
                fable += lettre.lower()
            elif (lettre in caractere_francais):
                fable += lettre.lower()
            elif (lettre =="\r"):
                print ("--> <CR>")
            else: fable += " "
        #Saut de ligne
        fable += " "

    lignes = fable.split(" ")
    fable = ""
    for ligne in lignes:
        if len(ligne.strip()) ==0: continue
        for lettre in ligne:
            if (lettre.lower() >="a" and lettre.lower()<="z" or (lettre in caractere_francais)):
               fable += lettre.lower()

        fable += " "
    print(fable)
    agrege_mot (fable.split(" "))

def agrege_mot (mots):
    ensemble = dict ()
    for mot in mots:
        if len(mot.strip())<=1: continue
        value = ensemble.get(mot)
        if value is not None :
           value +=1
        else : value =1
        ensemble[mot] = value


    serie = pd.Series(ensemble,ensemble)
    print(serie)
    print(sum(serie))
    sauvegarde_dictionnaire(serie)

    rest = serie.apply(lambda x: x if x> 100 else None)
    print(rest.dropna())


def test():
    print("Salut tout le monde")
    version_pandas = pd.__version__
    print("Version de pandas: {}".format(version_pandas))

    villes = pd.Series(['Paris', 'Lyon', 'Marseille'])
    population = pd.Series([2852469, 101785, 185199])
    population = population / 1000.
    feuille = pd.DataFrame({'Ville': villes, 'Population': population / 1000})
    print(villes)
    print(population)
    print(feuille)

    print("----\n")
    print(feuille['Ville'][0:2])

    feuille['Superficie'] = pd.Series([346.87, 176.53, 197.92])
    feuille['Densite'] = feuille['Population'] / feuille['Superficie']
    # affiche(feuille)

    # dessine()

    exercice_series()


def exercice_series ():
    mots = ['bonjour','monsieur']
    serie = pd.Series(mots)

    quantite =  [5,9]
    dictionnaire = pd.Series(quantite,index=mots)
    print (dictionnaire)

    mots_1 = ['suite','fin']
    ss = pd.Series(mots + mots_1)
    print ("Serie SS")
    print (ss)








