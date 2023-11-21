from src.Engine.Player.GUI.GUI import GUI, Board


class TerminalGUI(GUI):
    
    def __init__(self) -> None:
        pass
    
    
    def display_board(self, board:Board):
        txt_board = " " + "".join(["  " + file_name + " " for file_name in board.file_list]) + "\n"
        txt_board += " +" + "---+" * board.file_number + "\n"
        for rank in range(board.rank_number, 0, -1):
            txt_board += f"{rank}|" + "".join(["   |" for _ in range(board.file_number)]) + "\n"
            txt_board += " +" + "---+" * board.file_number + "\n"
        print(txt_board)