import pyray
from game.shared.point import Point
from game.casting.actor import Actor


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
        self._proxy_x1 = 0
        self._proxy_x2 = 0
        self._location = 0
        self._proxy_y1 = 0
        self._proxy_y2 = 0

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            self._proxy_x1 += 1
            if (self._proxy_x1 == 5):
                dx = -1
                self._proxy_x1 = 0
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            self._proxy_x2 += 1
            if (self._proxy_x2 == 5):
                dx = 1
                self._proxy_x2 = 0
        
        if pyray.is_key_down(pyray.KEY_UP):
            self._proxy_y1 += 1
            if self._proxy_y1 == 5:
                if self._location > 450:
                    dy = 0
                self._proxy_y1 = 0
           
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            self._proxy_y2 += 1
            if self._proxy_y2 == 5:
                if self._location < 570:
                    dy = 0
                self._proxy_y2 = 0
        
        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    def set_bottom(self, location):
        self._location = location