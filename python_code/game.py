class Room:
    def __init__(self, name, description, exits):
        self.name = name 
        self.description = description
        self.exits = exits

class Player:
    def __init__(self, name, current_room):
        self.name = name 
        self.current_room = current_room

def handle_user_input(player, rooms): 
    action = input('Where do you want to go? ')
    
    direction_map = {
        'north': 'north',
        'south': 'south',
        'east': 'east',
        'west': 'west'
    }

    direction = direction_map.get(action, None)
    if direction:
        if direction in player.current_room.exits:
            new_room_name = player.current_room.exits[direction]
            player.current_room = rooms[new_room_name]
        else:
            print(f'There is no door to the {direction}')
    else: 
        print('Invalid input.')

def game(player):
    while True:
        print(player.current_room.name)
        print(player.current_room.description)

        for exit_direction in player.current_room.exits:
            print(f'There is a door to the {exit_direction}.')

        handle_user_input(player, rooms)

if __name__ == '__main__':
    rooms = {
        'Kitchen': Room('Kitchen', 'You are in a large kitchen.', {'north': 'Living Room'}),
        'Living Room': Room('Living Room', 'You are in a large living room with many windows.', {'south': 'Kitchen'}),
        'Dining Room': Room('Dining Room', 'You are in a cozy dining room.', {'east': 'Living Room', 'north': 'Nook'}),
        'Nook': Room('Nook', 'You are in a quiet nook.', {'south': 'Dining Room'})
    }
    
    # Create the player
    player = Player('Celeste', rooms['Kitchen'])

    # Start the game loop
    game(player)

