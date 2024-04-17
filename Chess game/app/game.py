from typing import Tuple, List, Optional
from fastapi import HTTPException
from .chess_pieces import ChessPiece, Rook, Knight, Bishop, Queen, King, Pawn, Color


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        for i in range(8):
            self.grid[6][i] = Pawn(Color.WHITE, (6, i))
            self.grid[1][i] = Pawn(Color.BLACK, (1, i))

        self.grid[0][0] = Rook(Color.BLACK, (0, 0))
        self.grid[0][7] = Rook(Color.BLACK, (0, 7))
        self.grid[7][0] = Rook(Color.WHITE, (7, 0))
        self.grid[7][7] = Rook(Color.WHITE, (7, 7))

        self.grid[0][1] = Knight(Color.BLACK, (0, 1))
        self.grid[0][6] = Knight(Color.BLACK, (0, 6))
        self.grid[7][1] = Knight(Color.WHITE, (7, 1))
        self.grid[7][6] = Knight(Color.WHITE, (7, 6))

        self.grid[0][2] = Bishop(Color.BLACK, (0, 2))
        self.grid[0][5] = Bishop(Color.BLACK, (0, 5))
        self.grid[7][2] = Bishop(Color.WHITE, (7, 2))
        self.grid[7][5] = Bishop(Color.WHITE, (7, 5))

        self.grid[0][3] = Queen(Color.BLACK, (0, 3))
        self.grid[7][3] = Queen(Color.WHITE, (7, 3))

        self.grid[0][4] = King(Color.BLACK, (0, 4))
        self.grid[7][4] = King(Color.WHITE, (7, 4))

    def display(self):

        print("Black")
        print("--0--1--2--3--4--5--6--7--")
        for i in range(0, 8):
            row = self.grid[i]
            row_str = '|'.join(self.get_piece_symbol(piece) if piece else ' ' for piece in row)
            print(f"{i}|" + row_str + '|')

        print("--0--1--2--3--4--5--6--7--")
        print("White\n")

    def get_piece_symbol(self, piece):
        if not piece:
            return ' '
        piece_symbols = {
            Rook: '♖',
            Knight: '♘',
            Bishop: '♗',
            Queen: '♕',
            King: '♔',
            Pawn: '♙',
        }
        return piece_symbols[type(piece)]

    def get_board(self) -> List[str]:
        rows = []
        rows.append("Black")
        rows.append("--0--1--2--3--4--5--6--7--")
        for i in range(0, 8):
            row = self.grid[i]
            row_str = '|'.join(self.get_piece_symbol(piece) if piece else ' ' for piece in row)
            rows.append(f"{i}|" + row_str + '|')
        rows.append("--0--1--2--3--4--5--6--7--")
        rows.append("White")
        return rows


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = Color.WHITE
        self.game_over = False
        self.saved_board = {}

    def start_game(self):
        self.board.setup_board()
        self.current_player = Color.WHITE
        self.game_over = False

    def end_game(self):
        self.game_over = True

    def move(self, player: Color, position_from: Tuple[int, int], position_to: Tuple[int, int]):
        if self.game_over:
            raise HTTPException(status_code=400, detail="Game over")

        if player != self.current_player:
            raise HTTPException(status_code=400, detail="Not your turn")

        piece = self.board.grid[position_from[0]][position_from[1]]

        if not piece or piece.color != player:
            raise HTTPException(status_code=400, detail="Invalid piece")

        if not self.is_valid_move(piece, position_from, position_to, self.board.grid):
            raise HTTPException(status_code=400, detail="Invalid move")

        self.board.grid[position_to[0]][position_to[1]] = piece
        self.board.grid[position_from[0]][position_from[1]] = None

        self.switch_player()
        self.saved_board = {(i, j): self.board.grid[i][j] for i in range(8) for j in range(8)}

    def is_valid_move(self, piece: ChessPiece, position_from: Tuple[int, int], position_to: Tuple[int, int],
                      board: List[List[Optional[ChessPiece]]]) -> bool:
        if isinstance(piece, Pawn):
            return piece.move(position_from, position_to, board)
        elif isinstance(piece, Rook):
            return piece.move(position_from, position_to, board)
        elif isinstance(piece, Knight):
            return piece.move(position_from, position_to, board)
        elif isinstance(piece, Bishop):
            return piece.move(position_from, position_to, board)
        elif isinstance(piece, Queen):
            return piece.move(position_from, position_to, board)
        elif isinstance(piece, King):
            return piece.move(position_from, position_to, board)

    def switch_player(self):
        if self.current_player == Color.WHITE:
            self.current_player = Color.BLACK
        else:
            self.current_player = Color.WHITE

    def get_board(self):
        return self.board.get_board()
