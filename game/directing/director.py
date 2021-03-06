from turtle import pos
from game.casting.actor import Actor
from game.shared.score import Score
from game.shared.point import Point



class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = Score()
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        position = robot.get_position().get_y()
        self._keyboard_service.set_bottom(position)
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts. 
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")


        banner.set_text("Score: " + str(self.score.get_score()))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        banner.set_text("Score: " + str(self.score.get_score()))
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                if artifact.get_id() == "add":
                    self.score.add_score(1)
                    artifact.set_position(Point(max_x, max_y))
                elif artifact.get_id() == "bonus": 
                    self.score.add_score(5) 
                    artifact.set_position(Point(max_x, max_y))
                elif artifact.get_id() == "snake":
                    self.score.remove_score(5)
                    artifact.set_position(Point(max_x, max_y)) 
                else:
                    self.score.remove_score(1)
                    artifact.set_position(Point(max_x, max_y))
            
                # if artifact.get_position() < max_y:
                #     self._artifact.remove(artifact)

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        