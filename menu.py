from tkinter import *

class MenuBar:
     
    def __init__(self, objet_fenetre):
        self.barre_menu = Menu(objet_fenetre)
        objet_fenetre.config(menu=self.barre_menu)
    
    def sous_menu(self, label):
        sous_menu = Menu(self.barre_menu, tearoff=0) 
        self.barre_menu.add_cascade(label=label, menu=sous_menu)
        return sous_menu
        
    def commande(self, sous_menu, nom, fonction):
        sous_menu.add_command(label=nom, command=fonction)