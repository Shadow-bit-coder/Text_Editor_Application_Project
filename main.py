from fenetre import Fenetre
from menu import MenuBar
from fichier import Fichier

obj_fenetre = Fenetre()
obj_menu = MenuBar(obj_fenetre.root)
obj_fichier = Fichier(obj_fenetre)

obj_fenetre.afficher()