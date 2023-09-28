# This is a game to explore rooms of a house

# Define a Room class to represent individual rooms in the game
class Room:
    def __init__(self, name, description, exits, hidden_item=None):
        self.name = name  # Name of the room
        self.description = description  # Description of the room
        self.exits = exits  # Dictionary of exits from this room
        self.hidden_item = hidden_item

# Define a player class to represent the player
class Player:
    def __init__(self, name, current_room):
        self.name = name  # Player's name
        self.current_room = current_room  # Current room player is in
        self.hidden_item_found = False  # Track if hidden item is found

# Define a function to handle user input and move the player between rooms
def handle_user_input(player, rooms):
    print(f'Available exits: {", ".join(player.current_room.exits.keys())}')
    action = input('Where do you want to go? ')

    if action in player.current_room.exits:
        new_room_name = player.current_room.exits[action]
        player.current_room = rooms[new_room_name]
  
       # Check if there is a hidden item in the current room and mark it as found
        if player.current_room.hidden_item and not player.hidden_item_found:
            print(f'You found a {player.current_room.hidden_item}!')
            player.hidden_item_found = True

             # Check if the found item is the flashlight and print congratulations
            if player.current_room.hidden_item == 'flashlight':
                print('Congratulations! You found the flashlight!')
    else:
            print(f'There is no door to the {action}.')

# Define a function named 'game' that takes a 'player' object as an argument
def game(player):
    # Print a message at the beginning of the game
    print('You wake up in a dark house. The power is out, and all the rooms are dark. You need to find a flashlight.')

    # Create an infinite loop that keeps the game running until explicitly terminated
    while True:
        # Print the name of the current room the player is in
        print(player.current_room.name)

        # Print the description of the current room
        print(player.current_room.description)

        # Call the 'handle_user_input' function to handle player input and room navigation
        handle_user_input(player, rooms)

# Check if this script is the main program being run
if __name__ == '__main__':
    # Define a dictionary named 'rooms' that represents the game's rooms and their characteristics
    rooms = {
        'Kitchen': Room('Kitchen', 'You are in a large kitchen.', {'north': 'Living Room'}),
        'Living Room': Room('Living Room', 'You are in a spacious living room.', {'south': 'Kitchen', 'east': 'Dining Room'}),
        'Dining Room': Room('Dining Room', 'You are in a cozy dining room.', {'east': 'Kitchen', 'west': 'Living Room', 'north': 'Nook'}),
        'Nook': Room('Nook', 'You are in a quiet nook.', {'south': 'Dining Room', 'west': 'Living Room'}, hidden_item='flashlight')
    }

    # Create a player object and place them in the 'Kitchen' room initially
    player = Player('Celeste', rooms['Kitchen'])

    # Call the 'game' function to start the game with the 'player' object
    game(player)

    # Check if the player found the hidden item
    if player.hidden_item_found:
        print('Congratulations! You found the hidden item (flashlight)!')
    else:
        print('Game over. You did not find the hidden item.')
