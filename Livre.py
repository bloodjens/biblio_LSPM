from database import *




#fonction qui sert a augmenter la quantité du livre
def augmentation_livre(id_e, qt):
    conn = Livre.connecter

    aug = (
        "update livre set quantite_livre = quantite_livre + {} where id_livre = '{}'".format(qt, id_e)
    )
    curs = conn.cursor()
    curs.execute(aug)
    conn.commit()
    print("modification ok")


class Livre:
    d = Database()
    connecter = connect()

    def __init__(self, id_livre="", nom_livre="", auteur_livre="", edition_livre="", synopsis_livre="",
                 quantite_livre=""):
        self.id_livre = id_livre
        self.nom_livre = nom_livre
        self.auteur_livre = auteur_livre
        self.edition_livre = edition_livre
        self.synopsis_livre = synopsis_livre
        self.quantite_livre = quantite_livre

    def inserer_livre(self):
        conn = Livre.connecter
        if self.verification_id_livre(self.id_livre) == 0:
            inserer = (
                "INSERT INTO livre (id_livre, nom_livre, auteur_livre, edition_livre, synopsis_livre, quantite_livre) "
                "VALUES ('{}','{}','{}','{}','{}','{}')".format(self.id_livre, self.nom_livre, self.auteur_livre,
                                                                self.edition_livre, self.synopsis_livre,
                                                                self.quantite_livre)
            )
            curs = conn.cursor()
            curs.execute(inserer)
            conn.commit()
            print("livre inserer")
        else:
            print("id existe deja")

    @staticmethod
    def selection_livre_unique(id_l):
        conn = Livre.connecter
        selection = (
            "SELECT * FROM livre where id_livre = '{}'".format(id_l)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                print("id livre = {}, nom livre = {}, auteur livre = {}, edition livre = {}, synopsis = {}, quantite "
                      "= {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))

        else:
            print("pas de livre")

    @staticmethod
    def selection_livre_like(id_l):
            conn = Livre.connecter
            selection = (
                "SELECT * FROM livre where id_livre LIKE '%{}%'".format(id_l)
            )
            curs = conn.cursor()
            curs.execute(selection)
            records = curs.fetchall()

            i = 0
            for ligne in records:
                i += 1

            if i > 0:
                for ligne in records:
                    print(
                        "id livre = {}, nom livre = {}, auteur livre = {}, edition livre = {}, synopsis = {}, quantite "
                        "= {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))

            else:
                print("pas de livre")

    @staticmethod
    def verification_id_livre(id_l):
        conn = Livre.connecter
        selection = (
            "SELECT * FROM livre where id_livre = '{}'".format(id_l)
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        for ligne in records:
            i += 1

        return i

    @staticmethod
    def selection_livre():
        conn = Livre.connecter
        selection = (
            "SELECT * FROM livre"
        )
        curs = conn.cursor()
        curs.execute(selection)
        records = curs.fetchall()

        i = 0
        for ligne in records:
            i += 1

        if i > 0:
            for ligne in records:
                print(
                    "id livre = {}, nom livre = {}, auteur livre = {}, edition livre = {}, synopsis = {}, quantite "
                    "= {}".format(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))

        else:
            print("pas de livre")

    # fonction qui sert a diminuer la quantité du livre
    @staticmethod
    def diminution_livre(id_e, qt):
        conn = Livre.connecter

        dimin = (
            "update livre set quantite_livre = quantite_livre - {} where id_livre = '{}'".format(qt, id_e)
        )
        curs = conn.cursor()
        curs.execute(dimin)
        conn.commit()
        print("modification ok")