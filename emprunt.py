import datetime

import Livre
from Livre import *
from database import *


class Emprunt:
    d = Database()
    connecter = connect()
    date1 = datetime.datetime.now().date()
    date2 = date1 + datetime.timedelta(days=15)

    def __init__(self, id_livre_emprunt='', id_etudiant_emprunt='', quantite_emprunt=0):
        l = Livre()
        self.id_livre_emprunt = id_livre_emprunt
        self.id_etudiant_emprunt = id_etudiant_emprunt
        self.rendu = 'non'
        self.quantite_emprunt = quantite_emprunt

    def inserer_Emprunt(self):
        conn = Emprunt.connecter
        if self.date2.isoweekday() == 6:
            self.date2 += datetime.timedelta(days=2)
        elif self.date2.isoweekday() == 7:
            self.date2 = self.date2 + datetime.timedelta(days=1)

        if Emprunt.verification_etudiant_rendu_emprunter(16) != '':
            print("VOUS N'AVEZ PAS ENCORE RENDU VOTRE LIVRE")
        else:
            print("ACCES EMPRUNT AUTORISE")
            l = Livre()
            l.diminution_livre(self.id_livre_emprunt, self.quantite_emprunt)
            inserer = (
                "insert into emprunt (id_livre_emprunt, id_etudiant_emprunt, date_fin_emprunt, rendu, quantite_emprunt)"
                "values ('{}', '{}','{}','{}',{})".format(
                    self.id_livre_emprunt, self.id_etudiant_emprunt, self.date2, self.rendu, self.quantite_emprunt
                )
            )
            curs = conn.cursor()
            curs.execute(inserer)
            conn.commit()
            print("emprunt inserer")

    @staticmethod
    def quantite_livre_emprunter(id_e):
        conn = Emprunt.connecter
        selection = (
            'select quantite_emprunt from emprunt where id_emprunt = {}'.format(id_e)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        qt = 0
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                qt = ligne[0]
                break


        else:
            print("pas de livre")
        return qt

    @staticmethod
    def id_livre_emprunter(id_l):
        conn = Emprunt.connecter
        selection = (
            'select id_livre_emprunt from emprunt where id_emprunt = {}'.format(id_l)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        qt = ''
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                qt = ligne[0]
                break


        else:
            print("pas de livre")
        return qt

    @staticmethod
    def modification_rendu_oui(id_e):
        if Emprunt.valeur_rendu_emprunter(id_e) != 'oui':
            conn = Emprunt.connecter
            augmentation_livre(Emprunt.id_livre_emprunter(id_e), Emprunt.quantite_livre_emprunter(id_e))
            modification = (
                "update emprunt set rendu = 'oui' where id_emprunt = {}".format(id_e)
            )
            curs = conn.cursor()
            curs.execute(modification)
            conn.commit()
            print("modification OK")
        else:
            print("livre deja rendu")

    @staticmethod
    def modification_rendu_non(id_e):
        conn = Emprunt.connecter
        modification = (
            "update emprunt set rendu = 'non' where id_emprunt = {}".format(id_e)
        )
        curs = conn.cursor()
        curs.execute(modification)
        conn.commit()
        print("modification OK")

    @staticmethod
    def valeur_rendu_emprunter(id_l):
        conn = Emprunt.connecter
        selection = (
            'select rendu from emprunt where id_emprunt = {}'.format(id_l)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        qt = ''
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                qt = ligne[0]
                break
        else:
            print("non id_emprunt")
        return qt

    @staticmethod
    def selection_tout_rendu_emprunter_oui():
        conn = Emprunt.connecter
        selection = (
            "select * from emprunt where rendu = 'oui'"
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        qt = ''
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                print("id emprunt = {}, id livre emprunter = {}, id de l'étudiant = {}, date debut emprunt = {}, "
                      "date fin emprunt = {}, quantite de livre = {}, rendu = {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))
        else:
            print("non id_emprunt")
        return qt

    @staticmethod
    def selection_tout_emprunt():
        conn = Emprunt.connecter
        selection = (
            "SELECT * FROM emprunt "
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                print("id emprunt = {}, id livre emprunter = {}, id de l'étudiant = {}, date debut emprunt = {}, "
                      "date fin emprunt = {}, quantite de livre = {}, rendu = {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))

        else:
            print("pas d'emprunt")

    @staticmethod
    def verification_etudiant_rendu_emprunter(id_e):
        conn = Emprunt.connecter
        selection = (
            "select id_livre_emprunt from emprunt where id_etudiant_emprunt = {} AND rendu ='non'".format(id_e)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        qt = ''
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                qt = ligne[0]
                break
        else:
            print("non id_emprunt")
        return qt



