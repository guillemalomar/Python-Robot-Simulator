import unittest
from ToyRobot.ToyRobot import Robot
import StringIO
import sys


class Test_Robot(unittest.TestCase):

    def test_show_current_state(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        my_robot = Robot((0, 0), 'NORTH')
        my_robot.show_current_state()
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(), "0,0,NORTH\n")

    def test_calculate_orientation(self):
        self.assertEquals(Robot.calculate_orientation('NORTH'), 0)
        self.assertEquals(Robot.calculate_orientation('EAST'), 1)
        self.assertEquals(Robot.calculate_orientation('SOUTH'), 2)
        self.assertEquals(Robot.calculate_orientation('WEST'), 3)
        self.assertEquals(Robot.calculate_orientation('north'), 0)
        self.assertEquals(Robot.calculate_orientation('east'), 1)
        self.assertEquals(Robot.calculate_orientation('south'), 2)
        self.assertEquals(Robot.calculate_orientation('west'), 3)

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
        my_robot = Robot((0, 0), 'NORTH')
        self.assertFalse(my_robot.ready())
        my_robot.initialized = 1
        self.assertTrue(my_robot.ready())

    def test_check_correct_move(self):
        my_robot = Robot((0, 0), 'NORTH')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('EAST')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('SOUTH')
        self.assertFalse(my_robot.check_correct_move())
        my_robot.set_orientation('WEST')
        self.assertFalse(my_robot.check_correct_move())
        my_robot = Robot((4, 4), 'SOUTH')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('WEST')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('NORTH')
        self.assertFalse(my_robot.check_correct_move())
        my_robot.set_orientation('EAST')
        self.assertFalse(my_robot.check_correct_move())
        my_robot = Robot((4, 0), 'NORTH')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('WEST')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('EAST')
        self.assertFalse(my_robot.check_correct_move())
        my_robot.set_orientation('SOUTH')
        self.assertFalse(my_robot.check_correct_move())
        my_robot = Robot((0, 4), 'EAST')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('SOUTH')
        self.assertTrue(my_robot.check_correct_move())
        my_robot.set_orientation('NORTH')
        self.assertFalse(my_robot.check_correct_move())
        my_robot.set_orientation('WEST')
        self.assertFalse(my_robot.check_correct_move())

    def test_move(self):
        my_robot = Robot((0, 0), 'NORTH')
        my_robot.move()
        self.assertEquals(my_robot.get_place(), (0, 1))
        my_robot.move()
        self.assertEquals(my_robot.get_place(), (0, 2))
        my_robot.move()
        self.assertEquals(my_robot.get_place(), (0, 3))
        my_robot.move()
        self.assertEquals(my_robot.get_place(), (0, 4))
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        my_robot.move()
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(), "Incorrect Move, robot would fall out of the table.\n")

    def test_check_correct_place(self):
        self.assertEquals(Robot.check_correct_place('PLACE 0,0,  NORTH'), (0, 0, 'NORTH'))
        self.assertEquals(Robot.check_correct_place('PLACE 0,0,  north'), (0, 0, 'NORTH'))
        self.assertEquals(Robot.check_correct_place('PLACE 5,  0,NORTH'), None)
        self.assertEquals(Robot.check_correct_place('PLACE 5 ,0,north'), None)
        self.assertEquals(Robot.check_correct_place('PLACE 0,0, NORT'), None)

    def test_turn(self):
        my_robot = Robot((0, 0), 'NORTH')
        my_robot.turn('left')
        self.assertEquals(my_robot.get_orientation(), 'WEST')
        my_robot.turn('left')
        self.assertEquals(my_robot.get_orientation(), 'SOUTH')
        my_robot.turn('right')
        self.assertEquals(my_robot.get_orientation(), 'WEST')

    def test_check_orientation(self):
        self.assertTrue(Robot.check_orientation('south'))
        self.assertFalse(Robot.check_orientation('suth'))
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        Robot.check_orientation('suth')
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(),
                          "Error defining new orientation. The Robot must face 'NORTH', 'SOUTH', 'WEST' or 'EAST'.\n")

    def test_parse_second_input(self):
        my_robot = Robot((0, 0), 'NORTH')
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        my_robot.parse_second_input('bla')
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(), "Not a correct input\n")
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        my_robot.parse_second_input('place 0,0,North')
        sys.stdout = sys.__stdout__
        self.assertEquals(captured_output.getvalue(), "")

    def test_position(self):
        my_robot = Robot()
        my_robot.position((3, 4, 'EAST'))
        self.assertEquals(my_robot.get_place(),(3,4))
        self.assertEquals(my_robot.get_orientation(),'EAST')
