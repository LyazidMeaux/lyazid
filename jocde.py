import json
import requests
import os
import xmltodict
import collections


from scipy.constants import value
from scipy.optimize import root
from tensorflow.python.eager.backprop import val_and_grad_function

from jocde import *


from xml.sax.saxutils import prepare_input_source

root = "./data/"
if __name__ == '__main__':
    fichier = root + "compact.xml"
    fichier = root + "data.xml"
    fichier = root + "query.xml"
    fichier = root + "indice.xml"

    data = convert_xml_to_dict(fichier)
    show_data_sdmx_ml(data)


    #print (convert_xml_to_json(fichier))

def convert_xml_to_string(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d

def convert_xml_to_json(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)

def convert_xml_to_dict(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d




def show_fichier (filename):
    print("Exemple JSON")
    with open("./data/ocde.json", "r") as fichier_json:
        data = fichier_json.read()
    #show__data_sdmx_json(data)

# Different type d'entete
entete_xml = ["message:MessageGroup","message:CompactData","message:QueryMessage"]

def show_data_sdmx_ml(data):
    """Analyse un dictionnaire normé SDMX
    doc['mydocument']['@has'] # == u'an attribute'
    doc['mydocument']['and']['many'] # == [u'elements', u'more elements']
    doc['mydocument']['plus']['@a'] # == u'complex'
    doc['mydocument']['plus']['#text'] # == u'element as well'
    """
    valeurs = dict(data)

    #print (valeurs)
    #afficher_dictionnaire(valeurs,"Fichier")

    print ("---")
    for entete in entete_xml:
        # On recupere le ROOT
        branche = valeurs.get(entete)
        if (branche is None):
            continue
        # ou ceil = valeurs[entete]
        #afficher_dictionnaire(branche,entete)

        for key in branche:
            feuille = branche.get(key)
            if (str(key).startswith("@")):continue
            print ("Feuille: {}".format(key))

            bloc = str(key)
            if (bloc.lower()=="dataset"):
                dataset = dict(feuille)
                afficher_dictionnaire(dataset,"dataset")
            #afficher_dictionnaire(feuille, str(key))

        #header = branche.get("Header")
        #dataset = branche.get("DataSet")
        #structure = valeurs.get("structure")

        #afficher_dictionnaire(header, "header")
        #afficher_dictionnaire(dataset, "Dataset")

        #afficher_dictionnaire(structure,"structure")


def show__data_sdmx_json(data):

    valeurs =  dict(json.loads(data))

    print (valeurs)
    header = valeurs.get("header")
    datasets = valeurs.get("dataSets")
    structure = valeurs.get("structure")

    afficher_dictionnaire(valeurs)
    #afficher_dictionnaire(header,"header")
    #afficher_dictionnaire(datasets,"datasets")
    #afficher_dictionnaire(structure,"structure")


def afficher_dictionnaire(donnees,variable):
    if type(donnees) is dict or type(donnees) is collections.OrderedDict:
        pass
    elif  type(donnees) is list:
        afficher_list(donnees,variable)
        return
    else :
        print (donnees)
        # "Type de classe inatendue : " ,type(donnees) )
        return

    dico = dict(donnees)
    print (variable, ":")
    for key, value in dico.items():
        if type(value) is dict or type (value) is collections.OrderedDict :
            afficher_dictionnaire(value,variable +"_" + key)

        elif type(value) is list:
            afficher_list(value, variable)
            
        else:
            print("{} --> {}".format(key, value))

    print("---")

def afficher_list(donnees,variable):
    if type(donnees) is dict or type(donnees) is collections.OrderedDict:
        afficher_dictionnaire(donnees,variable)
        return
    elif  type(donnees) is list:
        pass
    else :
        print (donnees) #"Type de classe inatendue : " ,type(donnees) )
        return

    dico = list(donnees)

    x=0
    for value in dico:
        if type(value) is dict or type (value) is collections.OrderedDict:
            afficher_dictionnaire(value,variable)
        elif type(value) is list:
            afficher_list(value,variable)
        else :
            x+= 1
            print("{} --> {}".format(x, value))

def afficher_cle_dictionnaire(donnees):
    try:
        dico = dict(donnees)
    except ValueError:
        print ("class <class 'str'> attendue. Recu : " ,type(donnees) )
        return
    except TypeError:
        print("Aucunne clee trouvee.")
        return

    for key in dico:
        print("Cle trouvee: {}".format(key))

def exemple_variable():
    print ("Analyse Fichier")
    presidents = {"nom":"Mitterand" ,
                 "prenom":"Francois",
                "date": {"debut":2000,"fin":2008}
                }

    with open("./data/president.json","w" ) as json_file:
        json.dump(presidents,json_file)

    serialiser = json.dumps(presidents,indent=4)
    print (serialiser)
    deserialiser =  json.loads(serialiser)
    print (deserialiser)

def exemple_web():
    print ("Exemple JSON")
    reponse = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(reponse.text)
    for line in todos:
        dico = dict(line)
        print ("User: {} Id: {} Status: {} ".format(dico.get("userId"),dico.get("id"),dico.get("completed") ))

# Fonction utiles :
        # for key in dico.keys():
        #   print ("{} --> {}".format(key,dico.get(key)))

        # for key,value in dico.items():
        #   print ("{} --> {}".format(key,value))

        # top_users = sorted(dico.items(), key=lambda x: x[1], reverse=True)


