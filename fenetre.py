from tkinter import * 

class Fenetre:
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x450+200+100")
        self.root.title("Blog note")
        
        self.zone = Text(self.root, font=("Arial", 12))
        self.zone.pack(side=LEFT, expand=True, fill=BOTH) 
        
        self.scrollbarre = Scrollbar(self.root, command=self.zone.yview)   
        self.scrollbarre.pack(side=RIGHT, fill=Y)
        self.zone.configure(yscrollcommand=self.scrollbarre.set)  
    
    def afficher(self):
        self.root.mainloop()