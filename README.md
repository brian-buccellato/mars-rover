# Mars Rover Application
The Mars Rover application reads a file which defines a plateau to be explored (cartesian coordinate plane), and a starting point (cartesian coordinates and cardinal direction) and set of  navigation commands for each rover exploring the plateau.  Each rover is deployed sequentially.  The application outputs the final location of each rover deployed.

# Requirements
* Python 2.7

# Instructions
* To run application run in command line  "path to folder containing files" python main.py input.txt
* To run tests in command line "path to folder containing files" python tests.py
* To run alternative input files, create a .txt file in the same directory and run  "path to folder containing files" python main.py "your custom input file name".txt

# Input File Format
The acceptable input file format is as follows:

5 5 

1 1 N 

MLR

line 1: two integers which define the top right cordinates of the plateau, ie the Northeast corner.  Only One plateau is currently permitted
line 2: the first integer is the x starting position, second is the y starting position, the character defines the rovers direction
line 3: sequence of commands for the rover.  M- move one space in the direction the rover is facing.  R- Rotate the rover 90 degrees to the right.  L- Rotate the rover 90 degrees to the left.
Any number of rovers are currently permitted per plateau.  To add more rovers simply add additional versions of the described line 2 and line 3.

#Additional Work
Extend functionality to not allow two rovers to occupy the same spot or roam off the plateau.  Incorporate functionality to construct galaxies, universes, dimensions??? :).  
