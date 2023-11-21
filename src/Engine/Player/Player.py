from src.Engine.Player.GUI.GUI import GUI, Board, GUIEnum
from src.Engine.Player.GUI.TerminalGUI import TerminalGUI





class Player:
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.ui = TerminalGUI()
        pass
    
    def display_board(self, board:Board):
        self.ui.display_board(board)
    