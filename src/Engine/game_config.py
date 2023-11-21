

class BASE_GAME_CONFIG:
    
    rank_number = 8
    file_number = 8
    
    def __init__(self) -> None:
        pass
    
    
class GameConfig:
    
    def __init__(self, rank_number:int = None, file_number:int = None, **game_config) -> None:
        self.__dict__.update(**game_config)
        args = locals()
        for variable in args:
            self.__set_parameters_config(variable, args[variable])
        
        
    def __set_parameters_config(self, param_name, param):
        if param is not None:
            self.__dict__.update(**{param_name: param})
        elif not hasattr(self, param_name) or getattr(self, param_name) is None:
            self.__dict__.update(**{param_name: getattr(BASE_GAME_CONFIG, param_name)})