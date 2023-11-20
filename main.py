from src.Engine.Board.Board import Board



if __name__ == '__main__':
    print("Starting ...")
    board = Board()
    print(board)
    print(board.get_row_by_id(0))
    print(board.get_row_by_id(5))