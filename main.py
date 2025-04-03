from fenetre import Fenetre
from menu import MenuBar
from fichier import Fichier
from edition import Edition

obj_fenetre = Fenetre()
obj_menu = MenuBar(obj_fenetre.root)
obj_fichier = Fichier(obj_menu)
obj_edition = Edition(obj_menu)

obj_fenetre.afficher()