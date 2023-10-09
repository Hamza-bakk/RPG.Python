import random


class Character:
    def __init__(self, name, hp, dmg, mana):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.dmg = dmg
        self.mana = mana
        self.status = "playing"

    def takeDamage(self, damage):
        if self.status != "loser":
            self.hp -= damage
            if self.hp <= 0:
                self.status = "loser"

    def dealDamage(self, target):
        if self.status != "loser":
            target.takeDamage(self.dmg)


class Fighter(Character):
    def __init__(self, name):
        super().__init__(name, hp=12, dmg=4, mana=40)

    def specialAttack(self, target=None): #Cela signifie que le Fighter peut choisir 
                                          #de spécifier une cible ou non lorsqu'il utilise son attaque spéciale.
        if self.status != "loser" and self.mana >= 20:
            if target is not None:
                target.takeDamage(5)
            self.mana -= 20
            self.dmg_reduction = 2


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, hp=16, dmg=3, mana=160)

    def specialAttack(self, target):
        if self.status != "loser" and self.mana >= 40:
            target.takeDamage(4)
            self.hp += 5  # Healing
            self.mana -= 40


class Monk(Character):
    def __init__(self, name):
        super().__init__(name, hp=8, dmg=2, mana=200)

    def specialAttack(self, target=None):
        if self.status != "loser" and self.mana >= 25:
            if target is None:
                self.hp += 8  
            else:
                target.takeDamage(8)  
            self.mana -= 25


class Berzerker(Character):
    def __init__(self, name):
        super().__init__(name, hp=8, dmg=4, mana=0)

    def specialAttack(self):
        if self.status != "loser":
            self.dmg += 1
            self.hp -= 1


class Assassin(Character):
    def __init__(self, name):
        super().__init__(name, hp=6, dmg=6, mana=20)

    def specialAttack(self, target=None):
        if self.status != "loser" and self.mana >= 20:
            if target is not None:
                target.takeDamage(7)
            self.mana -= 20


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, hp=10, dmg=2, mana=200)

    def specialAttack(self, target=None):
        if self.status != "loser" and self.mana >= 25:
            if target is not None: 
                target.takeDamage(7)
                self.mana -= 25


class Ninja(Character):
    def __init__(self, name):
        super().__init__(name, hp=12, dmg=5, mana=60)

    def specialAttack(self, target=None):
        if self.status != "loser" and self.mana >= 15:
            if target is not None:
                target.takeDamage(6)
                self.mana -= 15


class Game:
    def __init__(self):
        self.turnLeft = 10
        self.characters = [
            Fighter("Grace"),
            Paladin("Ulder"),
            Monk("Moana"),
            Berzerker("Draven"),
            Assassin("Carl"),
            Wizard("Gandalf"),
            Ninja("HamzaLeBoss"),
        ]

    def skipTurn(self):
        self.turnLeft -= 1
        if self.turnLeft == 0:
            self.endGame()

    def startTurn(self):
        print(f"C'est à ton tour {11 - self.turnLeft}")

    def endGame(self):
        survivors = [
            character for character in self.characters if character.status == "playing"]
        if len(survivors) == 1:
            winner = survivors[0]
            winner.status = "winner"
            print(f"{winner.name} Est le gagnant!")
        else:
            print("C'est un match nul")

    def watchStats(self):
        for character in self.characters:
            print(
                f"{character.name}: HP={character.hp}, Mana={character.mana}, Status={character.status}")

    def startGame(self):
        print("Bienvenue dans le RPG game")
        while self.turnLeft > 0:
            self.startTurn()
            random.shuffle(self.characters)
            for character in self.characters:
                if character.status == "playing":
                    print(f"C'est le moment de  {character.name} de jouer")
                    while True:
                        print("1. Attaque normale")
                        print("2. Attaque spéciale")
                        print("3. Afficher les statistiques")
                        try:
                            choice = int(
                                input("Choisissez votre action (1/2/3): "))
                            if choice == 1:
                                target = random.choice(
                                    [c for c in self.characters if c != character and c.status == "playing"])
                                character.dealDamage(target)
                                print(
                                    f"{character.name} attaque {target.name}. Il lui inflige {character.dmg} points de dégâts. {target.name} a maintenant {target.hp} points de vie restants.")
                                break
                            elif choice == 2:
                                if isinstance(character, Paladin):
                                    target = random.choice(
                                        [c for c in self.characters if c != character and c.status == "playing"])
                                    character.specialAttack(target)
                                    print(
                                        f"{character.name} utilise son attaque spéciale sur {target.name}.")
                                else:
                                    character.specialAttack()
                                    print(
                                        f"{character.name} utilise son attaque spéciale.")
                                break
                            elif choice == 3:
                                self.watchStats()  # Afficher les statistiques
                            else:
                                print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
                        except ValueError:
                            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
                    
                    # Vérifier si le joueur est un "loser" après avoir joué
                    if character.status == "loser":
                        break  

                    self.skipTurn()
            self.watchStats()



# Le début du jeux
game = Game()
game.startGame()
