

class File:
    
    __files = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    def __init__(self, string_file=None, integer_file=None) -> None:
        if string_file is not None:
            self.string_file = string_file
            self.int_file = File.get_int_from_string(string_file)
            
        elif integer_file is not None:
            self.integer_file = integer_file
            self.string_file = File.self.get_string_from_integer(integer_file)
            
        else:
            raise ValueError("Invalid file: string_file or integer_file must be specified")
        
    @classmethod
    def get_string_from_integer(integer:int):
        return File.__files[integer]
    
    @classmethod
    def get_int_from_string(string_file:str):
        return File.__files.index(string_file)
    
    