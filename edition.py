from menu import MenuBar

class Edition(MenuBar):
    def an(self):
            pass
        
    def c(self):
            pass
        
    def co(self):
            pass
        
    def col(self):
        pass
        
    def su(self):
        pass
        
    def rb(self):
        pass
        
    def r(self):
        pass
        
    def rs(self):
        pass
        
    def rp(self):
        pass
        
    def re(self):
        pass
        
    def a(self):
        pass
        
    def s(self):
        pass
        
    def h(self):
        pass    
        
    def __init__(self, menu_bar):
        self.sous_menu_edition = menu_bar.sous_menu("Edition")
        
        self.annuler = self.commande(self.sous_menu_edition, "Annule", self.an)
        self.sous_menu_edition.add_separator()
        self.couper = self.commande(self.sous_menu_edition, "Couper", self.c)
        self.copier = self.commande(self.sous_menu_edition, "Copier", self. co)
        self.coller = self.commande(self.sous_menu_edition, "Coller", self.col)
        self.supprimer = self.commande(self.sous_menu_edition, "Supprimer", self.su)
        
        self.sous_menu_edition.add_separator()
        
        self.recherche_bing = self.commande(self.sous_menu_edition, "Recherche avec Bing...", self.rb)
        self.recherche = self.commande(self.sous_menu_edition, "Recherche...", self. r)
        self.recher_suivant = self.commande(self.sous_menu_edition, "Rechercher le mot suivant", self.rs)
        self.recherche_precedent = self.commande(self.sous_menu_edition, "Recherche précédente", self.rp)
        self.remplace = self.commande(self.sous_menu_edition, "Remplace...", self.re)
        self.atteindre = self.commande(self.sous_menu_edition, "Atteindre...", self.a)
        
        self.sous_menu_edition.add_separator()
        
        self.selectionne_tout = self.commande(self.sous_menu_edition, "Selectionner tout", self.s)
        self.heure_date = self.commande(self.sous_menu_edition, "Heure/date", self.h)