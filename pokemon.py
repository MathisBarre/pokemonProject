import time

class Pokemon:
    def __init__(self, name, maxHealth, health, attacks):
        self.name = name
        self.maxhealth = maxHealth
        self.health = health
        self.attacks = attacks

    def stopFight(self, target):
        # Initialisation du combat
        # Demande si le pokemon adverse veut faire le combat
        speedPrint("{0.name} a invoqué un duel contre {1.name}".format(self, target))
        speedPrint("{0.name} acceptes-tu ce duel ? Si oui, écris \"oui\"".format(target))
        # Attend la réponde
        response = input()
        # Toute réponse différentes de oui...
        if (response != "oui"):
            # ... Arrête le combat
            speedPrint("Le combat s'arrête ici")
            return True # Sort de la méthode (fonction dans un objet) et renvoie True

        # Sinon lance le combat !
        speedPrint("{0.name} accepte le combat ! Il commence donc par attaquer !".format(target))

    def startFightWith(self, target):
        # On définit un attaquant (celui qui à accepté le combat) et le défenseur (l'autre du coup)
        attacker = target
        defender = self

        # Début du combat tant, que nous sommes dans la boucle, le combat continu
        while True:
            # On demande l'attaque à utiliser
            speedPrint("{0.name}, quelle attaque veux-tu utiliser ? {1.name} a {1.health}pv".format(attacker, defender))
            time.sleep(1.5) # On attend 1.5s

            # Boucle infinie (on en sort grâce à break)
            # Elle permet de rechoisir l'attaque à utiliser si la valeur entré est incorrect
            while True:
                # Simple boucle afin d'afficher toutes les attaques disponible
                for nameAttack,valueAttack in attacker.attacks.items():
                    print("- {} : {} points de dégats ({} utilisation restante)".format(nameAttack, valueAttack["power"], valueAttack["usesRemaining"]))  # Affiche toutes les attaques disponibles
                # On attend la valeur entré par l'utilisateur (ex: Charge)
                attackUsued = input()

                # L'instruction try permet de stopper le programme si il y a une erreur (dans ce cas c'est ecept qui prend le relais)
                try:
                    # Si il n'y a plus d'utilisation restante sur une attaque, on redemande une attaque (en faisant continuer la boucle)
                    if (attacker.attacks[attackUsued]["usesRemaining"] <= 0):
                        speedPrint("Vous ne pouvez plus utiliser cette attaque")
                    # Sinon, càd si il n'y a pas d'erreurs et qu'il y a une utilisation resante, on sort de la boucle pour passer au reste
                    else :
                        break # break permet de sortir de la boucle
                # Si il y a une erreur, on l'affiche et on redemande une attaque à utiliser (en ne faisant pas stopper la boucle)
                except KeyError:
                    speedPrint("KEY ERROR : Veuillez choisir une attaque")
            # On annonce l'attaque
            speedPrint("{0.name} fait une attaque {1} sur {2.name}".format(attacker, attackUsued, defender))
            # Enlève de la vie au défenseur
            defender.health -= attacker.attacks[attackUsued]["power"]  
            # Enlève une utilisation restante à l'attaque
            attacker.attacks[attackUsued]["usesRemaining"] -= 1  
            # On attend 1.5s      
            time.sleep(1.5)
            # Si le défenseur est mort...
            if( defender.health <= 0 ):  
                # ...on l'annonce
                speedPrint("{} a perdu le combat, {} a gagné".format(defender.name, attacker.name))
                # Et on sort de la boucle principale, ce qui fait arrêter le combat
                break
            # Mais si il n'est pas mort, 
            speedPrint("{} a perdu {}pv, il lui reste {}pv".format(defender.name, attacker.attacks[attackUsued]["power"], defender.health)) 
            # ZZzZZzZZzZzzZ
            time.sleep(1.5)

            # Changement d'attaquant et de défenseur
            defender, attacker = attacker, defender

            # Puis la boucle retourne au début mais on a changé l'attaquant et le défenseur 

    def askForFightWith(self, target):
        
        if (self.stopFight(target)):
            return

        self.startFightWith(target)

# Permet de simuler l'ecriture de qlq
def speedPrint(string):
    for letter in string:
        print(letter, end="")
        time.sleep(0.02)
    print("")

        
# Création des pokémons
                 # nom      #maxPV #PV
rattata = Pokemon("Rattata", 100, 100, 
# Disctionnaire (liste) de toutes les attaques
{
    # Chaque attaque est elle même un dictionnaire avec le nombre...
    # ...de pv qu'il inflige et le nombre d'utilisation restante
    "Tacle": {
        "power": 35,
        "usesRemaining": 1,
        "accuracy": .95
    },
    "Queue de fer": {
        "power": 30,
        "usesRemaining": 1
    },
    "Attaque rapide": {
        "power": 40,
        "usesRemaining": 1
    },
})

roucool = Pokemon("Roucool", 100, 100, {
    "Charge": {
        "power": 35,
        "usesRemaining": 2
    },
    "Jet de sable": {
        "power": 15,
        "usesRemaining": 3
    },
    "Tornade": {
        "power": 35,
        "usesRemaining": 3
    }
})

# Roucool lance le combat contre Rattata (l'inverse est aussi possible)
roucool.askForFightWith(rattata)