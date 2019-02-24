import unittest

def moveRobot(str1):
    robotposition = [0, 0]
    for a in str1:
        if a == "L":
            robotposition[0] = robotposition[0] - 1
        if a == "R":
            robotposition[0] = robotposition[0] + 1
        if a == "U":
            robotposition[1] = robotposition[1] + 1
        if a == "D":
            robotposition[1] = robotposition[1] - 1
    print("Final position of the robot is: ", robotposition)
    return robotposition


class TestRobotPosition(unittest.TestCase):
    
    def test_move_robot(self):
        self.assertEqual([6, 3], moveRobot("LLLDDDDUUURRRRUUUURRRRR"))

unittest.main(exit=False)