#Programmed a interactive Swat Clearing Game using class (functions.py)
#Mariah Mitchell
#CSC 121
#12/11/2025



#----------- Player Class-----------------
class Player:
    def __init__(self, name, gender, badge_number, skill):
        self._name = name
        self._gender = gender
        self._badge_number = badge_number
        self._skill = skill
    
        self.inventory = ["Baton", "Medkit"]
        self.health = 100
#Getter Methods  
    def get_name(self):
        return self._name
    def get_gender(self):
        return self._gender
    def get_badge_number(self):
        return self._badge_number
    def get_skill(self):
        return self._skill
#Setter Methods
    def set_name(self, name):
        self._name = name
    def set_gender(self, gender):
        self._gender = gender
    def set_badge_number(self, badge_number):
        self._badge_number = badge_number
    def set_skill(self, skill):
        self._skill = skill
#Combat attack
    def attack(self, enemy):
        damage = 20
        enemy.health -= damage
        print(f"{self._name} hits {enemy.get_name()} for {damage} damage!")
    def gain(self, xp):
        print(f"{self._name} gained {xp} XP!")
       

#-----------Enemy Class-------------
class Enemy:
    def __init__(self, name):
        self._name = name
        self.health = 50
#       Getter Method
    def get_name(self):
        return self._name
   
# Setter Method
    def set_name(self, name):
        self._name = name

#-------------Inventory Class------------
class Inventory:
    def __init__(self,):
        self.items =[]
    def add_item(self, item):
        self.itemd.append(item)
        print(f"Picked up: {item.name}")
        
#-----------Item Class------------------
class Item:
    def __init__(self, name, effect, value):
        self.name = name
        self.effect = effect
        self.value =value
        

#---------Functions--------------
#options menu
def turn_menu():
    '''

    Returns
    -------
    choice : input
        Option to choose to move forward or exit the building.

    '''
    print("\n===== YOUR TURN =====")
    print("1. Move Forward")
    print("2. Exit Building")

    choice = input("Choose an option: ")

    while choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Choose an option: ")

    return choice
    
def get_characters(): 
    '''
    Returns
    -------
    list
        A list of the each character and description.

    '''
    return [
        Player("Officer Manning", "Female", "2257", "Marksman"),
        Player("Officer Jackson", "Male", "4024", "Breacher"),
        Player("Officer Dundas", "Female", "9502", "Negotiator")  
        ]
#Movement Function
def choose_direction():
    '''
    Prompt player to choose direction to move

    Returns
    -------
    direction : list of str
        The direction chosen by  the player.

    '''
    valid_directions = ["North", "South", "East", "West"]

    direction = input("\nEnter direction (North, South, East, West): ").strip().title()

    while direction not in valid_directions:
        print("\nInvalid input. Please type North, South, East, or West.")
        direction = input("Enter direction: ").strip().title()

    return direction
#Rooms
def create_random_room():
    '''
    Randomly generates a room.

    Returns
    -------
    Enemy, Item, None
        Enemy object if the room has an enemy.
        Item object if the room has an item.
        None if the room is empty.

    '''
    import random
    room_type = random.randint(1, 3)
    
    if room_type == 1:
        return Enemy("Criminal")
    elif room_type == 2:
        return Item("Med Kit", "heal", 25)
    else:
        return None #empty rooms
#Combat Function  
def combat(player, enemy):
    '''
    turn-based combat between the player and enemy.

    Parameters
    ----------
    player : objecct
        The player attacks first.
    enemy : object
        The enemy attacks first.
        Combat continues until a health reaches 0

    Returns
    -------
    None.

    '''
    print("\n ENEMY ENCOUNTER! Combat Begins!")
    
    while player.health > 0 and enemy.health > 0:
        input("\nPress Enter to attack first...")
        player.attack(enemy)
        if enemy.health <= 0:
            print("Enemy defeated!")
            player.gain(10)
            return
        #Enemy Encounter Attack
        enemy_damage = 10
        player.health -= enemy_damage
        print(f"{enemy.get_name()} hits {player.get_name()} for {enemy_damage}!")
        if player. health <= 0:
            print("You were defeated!")
            return

    
        
    
        