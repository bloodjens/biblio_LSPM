from Livre import *

l = Livre()
print("----------LISTE LIVRE-------------")
l.selection_livre()

print("\n\n----------INSERTION LIVRE-------------")
id_livre = input("id livre = ")
nom_livre = input("nom livre = ")
auteur_livre = input("auteur livre = ")
edition_livre = input("édition livre = ")
synopsis_livre = input("synopsis = ")
quantite = int(input("quantite = "))

l2 = Livre(id_livre, nom_livre, auteur_livre, edition_livre, synopsis_livre, quantite)
l2.inserer_livre()

print("----------LISTE LIVRE-------------")
l.selection_livre()

print("-------------RECHERCHE UNE LIVRE AVEC ID-------------")
l.selection_livre_like(input("ID du livre = "))