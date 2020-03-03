import numpy as np
import wx
import os

class MaFenetre(wx.Frame):    
    def __init__(self, ligne, colonne):
        chemin_script = os.path.dirname(os.path.realpath(__file__))
        super().__init__(parent=None, title='Ma fenêtre avec BitmapButton')
        self.bmp1 = wx.Bitmap("H:\semestre4\POO\PROJET\\Orange.png", wx.BITMAP_TYPE_PNG) 
        self.bmp2 = wx.Bitmap("H:\semestre4\POO\PROJET\\Rouge.png", wx.BITMAP_TYPE_PNG) 
        self.ligne= ligne
        self.colonne= colonne
        self.plateau = np.zeros((ligne,colonne),np.int32)
        nb_boutons = self.plateau.shape[0]*self.plateau.shape[1]
        self.ma_grille = wx.GridSizer(rows=ligne, cols=colonne, vgap=0, hgap=0)
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD)
        self.etat_bouton = None
        for i in range(nb_boutons):
            bouton = wx.BitmapButton(self, id=i, bitmap=self.bmp1)
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

       
if __name__ == '__main__':
    app = wx.App()
    frame = MaFenetre(5,5)
    app.MainLoop()
