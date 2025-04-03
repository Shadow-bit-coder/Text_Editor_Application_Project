from menu import MenuBar

class Format(MenuBar):
    def retour_auto_ligne(self):
        pass
        
    def pol(self):
        pass

    def __init__(self, menu_bar):
        self.sous_menu_format = menu_bar.sous_menu("Format")
        
        self.retour_automatique_ligne = self.commande(self.sous_menu_format, "Retour automatique à la ligne", self.retour_auto_ligne)
        self.police = self.commande(self.sous_menu_format, "Police...", self.pol)