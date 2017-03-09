import sys
import models

def format_input(filename):
	'''
		A helper function to format the input data read from the specified file.
			open the file
			construct a list of the lines in the file, removing the new line character
			construct a dictionary which specifies the length and width of the plateau,
			and the starting location, direction for each rover
	'''	
		# TODO add checking for input format validity
		# TODO comments
	
	file = open(filename, 'rU')
	lines = []
	inputs = {'rovers': []}
	for line in file:
		lines.append(line.replace('\n', ''))
	file.close()
	rover = {}
	for index, line in enumerate(lines):
		if index == 0:
			plateaus = line.split(' ')
			inputs['plateau'] = { 'length': int(plateaus[0]), 'width': int(plateaus[1]) }
		else:
			if index % 2 != 0:
				start = line.split(' ')
				rover['x'] = int(start[0])
				rover['y'] = int(start[1])
				rover['heading'] = start[2]
			else:
				rover['commands'] = line
		if 'commands' in rover:
			inputs['rovers'].append(rover)
			rover = {}
	return inputs

def deploy_rovers(inputs):
	length = inputs['plateau']['length']
	width = inputs['plateau']['width']
	rovers = inputs['rovers']
	planet = models.Planet('Mars')
	plateau = models.Plateau(length, width)
	planet.add_plateau(plateau)
	for rover in rovers:
		current_rover = models.Rover(rover['x'], rover['y'], rover['heading'])
		plateau.add_rover(current_rover)
		commands = rover['commands']
		for command in commands:
			current_rover.command_rover(command)
		print(current_rover.get_position())
	
def main():
	#get the input file
	filename = sys.argv[1]
	#format the input file contents into a dictionary
	inputs = format_input(filename)
	#create planet, plateau, and deploy rovers based on inputs
	deploy_rovers(inputs)
if __name__ == '__main__':
  main()