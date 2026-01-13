#Programmed a Swat Clearing Game using class (main.py)
#Mariah Mitchell
#CSC 121
#12/11/2025

import finalProject_MitchellMariah_functions as fn

def main():
    '''
    Create a main menu for the SWAT Building Clearing Game

    Returns
    -------
    None.

    '''
    print("="*40)
    print("SWAT Building Clearing Game")
    print("="*40)
    print("Your fellow comrades have been taking hostage during a heist.")
    print("They need your help to clear buiding and eliminate the threat!")
    print("-"*40)
    print("Choose your SWAT Officer:")
    
    #load character list from function.py
    characters = fn.get_characters()
    
    #Display character selection menu
    for i, character in enumerate(characters):
        print(f"{i}. {character.get_name()} - {character.get_skill()}")
   
    #Get player choice
    choice = int(input("Enter number: ")) 
    #Validate choice
    if choice < 0 or choice >= len(characters):
        print("Invalid choice. Defautling to first officer.")
        player = characters[0]
    else:
        player = characters[choice]
        
    print(f"\nYou selected: {player.get_name()}")
#game loop
    game_running = True

    while game_running and player.health > 0:
    
        option = fn.turn_menu()
    
        if option == "1":
            # MOVE FORWARD
            direction = fn.choose_direction()
            print(f"You move {direction}...")
            
            room = fn.create_random_room()
    
            if room is None:
                print("The room is empty.")
            elif isinstance(room, fn.Enemy):
                print(f"You encountered an enemy: {room.get_name()}!")
                fn.combat(player, room)
            elif isinstance(room, fn.Item):
                print(f"You found an item: {room.name}")
                player.inventory.append(room.name)
        
        elif option == "2":
            # EXIT BUILDING
            print("\nYou decide to exit the building. Mission aborted.")
            game_running = False
            
        

if __name__ == "__main__":
    main()
