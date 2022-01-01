class Rectangle:
    def __init__(self,larg,long) :
        self.larg=larg
        self.long=long
        self.nom="rectangle"
    def affiche(self):
        print("longeur et largeur de ce %s:"% (self.nom))  
        print(self.larg,self.long)
    def surface(self):
        return self.long*self.larg


R1=Rectangle(2,3)
R1.affiche()
#surf=Rectangle()
R1.surface()
