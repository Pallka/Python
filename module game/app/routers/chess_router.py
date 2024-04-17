from fastapi import APIRouter
from app.game import Game
from app.chess_pieces import Color

router = APIRouter(tags=["Chess game"])
game = Game()


@router.post("/start/")
def start_game():
    game.start_game()
    return {"message": "Game started"}


@router.post("/move/")
def move(player: str, from_row: int, from_col: int, to_row: int, to_col: int):
    color = Color.WHITE if player == "white" else Color.BLACK
    position_from = (from_row, from_col)
    position_to = (to_row, to_col)
    game.move(color, position_from, position_to)
    return {"message": "Move made"}


@router.get("/board/")
def get_board():
    board = game.get_board()
    return {"board": board}


@router.post("/end/")
def end_game():
    game.end_game()
    return {"message": "Game ended"}
