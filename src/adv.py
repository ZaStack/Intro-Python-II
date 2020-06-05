from room import Room
from player import Player
from item import Item
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

item = {
    "torch": Item("Torch", "To light your way"),
    "sword": Item("Sword", "Stick em with the pointy end"),
    "shield": Item("Shield", "So they don't stick you with the pointy end"),
    "pouch": Item("Pouch", "For carrying your shit"),
    "skooma": Item("Skooma", "Because why not?"),
}

room["outside"].items.append(item["torch"])
room["foyer"].items.append(item["sword"])
room["foyer"].items.append(item["shield"])
room["overlook"].items.append(item["skooma"])
room["narrow"].items.append(item["pouch"])


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
player1 = Player(name="Zach", position=room["outside"])


# Write a loop that:
#
# * Prints the current room name
print(f"##########Welcome {player1.name}#########")
print("#" * 31)
print(f"You are in {player1.position}")
player1.position.inspect_room()
print("#" * 31)
print(
    "## You can go N, S, E, or W. You can also take and drop items, or type inventory. ##"
)
print("###############################")
print("# What would you like to do? #")

while True:
    choice = input("> ")
    player_choice = choice.lower().split(" ")
    if len(player_choice) is 1:
        if choice is "q":
            print(f"Fine then, nobody likes you anyway, {player1.name}")
            sys.exit()
        elif choice is "n" or choice is "s" or choice is "e" or choice is "w":
            player1.move(choice)
            print(f"You are now in {player1.position}")
            player1.position.inspect_room()
        elif choice is "i":
            player1.check_inv()
        else:
            print("Need a proper command")

    elif len(player_choice) is 2:
        if player_choice[0] in ["take", "get", "pickup"]:
            if item[player_choice[1]]:
                player1.get_item(item[player_choice[1]])
            else:
                print("That isn't something you see in here")
        elif player_choice[0] == "drop":
            if item[player_choice[1]]:
                player1.drop_item(item[player_choice[1]])
                print("Hey, I think you dropped something")
                player1.check_inv()
            else:
                print("That isn't something you have on you")
    else:
        print("Need a proper command")
#  * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
