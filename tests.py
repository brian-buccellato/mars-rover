import unittest
import models


class TestPlanet(unittest.TestCase):
    """
    Test Planet() class and its methods
    """
    def test_name(self):
        planet = models.Planet('Mars')
        expected_name = 'Mars'
        self.assertEqual(planet.name, expected_name)
        
    def test_plateau_list(self):
        planet = models.Planet('Mars')
        plateau = models.Plateau(5, 5)
        planet.add_plateau(plateau)

        self.assertEqual(len(planet.plateau_list), 1)
        self.assertEqual(planet.plateau_list[0].length, 5)
        self.assertEqual(planet.plateau_list[0].width, 5)


class TestPlateau(unittest.TestCase):
    """
    Test Plateau() class and its methods
    """
    def test_length_and_width(self):
        plateau = models.Plateau(5, 5)
        
        self.assertEqual(plateau.length, 5)
        self.assertEqual(plateau.width, 5)
    
    def test_rover_list(self):
        plateau = models.Plateau(5, 5)
        rover = models.Rover(1, 1, 'N')
        plateau.add_rover(rover)
        
        self.assertEqual(len(plateau.rover_list), 1)
        self.assertEqual(plateau.rover_list[0].x_pos, 1)
        self.assertEqual(plateau.rover_list[0].y_pos, 1)
        self.assertEqual(plateau.rover_list[0].heading, 'N')

    
class TestRover(unittest.TestCase):
    """
    Test Rover() class and its methods
    """

    def test_rover(self):
        rover = models.Rover(1, 2, 'N')
        
        self.assertEqual(rover.x_pos, 1)
        self.assertEqual(rover.y_pos, 2)
        self.assertEqual(rover.heading, 'N')

    def test_move_west(self):
        rover = models.Rover(1, 1, 'W')
        rover.move()

        self.assertEqual(rover.x_pos, 0)
        self.assertEqual(rover.y_pos, 1)

    def test_move_east(self):
        rover = models.Rover(1, 1, 'E')
        rover.move()

        self.assertEqual(rover.x_pos, 2)
        self.assertEqual(rover.y_pos, 1)

    def test_move_north(self):
        rover = models.Rover(1, 1, 'N')
        rover.move()

        self.assertEqual(rover.y_pos, 2)
        self.assertEqual(rover.x_pos, 1)

    def test_move_south(self):
        rover = models.Rover(1, 1, 'S')
        rover.move()

        self.assertEqual(rover.y_pos, 0)
        self.assertEqual(rover.x_pos, 1)

    def test_turn_left(self):
        rover = models.Rover(1, 1, 'N')
        rover.turn_left()

        self.assertEqual(rover.heading, 'W')

    # TODO Add additional tests for turning left from each direction

    def test_turn_right(self):
        rover = models.Rover(1, 1, 'N')
        rover.turn_right()

        self.assertEqual(rover.heading, 'E')

    # TODO Add additional tests for turning right from each direction
    
    def test_command_rover_left(self):
        rover = models.Rover(1, 1, 'N')
        rover.command_rover('L')
		
        self.assertEqual(rover.heading, 'W')
	
	# TODO Add additional tests for commanding rover left from all directions

    def test_command_rover_right(self):
        rover = models.Rover(1, 1, 'N')
        rover.command_rover('R')

        self.assertEqual(rover.heading, 'E')
    
	# TODO Add addtional tests for commanding rover right from all directions
	
    def test_command_rover_move(self):
        rover = models.Rover(1, 1, 'N')
        rover.command_rover('M')
        
        self.assertEqual(rover.x_pos, 1)
        self.assertEqual(rover.y_pos, 2)
		
	# TODO Add Additional tests for commanding rover to move in all directions
		

if __name__ == '__main__':
    unittest.main()
	