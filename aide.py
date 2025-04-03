from menu import MenuBar

class Aide(MenuBar):
    
    def afficher_aide(self):
        pass
    
    def envoyer_commentaire(self):
        pass
    
    def afficher_propos(self):
        pass
    
    def __init__(self, menu_bar):
        self.sous_menu_aide = menu_bar.sous_menu("Aide")
        
        self.affiche_aide = self.commande(self.sous_menu_aide, "Afficher l'aide", self.afficher_aide)
        self.avoie_commentaire = self.commande(self.sous_menu_aide, "Envoyer des commentaires", self.envoyer_commentaire)
        
        self.sous_menu_aide.add_separator()
        
        self.propos_bloc = self.commande(self.sous_menu_aide,  "A propos du bloc-notes", self.afficher_propos)