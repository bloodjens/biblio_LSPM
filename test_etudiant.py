from etudiant import *

#insertion étudiant
e2 = Etudiant()
print("---------LISTE ETUDIANT---------")
e2.selection_tout_etudiant()


print("---------INSERTION ETUDIANT---------")
nom = input("nom = ")
prenom = input("prenom = ")
classe = int(input("classe: 1. Terminal L / 2. Terminal S / 3. Première S / 4. Première L"))
classes = ""
if classe == 1:
    classes = "Terminal L"
elif classe == 2:
    classes = "Terminal S"
elif classe == 3:
    classes = "Première S"
elif classe == 4:
    classes = "Première L"

adresse = input("adresse = ")
tel = input("tel = ")

e = Etudiant(nom, prenom, classes, adresse, tel)
e.insertion_etudiant()
