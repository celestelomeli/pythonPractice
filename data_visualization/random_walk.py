from random import choice #store possible moves in list and use choice to decide the moves

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000): #set default number of points in walk to value high enough to generate patterns
        """Initialize attributes of a walk """
        self.num_points = num_points

        # All walks start at (0,0), hold values 
        self.x_values = [0]  
        self.y_values = [0]

    def fill_walk(self):# method tells python how to simulate 4 random decisions 
        """Calculate all the points in the walk"""

        # Keep taking steps until walk reaches desired length
        while len(self.x_values) < self.num_points:

            #Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1]) #1 for right movement and -1 for left 
            x_distance = choice([0, 1, 2, 3, 4]) #select integer btwn 1-4
            x_step = x_direction * x_distance #determine length of each step
            #x : pos result= move right, - result = left, 0= vertically

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            # + result = move up, - = down, 0 = horizontally
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            #  continue loop until not 0 
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)