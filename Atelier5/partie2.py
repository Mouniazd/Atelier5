
class etudiant:
    def __init__(self,nom,prenom,cne,age,moyenne) :
       self.nom=nom
       self.cne=cne
       self.prenom=prenom
       self.age=age
       self.moyenne=moyenne

    def __repr__(self):
       return '{' + self.nom + ', ' + self.cne + ', '+ self.prenom + ', ' + str(self.age) + ', ' + str(self.moyenne) +'}'
     

listEtudiant=[etudiant('salma','benani','K23456',39,12.5),
etudiant('hassan','benani','K23456',19,13),
etudiant('sara','benani','K23456',29,17.5)]

print("____trie liste par age :____")      
listEtudiant.sort(key=lambda X: X.age)
print(listEtudiant)

print("____trie liste par moyenne :____")      
listEtudiant.sort(key=lambda X: X.moyenne)
print(listEtudiant)

    
 