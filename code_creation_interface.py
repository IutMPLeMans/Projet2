import numpy as np
import wx
import os
import Bataille_navale as bn

ID_BOUTON = 10000

class MaFenetre(wx.Frame):    
    def __init__(self, ligne, colonne):
        chemin_script = os.path.dirname(os.path.realpath(__file__))
        super().__init__(parent=None, title='Ma fenêtre avec BitmapButton')
        self.bmp1 = wx.Bitmap("H:\deuxièmeAnnee\S4\POO\TP\Orange.png", wx.BITMAP_TYPE_PNG) 
        self.bmp2 = wx.Bitmap("H:\deuxièmeAnnee\S4\POO\TP\Rouge.png", wx.BITMAP_TYPE_PNG) 
        self.plateau = bn.Plateau(ligne,colonne)
        nb_boutons = ligne*colonne
        self.liste_boutons = []
        #Création du menu
        barre_menu = wx.MenuBar()
        menu_fichier = wx.Menu()
        article_porteavion = menu_fichier.Append(1000, 'Porte-Avion')
        article_sousmarin1 = menu_fichier.Append(1001, 'Premier Sous Marin')
        article_sousmarin2 = menu_fichier.Append(1002, 'Deuxième Sous Marin')
        article_torpilleur = menu_fichier.Append(1003, 'Torpilleur')
        article_croiseur = menu_fichier.Append(1004, 'Croiseur')
        barre_menu.Append(menu_fichier, '&Fichier')
        self.SetMenuBar(barre_menu)
        self.Bind(wx.EVT_MENU, self.Onporteavion, article_porteavion)
        self.Bind(wx.EVT_MENU, self.Onsousmarin1, article_sousmarin1)
        self.Bind(wx.EVT_MENU, self.Onsousmarin2, article_sousmarin2)
        self.Bind(wx.EVT_MENU, self.Ontorpilleur, article_torpilleur)
        self.Bind(wx.EVT_MENU, self.Oncroiseur, article_croiseur)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        self.ma_grille = wx.GridSizer(rows=ligne, cols=colonne, vgap=10, hgap=10)
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD)
        self.etat_bouton = None
        #Création de la grille
        for i in range(nb_boutons):
            bouton = wx.BitmapButton(self, id=ID_BOUTON+i, bitmap=self.bmp1)
            self.liste_boutons.append(bouton)
            bouton.SetFont(font)
            bouton.Bind(wx.EVT_BUTTON, self.OnBouton)            
            self.ma_grille.Add(bouton, i,wx.EXPAND)
            if self.etat_bouton == None:
                self.etat_bouton={i: False}
            else:
                self.etat_bouton[i] = False
        self.SetSizerAndFit(self.ma_grille)   
        self.Show()

    def OnBouton(self, event):
        if event.GetId() in self.etat_bouton:
            bouton = event.GetEventObject()
            if not self.etat_bouton[event.GetId()]:
                self.etat_bouton[event.GetId()] = True
                bouton.SetBitmapLabel(self.bmp2)
            else:
                self.etat_bouton[event.GetId()] = False
                bouton.SetBitmapLabel(self.bmp1)

    def OnPaint(self, event): 
       for i in range(len(self.liste_boutons)):
           lig = i  // self.plateau.p.shape[1] #Appelles de fonction à simplifier
           col = i % self.plateau.p.shape[1]
           if self.plateau.p[lig][col] != 0:
                self.liste_boutons[i].SetBitmapLabel(self.bmp2)
           else:
                self.liste_boutons[i].SetBitmapLabel(self.bmp1)

    def OnQuit(self, e):
        print('Article : ',e.GetId() )
        print("Je quitte") 
        self.Close()
        
    def Onporteavion(self, event):
        s = wx.TextEntryDialog(self,'Ligne','Entrez la ligne la plus en haut du Porte-Avion',value='0')
        s.ShowModal()
        lig = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Colonne','Entrez la colonne la plus à gauche du Porte-Avion',value='0')
        s.ShowModal()
        col = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Direction','0 = Horizontal  1 = Vertical',value='0')
        s.ShowModal()
        direction = int(s.GetValue())
        if self.plateau.placer_bateau(lig,col,5,direction):
            event.GetEventObject().Enable(event.GetId(), False)
        self.Refresh(True)
        
    def Onsousmarin1(self, event):
        s = wx.TextEntryDialog(self,'Ligne','Entrez la ligne la plus en haut du Sous-Marin',value='0')
        s.ShowModal()
        lig = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Colonne','Entrez la colonne la plus à gauche du Sous-Marin',value='0')
        s.ShowModal()
        col = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Direction','0 =  Horizontal   1 = Vertical',value='0')
        s.ShowModal()
        direction = int(s.GetValue())
       
        if self.plateau.placer_bateau(lig,col,3,direction):
            event.GetEventObject().Enable(event.GetId(), False)
        self.Refresh(True)

    def Onsousmarin2(self, event):
        s = wx.TextEntryDialog(self,'Ligne','Entrez la ligne la plus en haut du Sous-Marin',value='0')
        s.ShowModal()
        lig = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Colonne','Entrez la colonne la plus à gauche du Sous-Marin',value='0')
        s.ShowModal()
        col = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Direction','0 =  Horizontal   1 = Vertical',value='0')
        s.ShowModal()
        direction = int(s.GetValue())
       
        if self.plateau.placer_bateau(lig,col,3,direction):
            event.GetEventObject().Enable(event.GetId(), False)
        self.Refresh(True)

    def Ontorpilleur(self, event):
        s = wx.TextEntryDialog(self,'Ligne','Entrez la ligne la plus en haut du Torpilleur',value='0')
        s.ShowModal()
        lig = int(s.GetValue())
        
        s = wx.TextEntryDialog(self,'Colonne','Entrez la colonne la plus à gauche du torpilleur',value='0')
        s.ShowModal()
        col = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Direction','0 =  Horizontal   1 = Vertical',value='0')
        s.ShowModal()
        direction = int(s.GetValue())
        if self.plateau.placer_bateau(lig,col,2,direction):
            event.GetEventObject().Enable(event.GetId(), False)
        self.Refresh(True)

    def Oncroiseur(self, event):
        s = wx.TextEntryDialog(self,'Ligne','Entrez la ligne la plus en haut du croiseur',value='0')
        s.ShowModal()
        lig = int(s.GetValue())
        
        s = wx.TextEntryDialog(self,'Colonne','Entrez la colonne la plus à gauche du croiseur',value='0')
        s.ShowModal()
        col = int(s.GetValue())

        s = wx.TextEntryDialog(self,'Direction','0 =  Horizontal   1 = Vertical',value='0')
        s.ShowModal()
        direction = int(s.GetValue())
        if self.plateau.placer_bateau(lig,col,4,direction):
            event.GetEventObject().Enable(event.GetId(), False)
        self.Refresh(True)

if __name__ == '__main__':
    app = wx.App()
    frame = MaFenetre(10,10)
    app.MainLoop()
