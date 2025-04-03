from menu import MenuBar
from fenetre import Fenetre

class Fichier(MenuBar):
  
    def creer_note(self):
        pass

    def ouvrir_nouvelle_fenetre(self):
        pass

    def ouvrir_fichier(self):
        pass

    def enregister_fichier(self):
        pass

    def enregistrer_sous(self):
        pass

    def mise_en_page(self):
        pass

    def imprimer(self):
        pass
    
    def quitter(self):
        pass
   
    def __init__(self, menu_bar):
        self.sous_menu_fichier = menu_bar.sous_menu("Fichier")
            
        self.nouveau = self.commande(self.sous_menu_fichier, "Nouveau", self.creer_note)
        self.nouvelle_fenetre = self.commande(self.sous_menu_fichier, "Nouvelle fenêtre", self.ouvrir_nouvelle_fenetre)
        self.ouvrir = self.commande(self.sous_menu_fichier, "Ouvrir...", self.ouvrir_fichier)
        self.enregistrer = self.commande(self.sous_menu_fichier, "Enregistrer", self.enregister_fichier)
        self.enregistrer_sous = self.commande(self.sous_menu_fichier, "Enregistrer sous...", self.enregistrer_sous)
        
        self.sous_menu_fichier.add_separator()
        
        self.mise_page = self.commande(self.sous_menu_fichier, "Mise en page", self.mise_en_page)
        self.imp = self.commande(self.sous_menu_fichier, "Imprimer", self.imprimer)
        
        self.sous_menu_fichier.add_separator()
        
        self.nouvelle_fenetre = self.commande(self.sous_menu_fichier, "Quitter ", self.quitter)