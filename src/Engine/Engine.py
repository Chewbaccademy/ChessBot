from src.Engine.Board.Board import Board, SquareCollection
from src.Engine.game_config import GameConfig
from src.Engine.Player.Player import Player



class Engine:
    
    def __init__(self, players_config:list, game_config:dict = {}) -> None:
        self.game_config = GameConfig(**game_config)
        self.players = [Player(**p) for p in players_config]
        self.board = Board(self.game_config.rank_number, self.game_config.file_number)
        
        
    def game(self):
        self.players[0].display_board(self.board)
        
    
        