#Exercice 1: nombre mystérieux - Résolution
import random

n = random.randint(1,100)
appreciation = "neutre"

while True:
    var = int(input("Entrez un nombre : "))
    if var < n :
        appreciation = "Trop petit"
        print(var, appreciation)

    else :
        appreciation = "Trop grand"
        print(var, appreciation)
        
    if var == n:
        appreciation = "Bravo !"
        print(var, appreciation)
        break
        

        
        
#Exercice 2: Fonction purge ! - - Résolution
def purge(a, chars):
    if len(a)==1:
        return "" if a in chars else a
    return purge(a[0:int(len(a)/2)], chars) +  purge(a[int(len(a)/2):len(a)], chars)