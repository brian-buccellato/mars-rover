import unittest
import models

class TestPlanet(unittest.TestCase):
	"""
	Test Planet() class and it's methods
	
	"""
	def test_name(self):
		planet = models.Planet('Mars')
		expected_name = 'Mars'
		self.assertEqual(planet.name, expected_name)
		
	def test_plateau_list_from_example(self):
		planet = models.Planet('Mars')
		plateau = models.Plateau(5, 5)
		planet.add_plateau(plateau)
		plateaus = planet.plateau_list
		
		self.assertEqual(len(plateaus), 1)
		self.assertEqual(plateaus[0].length, 5)
		self.assertEqual(plateaus[0].width, 5)
		
class TestPlateau(unittest.TestCase):
	"""
	Test Plateau() class and its methods
	"""
	def test_length_and_width(self):
		plateau = models.Plateau(5, 5)
		
		self.assertEqual(plateau.length, 5)
		self.assertEqual(plateau.length, 5)
	
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
	Test Rover() class and it's methods
	
 	"""
	def test_rover(self):
		rover = models.Rover(1, 2, 'N')
		
		self.assertEqual(rover.x_pos, 1)
		self.assertEqual(rover.y_pos, 2)
		self.assertEqual(rover.heading, 'N')
	
	def test_command_rover(self):
		rover = models.Rover(1, 1, 'N')
		rover.command_rover('M')
		
		self.assertEqual(rover.y_pos, 2)
		self.assertEqual(rover.x_pos, 1)
		
		rover.command_rover('L')
	
		self.assertEqual(rover.heading, 'W')
	
		rover.command_rover('M')
		
		self.assertEqual(rover.x_pos, 0)
		self.assertEqual(rover.y_pos, 2)
		
		rover.command_rover('R')
		
		self.assertEqual(rover.heading, 'N')
		
		rover.command_rover('R')
		
		self.assertEqual(rover.heading, 'E')
		
		rover.command_rover('M')
		
		self.assertEqual(rover.x_pos, 1)
		self.assertEqual(rover.y_pos, 2)
		
		rover.command_rover('R')
		
		self.assertEqual(rover.heading, 'S')
		
		rover.command_rover('M')
		
		self.assertEqual(rover.x_pos, 1)
		self.assertEqual(rover.y_pos, 1)
		
if __name__ == '__main__':
    unittest.main()