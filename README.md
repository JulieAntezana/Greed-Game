# cse210-04

Repository for Greed game Team-j-12pm
Greed

He who is not contented with what he has, would not be contented with what he would like to have.

Socrates -
Overview Greed is a game in which the Actor seeks to gather as many falling Artifacts as possible. The game continues as long as the Actor wants more!

Rules Greed is played according to the following rules.

Artifacts such as gems (\*), bonus (+), rocks (o), and snakes (~) randomly appear and fall from the top of the screen. The Actor (#) can move left or right along the bottom of the screen. If the Actor touches a gem they earn a point. If the Actor touches a rock they lose a point. The bonus (+) earns 5 points. The snakes take away 5 points. All artifacts are removed when the Actor touches them. The game continues until the Actor closes the window.

Getting Started
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

python3 -m pip install raylib
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 main.py

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure

---

The project files and folders are organized as follows:
root (project root folder) +-- greed (source code for game) +-- data (data files for game) +-- game (specific game classes) +-- main.py (entry point for program) +-- README.md (general info)

## Required Technologies

---

- Python 3.8.0
- Raylib Python CFFI 3.7

## Authors

Marcus Ayodeji Ojo-Osasere
Julie Antezana
Rune Larsen

Game Design Details

class Director:
This class is responsible for controlling the game

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.

class Score:
This class handles the scoring system. It has methods like add_score and get_score
Attributes:
\_score (int): This is the current score the user has
-gem: + 1
-plus sign: + 5
-rock: - 1
-snake: - 5

class Point:
A distance from a relative origin (0, 0). This would enable drawings of the shapes to be made

    The responsibility of Point is to hold and provide information about itself.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.

class Colors:
The color class returns the colors needed to be applied to the shapes
Attributes:
\_red (int): The red value.
\_green (int): The green value.
\_blue (int): The blue value.
\_alpha (int): The alpha or opacity.
"""
class Cast:
"""A collection of actors.
The responsibility of a cast is to keep track of a collection of actors. It has methods
for adding, removing and getting them by a group name.
Attributes:
\_actors (dict): A dictionary of actors

class Actor:
"""A visible, moveable shape that participates in the game.

    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d.
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

class Artifacts:
A child to the parent class Actor, are visible, randomly generated moving rocks, gems, plus signs, or snakes that move from the top of the screen to the bottom of the screen. The responsibility of Artifacts is to keep track of its appearance, position and velocity in 2d.

    Attributes:
        Gem, Bonus, Rock, or Snake
    Inherited from Actor
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.

class VideoService:
Outputs the game state. The responsibility of the class of objects is to draw the game
state on the screen.

    Attributes:
        _caption (str): the caption above the screen
        _width (int): the video screen's width
        _height (int): the video screen's height
        _cell_size (int): the size of the video screen's cell.
        _frame_rate (int): the number of frames per second.
        _debug (bool): whether or not to draw in debug mode.

class KeyboardService:
Detects Actor input.

    The responsibility of a KeyboardService is to detect Actor key presses and translate them into a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
