from fastapi import FastAPI
import uvicorn
from app.game import Game
from http.client import HTTPException
from app.routers.chess_router import router
app = FastAPI()
app.include_router(router)


def main():
    game = Game()
    game.start_game()

    print("Initial board state:")
    game.board.display()

    while not game.game_over:
        print(f"Current player: {game.current_player.name}")
        position_from = tuple(map(int, input("Enter position from: ").strip().split()))
        position_to = tuple(map(int, input("Enter position to: ").strip().split()))

        try:
            game.move(player=game.current_player, position_from=position_from, position_to=position_to)
            game.board.display()

        except HTTPException as e:
            print(e.detail)

    print("Game over!")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # main()
