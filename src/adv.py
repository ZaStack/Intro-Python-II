from room import Room
from player import Player
import textwrap
import cmd
import sys
import os


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
def print_location():
    print('\n' + ('#' * (4 +len(player1.position))))
    print('# ' + player1.position.upper() + ' #')
    print('#' * (4 +len(player1.position)))
    print('\n' + (room[player1.position]))

def prompt():
	print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Where would you like to go?")
	action = input("> ")
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'q']
	while action.lower() not in acceptable_actions:
		print("Unknown action command, please try again.\n")
		action = input("> ")
	if action.lower() == quitgame:
		sys.exit()
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		move(action.lower())

def move(myAction):
    ask
#  * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while player1.won is False:
    move = input("Enter a direction or q to quit")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
