'''
/***********************************************
*    Title: Moving Robot Application           *
*    Author: Guillem Nicolau Alomar Sitjes     * 
*    Date: July 15th, 2017                     *
*    Code version: 0.1                         *
*    Availability: Public                      *
***********************************************/
'''


import re
from Landscape import Landscape


class Robot:
    place = (-1, -1)
    current_orientation = -1
    initialized = 0
    possible_orientations = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self, place=None, orientation=None, size=(4,4)):
        if place is not None:
            self.place = place
        if orientation is not None:
            self.current_orientation = Robot.possible_orientations.index(orientation.upper())
        self.landscape = Landscape(size)

    # This method defines a new position for the robot (used or the tests)
    # Input:
    #     new_x: new x coordinate position
    #     new_y: new y coordinate position
    def set_place(self, new_x, new_y):
        self.place = (new_x, new_y)

    # This method defines a new orientation for the robot (used or the tests)
    # Input:
    #     new_orientation: new orientation for the robot
    def set_orientation(self, new_orientation):
        self.current_orientation = Robot.possible_orientations.index(new_orientation)

    # This method returns de current position for the robot (used or the tests)
    # Output:
    #     (place): current robot position
    def get_place(self):
        return self.place

    # This method returns de current orientation for the robot (used or the tests)
    # Output:
    #     orientation: current robot orientation
    def get_orientation(self):
        return Robot.possible_orientations[self.current_orientation]

    # This method prints the REPORT order information
    def show_current_state(self):
        print str(self.place[0]) + "," +\
              str(self.place[1]) + "," +\
              Robot.possible_orientations[self.current_orientation]

    # This method translates the orientation from the input string to a clockwise ordered number that specifies
    # the orientation (easier for turning the robot)
    # Input:
    #     new_orientation: new orientation
    # Output:
    #     translated to clockwise ordered number
    @staticmethod
    def calculate_orientation(new_orientation):
        return Robot.possible_orientations.index(new_orientation.upper())

    # This method checks if the robot can be put in the specified position
    # Input:
    #     new_x: new x coordinate position
    #     new_y: new y coordinate position
    # Output:
    #     0 (False) if the new poisition is not valid
    #     1 (True) if the new position is valid
    def check_position(self, new_x, new_y):
        if new_x not in range(0, self.landscape.get_dims()[0]+1) or new_y not in range(0, self.landscape.get_dims()[1]+1):
            print "Error defining new position. The Robot must be in a table of size 5x5."
            return 0
        return 1

    def ready(self):
        return self.initialized

    # This method checks if the robot can be put in the specified position, and returns the parsed values from the input
    # Input:
    #     input_val: the input message
    # Output:
    #     new_x, new_y, new_orientation: parsed parameters needed to place the object in a new position
    def check_correct_place(self, input_val):
        try:
            variables = input_val.upper().split('PLACE')[1]
            new_x = int(re.sub(r'\s+', '', variables.split(',')[0]))
            new_y = int(re.sub(r'\s+', '', variables.split(',')[1]))
            new_orientation = re.sub(r'\s+', '', str(variables.split(',')[2]))
            if self.check_position(new_x, new_y) and Robot.check_orientation(new_orientation):
                return new_x, new_y, new_orientation
            else:
                print "The input message isn't valid."
                return None
        except Exception as e:
            if type(e) == IndexError:
                print "The input message isn't valid."
            if type(e) == ValueError:
                print "The input message isn't valid."
            return None

    # This method checks of the robot can move forward depending on its current position and orientation
    def check_correct_move(self):
        if (self.current_orientation == 0 and self.place[1] == self.landscape.get_dims()[1]) or \
           (self.current_orientation == 1 and self.place[0] == self.landscape.get_dims()[0]) or \
           (self.current_orientation == 2 and self.place[1] == 0) or \
           (self.current_orientation == 3 and self.place[0] == 0):
            print "Incorrect Move, robot would fall out of the table."
            return 0
        return 1

    # This method moves the robot to a new position
    def move(self):
        if self.check_correct_move():
            new_place = ''
            if self.current_orientation == 0:
                new_place = (self.place[0], self.place[1] + 1)
            if self.current_orientation == 1:
                new_place = (self.place[0] + 1, self.place[1])
            if self.current_orientation == 2:
                new_place = (self.place[0], self.place[1] - 1)
            if self.current_orientation == 3:
                new_place = (self.place[0] - 1, self.place[1])
            self.place = new_place

    # This method turns the robot to a new orientation
    # Input:
    #     input_val: the new orientation obtained from the input message
    def turn(self, input_val):
        if input_val.upper() == 'LEFT':
            if self.current_orientation > 0:
                self.current_orientation -= 1
            else:
                self.current_orientation = 3
        else:  # Right
            if self.current_orientation < 4:
                self.current_orientation += 1
            else:
                self.current_orientation = 0

    # This method checks if the new orientation is valid
    # Input:
    #     new_orientation: the new orientation obtained from the input message
    # Returns:
    #     0 (False) if the new orientation is not valid
    #     1 (True) if the new orientation is valid
    @staticmethod
    def check_orientation(new_orientation):
        if new_orientation.upper() not in Robot.possible_orientations:
            print "Error defining new orientation. The Robot must face 'NORTH', 'SOUTH', 'WEST' or 'EAST'."
            return 0
        return 1

    # This method analyzes the first application input message
    # Input:
    #     input_val: the input message from the user
    def parse_first_input(self, input_val):
        parsed_input = self.check_correct_place(input_val)
        if parsed_input is not None:
            self.position(parsed_input)

    # This method analyzes the second application input message
    # Input:
    #     input_val: the input message from the user
    def parse_second_input(self, input_val):
        inputval_split = input_val.split(' ')[0].upper()
        if inputval_split == 'PLACE':
            parsed_input = self.check_correct_place(input_val)
            if parsed_input is not None:
                self.position(parsed_input)
        elif inputval_split == 'MOVE':
            self.move()
        elif inputval_split in ['LEFT', 'RIGHT']:
            self.turn(input_val)
        elif inputval_split == 'REPORT':
            self.show_current_state()
        else:
            print 'Not a correct input'

    # This method moves the robot to a new position
    # Input:
    #     args: list of (new_x position, new_y position, new_orientation)
    def position(self, args):
        new_x = int(args[0])
        new_y = int(args[1])
        new_orientation = str(args[2]).replace('\n', '')
        self.place = (new_x, new_y)
        self.current_orientation = Robot.calculate_orientation(new_orientation)
        self.initialized = 1
