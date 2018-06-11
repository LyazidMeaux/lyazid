import json
import requests
import os
import xmltodict
import collections

from sdmx import *
from serie import *

root = "./data/"
log = logging.getLogger("SDMX")

if __name__ == '__main__':
    # Gestion des log
    ligne = '%(asctime)s %(levelname)s %(message)s'
    # logging.basicConfig(level=logging.DEBUG,format=ligne)
    log_filename = './log/debug.txt'
    file_handler = logging.FileHandler(log_filename,mode="w")
    format = '%(asctime)s %(levelname)s %(message)s',
    datefmt = '%A %d %b %Y à %I.%M.%S %p'
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)
    root_logger.setLevel(logging.DEBUG)

    fichier = root + "compact.xml"
    fichier = root + "data.xml"
    fichier = root + "query.xml"

    fichier = root + "indice.xml"

    log.debug(convert_xml_to_json(fichier))
    result = convert_xml_to_json(fichier)
    file = open ("indice.json","w")
    file.write(result)
    file.close()

    data = convert_xml_to_dict(fichier)
    show_data_sdmx_ml(data)

    # On ferme le fichier de log
    file_handler.close()

def convert_xml_to_json(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)

def convert_xml_to_dict(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d



# Differents types d'entete
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
        print ("SDMX de type: <{}>".format(entete))
        for key in branche:
            feuille = branche.get(key)
            if (str(key).startswith("@")):
                continue
            print ("Feuille: {}".format(key))

            bloc = str(key)
            if (bloc.lower()=="dataset"):
                dataset = dict(feuille)
                extract_dataset(dataset)


def extract_dataset(dataset):
    """Extrait les series d'un dataset de type MessageGroup
    """
    if type(dataset) is dict or type(dataset) is collections.OrderedDict:
        pass
    else:
        print(dataset)
        # "Type de classe inatendue : " ,type(donnees) )
        return

    dico = dict(dataset)
    uri = dico["@keyFamilyURI"]
    family = dico["KeyFamilyRef"]
    print("Family {}".format(family))

    liste_series = []
    series = dico["Series"]
    dataset_key = dico["Series"][:]
    for item in dataset_key:
        detail = dict(item)
        #afficher_cle_dictionnaire(detail)
        series_key = detail["SeriesKey"] # dict
        attributes = detail["Attributes"] # dict
        obs = detail ["Obs"] # list


        serie = Serie(series_key,attributes,obs)
        if serie.show() is False:
            print(detail)
        liste_series.append(serie)
        print ("Serie: {}".format(serie))

    print("---")
    return liste_series

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

