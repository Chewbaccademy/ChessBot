from pandas import DataFrame, np
from utils import File



class Dataset:
    
    __pieces = ["K", "Q", "R", "B", "C", "P", "k", "q", "r", "b", "c", "p"]
    __rank = [1, 2, 3, 4, 5, 6, 7, 8]
    __files = ["a", "b", "c", "d", "e", "f", "g", "h"]
    __data = None
    
    
    @property
    def data(self):
        return self.__data
    
    def __init__(self) -> None:
        self.__init_dataframe()
    
    def __init_dataframe(self):
        columns = self.__generate_columns()
        self.__data = DataFrame(np.empty((0, len(columns))))
        self.data.columns = columns
    
    def __generate_columns(self) -> list:
        # add one column to check for each piece in each square
        cols = []
        for p in self.__pieces:
            for r in self.__rank:
                for f in self.__files:
                    cols.append(f"is_{p}_in_{f}{r}")
                    
        # add other FEN information
        cols.append('is_white_turn')
        cols.append('can_k_castle')
        cols.append('can_q_castle')
        cols.append('can_K_castle')
        cols.append('can_Q_castle')
        cols.append('number_of_en_passant_possible')
        cols += self.__generate_en_passant_columns()
        cols.append('halfmoves_since_non_reversible_move')
        cols.append('number_of_moves')
        
        return cols
    
    def __generate_en_passant_columns(self):
        ep_cols = []
        
        for r in self.__rank:
            for f in self.__files:
                ep_cols.append(f"is_en_passant_in_{f}{r}")
                
        return ep_cols
    
    def get_line_from_fen(self, fen:str):
        
        line = dict()
        
        
        fen_parts = fen.split(' ')
        # get board information
        board = fen_parts.pop(0)
        ranks = board.split('/')
        
        for rank in ranks:
            for info in rank:
                pass