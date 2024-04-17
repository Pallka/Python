from typing import Tuple, List, Optional
from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"


class ChessPiece(ABC):
    def __init__(self, color: Color, position: Tuple[int, int]):
        self.color = color
        self.position = position

    @abstractmethod
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.color}, {self.position})"


class Rook(ChessPiece):
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        if current_position[0] == new_position[0] or current_position[1] == new_position[1]:
            return True
        return False


class Knight(ChessPiece):
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        diff_x = abs(current_position[0] - new_position[0])
        diff_y = abs(current_position[1] - new_position[1])
        return (diff_x == 2 and diff_y == 1) or (diff_x == 1 and diff_y == 2)


class Bishop(ChessPiece):
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        diff_x = abs(current_position[0] - new_position[0])
        diff_y = abs(current_position[1] - new_position[1])
        return diff_x == diff_y


class Queen(ChessPiece):
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        return Rook().move(current_position, new_position, board) or Bishop().move(current_position, new_position, board)


class King(ChessPiece):
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        diff_x = abs(current_position[0] - new_position[0])
        diff_y = abs(current_position[1] - new_position[1])
        return diff_x <= 1 and diff_y <= 1


class Pawn(ChessPiece):
    def move(self, current_position: Tuple[int, int], new_position: Tuple[int, int], board) -> bool:
        row_from, col_from = current_position
        row_to, col_to = new_position

        direction = -1 if self.color == Color.WHITE else 1

        if col_from != col_to:
            if board[row_to][col_to] is None:
                return False
            if board[row_to][col_to].color == self.color:
                return False
            return True

        if col_from == col_to and board[row_to][col_to] is None:
            if row_to == row_from + direction:
                return True
            elif row_from in [1, 6] and row_to == row_from + 2 * direction and board[row_from + direction][col_from] is None:
                return True
        return False
