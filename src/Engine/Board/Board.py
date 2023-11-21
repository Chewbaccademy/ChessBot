from src.Engine.Board.Square import Square, SquareCollection
from src.utils import get_letter_by_alphabet_rank

class Board:
    """
        Board:
        Class representing the whole chess board
        Useful to interact with board and board contents (like squares, ranks, etc.)
    """
    def __init__(self, rank_number:int = 8, file_number:int = 8) -> None:
        print("Board Initialization ...", end="\r")
        self.rank_number = rank_number
        self.file_number = file_number
        
        self.square_list = SquareCollection(dims=(self.rank_number, self.file_number))
        for i in range(self.rank_number):
            for j in range(self.file_number):
                self.square_list.append(Square(i, j))
                
        self.file_list = [get_letter_by_alphabet_rank(i) for i in range(self.file_number)]
                
                
        print("Board Initialization [OK]")
        
    def get_rank_by_id(self, id:int) -> SquareCollection:
        return self.square_list.get_rank_by_id(id)
    
    def __str__(self) -> str:
        return f"Board: {self.rank_number}x{self.file_number} : {self.square_list}"