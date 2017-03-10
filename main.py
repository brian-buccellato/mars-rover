import sys
import models


def format_input(filename):
    """
    A helper function to format the input data read from the specified file.

    open the file
    construct a list of the lines in the file, removing the new line character
    construct a dictionary which specifies the length and width of the plateau,
    and the starting location, direction for each rover
    """
    # TODO add checking for input format validity
    # TODO comments

    file_handle = open(filename, 'rU')
    lines = [line.replace('\n', '') for line in file_handle]
    file_handle.close()

    # Initialize a set of Rover instances
    inputs = {'rovers': []}

    for index, line in enumerate(lines):
        if index == 0:
            # Initialize plateau
            plateaus = line.split(' ')
            inputs['plateau'] = {'length': int(plateaus[0]), 'width': int(plateaus[1])}
        else:
            # Starting point for a new Rover
            if index % 2 != 0:
                start_position = line.split(' ')
                rover = {
                    'x': int(start_position[0]),
                    'y': int(start_position[1]),
                    'heading': start_position[2]
                }
            else:
                # Commands for the Rover instance.
                rover['commands'] = line
                inputs['rovers'].append(rover)

    return inputs


def deploy_rovers(inputs):
    """
    Create a new planet, with a plateau on which to deploy input rovers.
    :param inputs:
    :return:
    """
    # Get the length and width of the plateau
    length = inputs['plateau']['length']
    width = inputs['plateau']['width']
    
	# Get the list of rovers
    rovers = inputs['rovers']
    
	# Create a planet which will list all plateaus on the planet
    planet = models.Planet('Mars')
	
	# Create a plateau with the given length and width
    plateau = models.Plateau(length, width)
    
	# Add the plateau to the planet list of plateaus
    planet.add_plateau(plateau)
    
    for rover in rovers:
        # Create a new rover
        current_rover = models.Rover(rover['x'], rover['y'], rover['heading'])
        
        # Add the rover to the plateau		
        plateau.add_rover(current_rover)
        
        # Get the rover's commands		
        commands = rover['commands']
        for command in commands:
            # Command the rover
            current_rover.command_rover(command)
        print(current_rover.get_position())


def main():
    # Get the input file
    filename = sys.argv[1]

    # Format the input file contents into a dictionary
    inputs = format_input(filename)

    # Create planet, plateau, and deploy rovers based on inputs
    deploy_rovers(inputs)

if __name__ == '__main__':
    main()
