import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 80
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 3500
score = 0


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text(f"Score: {score}")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    banner.set_id("banner")
    cast.add_actor("banners", banner)
    
    # create the player (robot)
    x = int(MAX_X / 2)
    y = int(MAX_Y - 30)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    robot.set_id("robot")
    cast.add_actor("robots", robot)
    
    # create the artifacts
    for n in range(DEFAULT_ARTIFACTS):                
        char = [79] * 10 + [42] * 5 + [126] * 2 + [43] * 2
        rand = random.choice(char)
        text = rand

        #set the x (horizontal) position of the artifact
        x = random.randint(1, COLS - 1)
        #setting y position from negative allows artifacts to display before coming into view
        y = random.randint(-5000, 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # define the colors for the artifacts
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # set other attributes for the artifacts
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        
        if rand == 42:   
            artifact.set_id("add")
        elif rand == 43:  #3. add a new elif condition for new item on the list add +1, i.e. rand == 1, change to rand == 2
            artifact.set_id("bonus")  # choose a name to identify the bonus character
        elif rand == 126:
            artifact.set_id("snake")
        else:
            artifact.set_id("remove")
        
        # add artifacts to the screen
        cast.add_actor("artifacts", artifact)
    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()