from src.utils import get_letter_by_alphabet_rank, is_integer
from src.utils import math

class Square:
    """
        Board:
        Class representing a square in the chess board
    """
    def __init__(self, rank_id:int, file_id:int) -> None:
        self.rank_id = rank_id
        self.file_id = file_id
        self.rank_name = str(rank_id+1)
        self.file_name = get_letter_by_alphabet_rank(file_id)
        self.name = self.file_name + self.rank_name
    
    def __str__(self) -> str:
        return self.name
    
    
class SquareCollection:
    
    def __init__(self, square_list:list[Square] = [], dims:tuple = None) -> None:
        self.square_list = square_list
        self.dims = dims
        
    def append(self, square:Square):
        self.square_list.append(square)
        
    def __str__(self) -> str:
        return "SquareCollection[" + ", ".join([square.name for square in self.square_list]) + "]"
    
    def get_rank_by_id(self, id:int):
        if self.dims is not None:
            nb_files = self.dims[1]
        else:
            # if dims are not set, we assume the collection represent a squared board
            nb_files = math.sqrt(len(self.square_list))
            if not is_integer(nb_files):
                raise ValueError("If the collection is not a squared board, the dimensions must be set")
            
        return SquareCollection(self.square_list[id * nb_files : id * nb_files + nb_files], (1, nb_files))
    
    def __getitem__(self, index:int|tuple) -> Square:
        if isinstance(index, int):
            return self.get_rank_by_id(index)
        
        elif isinstance(index, tuple):
            ret_value = SquareCollection()
            for i in range(index[0], index[1], index[2]):
                ret_value += self.get_rank_by_id(i)
            return ret_value
                
            
        raise ValueError("The index must be an integer or a slice when used like SquareCollection[index]")
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return SquareCollection(self.square_list + other.square_list)
        
        raise ValueError(f"Cannot use the operator + between a SquareCollection and a {type(other)}")
        