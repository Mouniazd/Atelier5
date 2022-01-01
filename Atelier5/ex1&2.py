
class vecteur2D:
    
    def __init__(self, x=0,y=0) :
        self.x=x
        self.y=y
    
 
    def show(self):
        print("les cordonnes du vecteur :")
        print(self.x,self.y)
    def addition(self,V1,V2):
        self.x=V2.x+V1.x
        self.y=V2.y+V1.y
        print(self.x,self.y)


vect1=vecteur2D(4,6)
vect2=vecteur2D(5,-2)
vect1.show()
vect2.show()
res=vecteur2D()
print("l'addition des deux vecteurs est: ")
res.addition(vect1,vect2)






