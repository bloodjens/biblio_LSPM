from database import *


class Etudiant:
    d = Database()
    connecter = connect()

    def __init__(self, nom_etudiant="", prenom_etudiant="", classe_etudiant="", adresse_etudiant="", tel_etudiant=""):
        self.nom_etudiant = nom_etudiant
        self.prenom_etudiant = prenom_etudiant
        self.classe_etudiant = classe_etudiant
        self.adresse_etudiant = adresse_etudiant
        self.tel_etudiant = tel_etudiant

    def insertion_etudiant(self):
        conn = Etudiant.connecter
        inserer = (
                "INSERT INTO etudiant (nom_etudiant, prenom_etudiant, classe_etudiant, adresse_etudiant, "
                "tel_etudiant) VALUES ('" + self.nom_etudiant + "','" + self.prenom_etudiant + "',"
                                                                                               "'" +
                self.classe_etudiant + "','" + self.adresse_etudiant + "','" + self.tel_etudiant + "')")

        curs = conn.cursor()
        curs.execute(inserer)
        conn.commit()
        print("etudiant inserer")

    @staticmethod
    def selection_nom_etudiant(id_e):
        conn = Etudiant.connecter
        selection = (
            "select nom_etudiant from etudiant where id_etudiant = {}".format(id_e)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()
        i = 0

        for ligne in records:
            i += 1
        if i > 0:
            for ligne in records:
                print(ligne[0])
        else:
            print("resultat vide")

    @staticmethod
    def selection_prenom_etudiant(id_e):
        conn = Etudiant.connecter
        selection = (
            "select prenom_etudiant from etudiant where id_etudiant = {}".format(id_e)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()
        i = 0

        for ligne in records:
            i += 1
        if i > 0:
            for ligne in records:
                print(ligne[0])
        else:
            print("resultat vide")

    @staticmethod
    def selection_classe_etudiant(id_e):
        conn = Etudiant.connecter
        selection = (
            "select classe_etudiant from etudiant where id_etudiant = {}".format(id_e)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()
        i = 0

        for ligne in records:
            i += 1
        if i > 0:
            for ligne in records:
                print(ligne[0])
        else:
            print("resultat vide")

    @staticmethod
    def selection_etudiant(id_e):
        conn = Etudiant.connecter
        selection = (
            "select * from etudiant where id_etudiant = {}".format(id_e)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()
        i = 0

        for ligne in records:
            i += 1
        if i > 0:
            for ligne in records:
                print("id = {}, nom = {}, prenom = {}, classe = {}, adresse = {}, tel = {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))
        else:
            print("resultat vide")

    @staticmethod
    def selection_tout_etudiant():
        conn = Etudiant.connecter
        selection = (
            "select * from etudiant"
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()
        i = 0

        for ligne in records:
            i += 1
        if i > 0:
            for ligne in records:
                print("id = {}, nom = {}, prenom = {}, classe = {}, adresse = {}, tel = {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))
        else:
            print("resultat vide")