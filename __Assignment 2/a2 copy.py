# Hans van Riet
# Assigment 2
# 04/17/13

# Constants for the contents of the maze.
WALL = '#'                      # The visual representation of a wall.
HALL = '.'                      # The visual representation of a hallway.
SPROUT = '@'                    # The visual representation of a brussels sprout.

# Constants for the directions. Use these to make Rats move.
LEFT        = -1                # The left direction.
RIGHT       =  1                # The right direction.
NO_CHANGE   =  0                # No change in direction.
UP          = -1                # The up direction.
DOWN        =  1                # The down direction.

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        '''(Rat, str, int, int) -> NoneType

        Initialize the rat's four instance variables.
        '''
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.
        '''
        self.row = row
        self.col = col

    def eat_sprout(self):
        '''(Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.
        '''
        self.num_sprouts_eaten += 1

    def __str__(self):
        '''(Rat) -> str
        '''
        ident = "{} at ({}, {}) ate {} sprouts."
        return ident.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)




class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        '''(Maze, list of list of str, Rat, Rat) -> NoneType
        '''
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        # count the number of sprouts in the maze
        count = 0
        for item in maze:
            count = count + item.count(SPROUT)
        self.num_sprouts_left = count


    def is_wall(self, row, col):
        '''(Maze, int, int) -> bool

        Return True if there is a wall at the given row and column of the maze.
        '''
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        '''(Maze, int, int) -> str

        Return the character in the maze at the given row and column.
        If there is a rat at that location,
        then its character should be returned rather than HALL.
        '''
        # First test if the rats are on the given location
        if (self.rat_1.row == row and self.rat_1.col == col):
            return RAT_1_CHAR
        elif (self.rat_2.row == row and self.rat_2.col == col):
            return RAT_2_CHAR
        # If there's no rat at the given location, return the maze character
        else:
            return self.maze[row][col]


    def move(self, thisRat, moveRow, moveCol):
        '''Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall in the way.
        '''
        # Calculate the new position after a potential move
        newRow = thisRat.row + moveRow
        newCol = thisRat.col + moveCol
        # Now test for the character at that position in the maze
        if self.is_wall(newRow, newCol):     # There's a wall, we cannot move and return False
            return False
        if self.get_character(newRow, newCol) == SPROUT: # There's a Sprout, eat it and update the varables
        #   self.maze[newRow][newCol] = HALL
            self.num_sprouts_left -= 1
            thisRat.eat_sprout()
        # Finally, redraw the HALL at the oldposition, move the rat in the new position and return True
        self.maze[thisRat.row][thisRat.col] = HALL
        thisRat.set_location(newRow, newCol)
        return True

    def __str__(self):
        '''(Maze) -> str

        Return a string representation of the maze.
        '''
        # First populate the maze with the two rats
        self.maze[self.rat_1.row][self.rat_1.col] = RAT_1_CHAR
        self.maze[self.rat_2.row][self.rat_2.col] = RAT_2_CHAR
        # Now scan the maze and build a return string from the maze characters
        returnString = ''
        for item in self.maze:
            for character in item:
                returnString = returnString + character
            returnString = returnString + '\n'
        # Append the two rat strings and return the result
        return returnString + str(self.rat_1)+'\n'+str(self.rat_2)
