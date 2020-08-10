from room import Room
from item import Item
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside the Cave Entrance",
                     "North of you, the cave mount beckons", ''),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ''),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ''),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ''),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ''),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#ITEMS
item_list = {
    'frogs': Item('Frogs','They Just Hop around.'),
    'note': Item('An old note', 'It is really old.')
}

#room items
room['outside'].items.append(item_list['frogs'])
room['foyer'].items.append(item_list['note'])    

#get_item
def get_item(name):
    player_character.inventory.append(item_list[f'{name}'])
    player_character.location.items.remove(item_list[f'{name}'])
    print('You got ', item_list[f'{name}'].name)

#drop_item
def drop_item(name):
    print(item_list[f'{name}'])
    player_character.inventory.remove(item_list[f'{name}'])
    player_character.location.items.append(item_list[f'{name}'])
    print(player_character.location.items[0])

#
# Main
game_over = False

player_character = Player("","20","Medium","2","50","Catacombs","")
player_character.location = room['outside']
# 
print("\n\n Welcome adventurer, before you is a perilous quest, do you have what it takes to survive? We shall soon find out!\n\n")

player_character.name = input("Before You go to meet your doom, what is your name? \n")

print(f"\n{player_character.name}, eh? I thought that may be it. Well, get to it, there is a monster or something in that cave and you gotta go get it.\n")
print("\n Your adventure begins now...\n")

print('\n [W] will take you North, [A] will take you West, [S] will take you South, and [D] will take you East.  \n')
player_character.inventory.pop(0)
player_character.location.items.pop(0)
while not game_over:
    print(f"Your position - {player_character.location}")
    #Prints players position with description of the room.
    if len(player_character.location.items) >= 1:
        
        print('\n --> Interesting items in this location:')
        for i in player_character.location.items:
            print(f'--> {i}')
    else:
        print('There are no items of interest here.')
    #if there are items of note in the room they are pinted out here.

    print('\n [W] will take you North, [A] will take you West, [S] will take you South, and [D] will take you East.  \n')
    response = input("\nWhat would you like to do?\n").lower().strip().split()
    #Response given at the beginning og the loop with some help text.

    
    
    #Directional keys
    if response[0] == 'w' and hasattr(player_character.location, 'n_to'):
        player_character.location = player_character.location.n_to
        print('\nYou Move North\n')

    elif response[0] == 'a' and hasattr(player_character.location, 'w_to'):
        player_character.location = player_character.location.w_to

    elif response[0] == 's' and hasattr(player_character.location, 's_to'):
        player_character.location = player_character.location.s_to

    elif response[0] == 'd' and hasattr(player_character.location, 'e_to'):
        player_character.location = player_character.location.e_to

    elif response[0] == 'get' and f"{response[1]}" in item_list:
        get_item(response[1])
    elif response[0] == 'drop' and f"{response[1]}" in item_list:
        if item_list[f"{response[1]}"] not in player_character.inventory:
            print("You dont have any of that to drop.")
        else:
            drop_item(response[1])
    #Directional Keys -  End
    elif response[0] == 'i':
        
        print('\nYour Inventory:')
        for i in player_character.inventory:
            print(type(i))
            print(f'-> {i}')
        print('\n')
    #if i is pressed prints out the players inventory
    else: 
        print("\n--> You cannot do that, try again.\n")
    

    

    if response[0] == 'q':
        print('Well, you tried at least. GAME OVER')
        break
    
    


    
       
            

            





    



# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
