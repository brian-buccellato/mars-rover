import sys
import string

'''
	New classes could include galaxy and universe
	such that a galaxy would consist of planets, and a universe would 
	consist of galaxies.  The Planet class is an example of this idea.
'''

class Planet(object):
	"""A planet containing plateau objects explored by rovers
		Attributes:
			name: string name of planet
			plateau_list: list of all plateaus being explored by rovers on the planet	
	"""
	def __init__(self, name, plateau_list=None):
		self.name = name
		self.plateau_list = plateau_list if plateau_list is not None else []
	
	def add_plateau(self, plateau):
		if plateau not in self.plateau_list:
			self.plateau_list.append(plateau)

class Plateau(object):
    """A plateau to be traversed by a Mars rover.  
		Plateau is modeled as a rectangular grid.
		
		Attributes:
			 width: an integer representing the width of the plateau
			 length: an integer representing the length of the plateau
			 rover_list: a list of all of the rovers currently on the plateau
	"""
    def __init__(self, width, length, rover_list=None):
        self.width = width
        self.length = length
        self.rover_list = rover_list if rover_list is not None else []
	
	#add a rover to the list of all rovers on the plateau
    def add_rover(self, rover):
        if rover not in self.rover_list:
            self.rover_list.append(rover)
			
class Rover(object):
	"""A Mars rover to be deployed on a plateau.
		
		Attributes:
			x_pos: an integer  defining the relative east/west position of the rover
			y_pos: an integer defining the relative north/south position of the rover
			heading: a character which defines the cardinal direction the rover is facing 
	"""
	
	#mapping for left and right turns
	lefts = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
	rights = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
	
	def __init__(self, x_pos, y_pos, heading):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.heading = heading
		
	def command_rover(self, command):
		if command == 'L':
			self.left_turn()
		elif command == 'R':
			self.right_turn()
		else:
			self.move()
				
	
	def left_turn(self):
		self.heading = self.lefts[self.heading]
	
	def right_turn(self):
		self.heading = self.rights[self.heading]
	
	'''
		Rovers are expensive.  Adding functionality to
		make sure they stay on the grid or do not occupy the 
		same spot could be helpful.
	'''
	def move(self):
		if self.heading == 'N':
			self.y_pos += 1
		elif self.heading == 'S':
			self.y_pos -= 1
		elif self.heading == 'E':
			self.x_pos += 1
		else:
			self.x_pos -= 1
	
	def get_position(self):
		return str(self.x_pos) + ' ' +  str(self.y_pos) + ' ' + str(self.heading)
			

			
		

        