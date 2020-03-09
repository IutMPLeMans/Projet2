import numpy as np
#création du plateau
class Plateau:
    def __init__(self,ligne,colonne):
        self.ligne= ligne
        self.colonne= colonne
        self.p = np.zeros((ligne,colonne),np.int32)
 #convertion pour afficher la matrice
    def __repr__(self):
        return np.array_str(self.p)
    #Fonction pour placer les bateaux 
    def placer_bateau(self,lig_ini,col_ini,longueur,direction): # 4 paramètres coordonnées ligne colonne, longueur du bateau et la direction 
        libre = True
        if direction == 0:
            dc = 1
            dl = 0
        else:
            dc = 0
            dl = 1
        #Vérification que le bateau puisse bien être placé dans le plateau 
        if 0 <= lig_ini < self.ligne and 0 <= col_ini < self.colonne and 0 <= lig_ini + (longueur - 1)*dl < self.ligne and 0 <= col_ini + (longueur - 1)*dc < self.colonne:
            for l in range(0,longueur): # vérification que les case ne sont pas déja occupé par un autre bateau
                if self.p[lig_ini + l*dl][col_ini+l*dc] !=0:
                    print("case déjà utilisée par un autre bateau")
                    libre = False
                    return libre
            if libre: 
                for l in range(0,longueur):
                    self.p[lig_ini + l*dl][col_ini+l*dc] = longueur  # Placement du bateau dans le plateau (modification de la valeur dans la matrice)
                return True
        else:
            print("Hors plateau")
            libre = False
            return libre



p=Plateau(10,10)

print(p)


long_bateau=[2, 3, 5] # Chaque valeur correspond à un bateau (valeur = taille)
for i in long_bateau:
    print ("séléctionner les cordonnées la plus à gauche du bateau")
    print("ligne")
    lg_ini = int(input())
    print("colonne")
    col_ini = int(input())
    print ("horizontal = 0 ou vertical = 1 ?")
    direction = int(input())
    ok = p.placer_bateau(lg_ini,col_ini,i,direction) #appel de la fonction placer bateau
    if ok:
        print(p)
    else:
        print ("erreur")


