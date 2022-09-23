wantinfo = input("Write y to read info. Write n to go straight to game.")
ansinfo = False 
playername = "Player"

class Player:
    def __init__(self, name, health, power, magic):
        self.name = name
        self.health = health 
        self.power = power
        self.magic = magic

def start_info():
    print("This is the demo (first level) of a turnbased adventure rpg.")
    print("The game consists only of text.")
    print("to see your characters information, press I.")
    print("write something to start the game.")
    input()
    start_game()

def start_game():
    print("Tell me your name:")
    playername = input()
    p1 = Player(playername, 100, 2, 20)
    print("Welcome to the game " + playername)
    print("This is your information:")

def level1():
    print("Level 1: The Forest")

while ansinfo == False:  
    if wantinfo == "y":
        start_info()
        ansinfo = True
    elif wantinfo == "n":
        start_game()
        ansinfo = True
    else: 
        ansinfo = False
        wantinfo = input("Write either y or n")

