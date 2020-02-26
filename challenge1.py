for loop in range(100):   # Loop for. Synthaxe simple et à l'avantage de créer une variable (ici loop) utilisable dans le projet
    if(loop % 2 == 0):    # On vérifie si la variable loop (qui prend toutes le valeurs de 0 à 100) à comme reste 0
        print(loop)       # Si c'est vérifié, un affiche le nombre présent dans la variable loop


# Challenge #1.1
print("Quelle table de multiplication souhaitez-vous afficher ?")
table = int(input())
for loop in range(11):
    print("{} * {} = {}".format( loop, table, table*loop ) )