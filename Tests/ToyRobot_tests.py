import unittest
from ToyRobot.ToyRobot import Robot
import StringIO
import sys


class RobotTests(unittest.TestCase):
    def test_show_current_state(self):

        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        my_robot = Robot()
        my_robot.set_place(0,0)
        my_robot.show_current_state()
        sys.stdout = sys.__stdout__
        self.assertEquals(capturedOutput.getvalue(), "0,0,WEST\n")

    def test_calculate_orientation(self):
        self.assertEquals(Robot.calculate_orientation('NORTH'), 0)
        self.assertEquals(Robot.calculate_orientation('EAST'), 1)
        self.assertEquals(Robot.calculate_orientation('SOUTH'), 2)
        self.assertEquals(Robot.calculate_orientation('WEST'), 3)

    def test_check_position(self):
        self.assertTrue(Robot.check_position(0, 0))
        self.assertTrue(Robot.check_position(4, 4))
        self.assertFalse(Robot.check_position(5, 0))
        self.assertFalse(Robot.check_position(0, 5))
        self.assertFalse(Robot.check_position(5, 5))
        self.assertFalse(Robot.check_position(-1, 0))
        self.assertFalse(Robot.check_position(0, -1))
        self.assertFalse(Robot.check_position(-1, -1))

    def test_ready(self):
        my_robot = Robot()
        self.assertFalse(my_robot.ready())
        my_robot.initialized = 1
        self.assertTrue(my_robot.ready())

    def test_check_correct_move(self):
        pass

    def test_move(self):
        pass

    def test_check_correct_place(self):
        pass

    def test_turn(self):
        pass

    def test_check_orientation(self):
        pass

    def test_parse_first_input(self):
        pass

    def test_parse_second_input(self):
        pass

    def test_positionate(self):
        pass
