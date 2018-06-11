# -*- coding: utf-8 -*-
import collections
import logging

log = logging.getLogger('serie')


class Serie:
    def __init__(self, serie, attributs, _valeur):
        log.setLevel(logging.INFO)
        self.serie = dict(serie)
        self.attibuts = dict(attributs)
        if type(_valeur) is collections.OrderedDict:
            self.valeur = dict(_valeur)
        elif type(_valeur) == list:
            self.valeur = list(_valeur)
        else:
            print("****** ERREUR de struture sur le type {} *******".format(type(_valeur)))

        self.qualification = {}
        self.points = collections.OrderedDict()


    def show(self):
        # On extrait tutes les données de la serie_key
        liste = self.serie["Value"]
        # print(liste)

        for item in liste:
            detail = dict(item)
            # print (detail)
            self.qualification[detail.get("@concept")] = detail.get("@value")

        log.debug(self.qualification)

        # On extrait tutes les données de la serie_attribut
        liste = self.attibuts["Value"]
        # print(liste)

        for item in liste:
            detail = dict(item)
            # print (detail)
            self.qualification[detail.get("@concept")] = detail.get("@value")
        log.info(self.qualification)

        # On extrait tutes les données de la serie_obsc
        # Celle ci peut etre une list ou un dict

        if type(self.valeur) is list:
            for items in self.valeur:
                periode = items["Time"]
                axe = items["ObsValue"]["@value"]
                self.points[periode] = axe
                log.debug(" Soit {} en {}".format(axe, periode))
        elif type(self.valeur) is dict:
            # Dans le cas d'un dictionnaire , on ne recupere qu'un tuplet (donc 1 valeur)
            #for items in self.valeur:
            periode = self.valeur['Time']
            axe = self.valeur["ObsValue"]["@value"]
            self.points[periode] = axe
            log.debug("Soit {} en {}".format(axe, periode))
        else :
            print("*******\nERROR\n********")
            print(self.qualification)
            print(type(self.valeur), self.valeur)
            print("*******")
            return False

        return True

    def __str__(self):
        return self.qualification.__str__()