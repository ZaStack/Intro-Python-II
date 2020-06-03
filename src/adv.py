from room import Room
from player import Player
import textwrap
import sys


# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(name = 'Zach', position = room['outside'])
solved = False
quitgame = 'quit', 'q'
room_solved = {
    "outside": False,
    "foyer": False,
    "overlook": False,
    "narrow": False,
    "treasure": False,
}

# Write a loop that:
#
# * Prints the current room name
print(f'Welcome {player1.name}')
print(f'You are in {player1.position}')
print('###You can go N, S, E, or W.###')
print('###############################')
print('##Where would you like to go?##')

while True:
    choice = input('> ')
    player_choice = choice.lower()
    if len(player_choice) == 1:
        if choice == 'q':
            print(f'Fine then, nobody likes you anyway, {player1.name}')
            sys.exit()
        elif choice == 'n' or choice == 's' or choice == 'e' or choice == 'w':
            player1.move(choice)
            print(f'You are now in {player1.position}')
        else:
            print('Need a proper command')
    else:
        print('Need a proper command')
#  * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while player1.won is False:
    move = input("Enter a direction or q to quit")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
