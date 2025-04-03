from menu import MenuBar
from tkinter import *

class Affichage(MenuBar):
    
    def zoomer(self):
        pass
    
    def afficher_barre_etat(self):
        pass
    
    def zoomer_avant(self):
        pass
    
    def zoomer_arriere(self):
        pass
    
    def restaurer_zoom_default(self):
        pass
    
    def __init__(self, menu_bar):
        self.sous_menu_affichage = menu_bar.sous_menu("Affichage")
        
        self.zoom = self.commande(self.sous_menu_affichage, "Zoom", self.zoomer)
        
#        self.zoom_avant = self.commande(self.zoom, "Zoom avant", self.zoomer_avant)
#        self.zoom_arriere = self.commande(self.zoom, "Zoom arrière", self.zoomer_arriere)
#        self.restaurer_zoom = self.commande(self.zoom, "Restaurer zoom par défault", self.restaurer_zoom_default

        self.barre_etat = self.commande(self.sous_menu_affichage, "Barre d'état", self.afficher_barre_etat)