# This is a game to explore rooms of a house

# Define a Room class to represent individual rooms in game
class Room:
    def __init__(self, name, description, exits):
        self.name = name # Name of the room
        self.description = description # Description of the room
        self.exits = exits # Dictionary of exits from this room

# Define player class to represent the player
class Player:
    def __init__(self, name, current_room):
        self.name = name # Player's name
        self.current_room = current_room # Current room player is in 


# Define a function to handle user input for moving between rooms
def handle_user_input(player, rooms):
    action = input('What do you want to do? ')  # Prompt the user for input

    if action.startswith("go "):
        # Check if the input starts with "go "
        direction = action[3:]  # Extract the direction from the input after index 3

        if direction in player.current_room.exits:
            # Check if the direction is a valid exit from the current room
            new_room_name = player.current_room.exits[direction]  # Get the name of the room in the chosen direction
            player.current_room = rooms[new_room_name]  # Move the player to the new room
        else:
            # If the direction is not valid, print a message indicating there's no door in that direction
            print(f'There is no door to the {direction}.')
    else:
        # If the input doesn't start with "go ", print an "Invalid input" message
        print('Invalid input.')

# Define a function named 'game' that takes a 'player' object as an argument
def game(player):
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
        'Nook': Room('Nook', 'You are in a quiet nook.', {'south': 'Dining Room', 'west': 'Living Room'})
    }

    # Create a player object and place them in the 'Kitchen' room initially
    player = Player('Celeste', rooms['Kitchen'])

    # Call the 'game' function to start the game with the 'player' object
    game(player)




