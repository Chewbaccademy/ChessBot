# all libraries import are done here
import math


def get_letter_by_alphabet_rank(letter_rank:int, get_maj_letter:bool = False):
    if 0 <= letter_rank <= 25:
        if get_maj_letter:
            return chr(ord('A') + letter_rank)
        else:
            return chr(ord('a') + letter_rank)
    
    raise ValueError("Letter rank must be between 0 and 25")


def is_integer(x:any) -> bool:
    try:
        _ = int(x)
    except ValueError:
        return False
    
    return True