import numpy as np
#cr�ation du plateau
class Plateau:
    def __init__(self,ligne,colonne):
        self.ligne= ligne
        self.colonne= colonne
        self.p = np.zeros((ligne,colonne),np.int32)
 #convertion pour afficher la matrice
    def __repr__(self):
        return np.array_str(self.p)
p=Plateau(10,10)
print(p)
#Placement bateau PorteAvion
for k in range(5):
    print("placez 1ere coordon�e du PorteAvion (ligne,colonne)")
    x1=int(input())
    y1=int(input())
    print("vous avez choisi la case : ",x1,y1)
    """
    Faire la classe placer_bateau : soit cr�ation case par case ou le bateau directement avec les param�tres x et y (premier point)
    et direction (vertical ou horizontal)
    """
    p.placer_bateau(x1,y1)=5 #chaque type de bateau prend une valeur diff�rente dans la matrice (si plus de 5 touch� coul�)
    print(p)