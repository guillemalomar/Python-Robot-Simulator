import unittest
from RobotApp import check_input, message_output1, message_output2
import StringIO
import sys


class RobotApp_Test(unittest.TestCase):

    def test_message_output1(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        message_output1()
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(), 'This is an application to place a robot on a table of 5x5.\nAfter placing it, you will be able to move it all over the table.\nFirst place value is on the West/East axis, second is on the North/South axis.\nTo quit the application, insert "exit"\n')

    def test_message_output2(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        message_output2()
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(), "Now that the robot has been initialized, you can either:\n    a) 'PLACE x, y, orientation(NORTH,SOUTH,EAST or WEST' to define a new position\n    b) 'MOVE' the robot forward to a new position\n    c) Turn the robot 'LEFT' or 'RIGHT'\n    d) 'REPORT' current robot state\n")

    def test_check_input(self):
        self.assertRaises(SystemExit, check_input, 'exit')
        self.assertEquals(check_input('not_exit'), 0)
