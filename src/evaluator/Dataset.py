from pandas import DataFrame, np



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
        cols = []
        for p in self.__pieces:
            for r in self.__rank:
                for f in self.__files:
                    cols.append(f"is_{p}_in_{f}{r}")
        return cols