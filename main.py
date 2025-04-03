from fenetre import Fenetre
from menu import MenuBar
from fichier import Fichier
from edition import Edition
from format import Format
from affichage import Affichage
from aide import Aide

obj_fenetre = Fenetre()
obj_menu = MenuBar(obj_fenetre.root)
obj_fichier = Fichier(obj_menu)
obj_edition = Edition(obj_menu)
obj_format = Format(obj_menu)
obj_affichage = Affichage(obj_menu)
obj_aide = Aide(obj_menu)

obj_fenetre.afficher()