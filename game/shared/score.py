class Score:
    """The Score class is responsible for keeping track of the score in the game.
    
        Attributes: Self_score
        
        Methods:
            Add_score: adds 1 to the score
            remove_score: removes 1 from the score
            get_score: returns the current score"""
    
    def __init__(self):
        
        self._score = 0
        
    def add_score(self): 
        self._score += 1
        
    def remove_score(self): 
        self._score -= 1
        
    def get_score(self):
        return self._score