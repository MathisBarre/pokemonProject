# Python basic cheatsheet 1


# Basic printing
print("Hello World")       # Affiche une chaine de caractère
print(4)                   # Affiche un nombre
print("hi ", end = "")     # Affiche "hi"
print("planet")            # Affiche "planet" sur la même ligne que "hi"


# Basic loop
for loop in range(5):
    print(loop)            #Affiche 0,1,2,3,4 (sur différentes lignes)


# Basic calculation
print(10 + 5)              # Affiche 15    (addition)
print(10 * 5)              # Affiche 50    (multiplication)
print(10 / 5)              # Affiche 2.0   (division)
print(10 % 5)              # Affiche 0     (modulo = reste)
print((10 + 5) / 2 * 4)    # Affiche 30.0


# Basic variable & variable printing
iAmAVariable = 5
meeToo = "Nombre de pions"
print(iAmAVariable)                # Affiche 5
print(meeToo, ":", iAmAVariable)   # Nombre de pions : 5


# Read input
variable = input()                   # Demande un input et met le résultat dans la variable
number = int(input())                # Demande un input et met le résultat converti en entier dans la variable


# Printing options
print("007", "P99" , sep = "-")      # Change le séparateur initial (un espace) par la valeur que vous souhaitez


# Conditions
if number > 10:                      # si la variable number est plus grande que 10, faire #stuff...
    #stuff...

if number < 10:                      # si la variable number est plus petite que 10
if number >= 10:                     # si la variable number est plus grande ou égale à 10
if number <= 10:                     # si la variable number est plus petite ou égale à 10
if number == 10:                     # si la variable number est égale à 10
    
if number > 10:                      # si la variable number est plus grande que 10, faire #stuff...
    #stuff... 
else :                               # sinon faire # other stuff...
    #other stuff...

if (age <= 25) and (age >= 12):      # les deux conditions doivent être rempli
if (age <= 25) or (age >= 12):       # une des deux conditions doit être rempli

pastropjeune = (age >= 12)           # on peut mettre des conditions dans des variables...
pastropvieux = (age <= 25)           # on peut mettre des conditions dans des variables...

if pastropjeune and pastropvieux:    # ...pour les réutiliser par la suite

if not tropjeune or not tropvieux:   # mot-clé not pour inverser le résultat de la condition, ici cela revient au même que la ligne au dessus


# Conditioned loop
while true:       #tant que la condition est vrai, boucler sur #stuff... (ici boucle infinie)
    #stuff...
