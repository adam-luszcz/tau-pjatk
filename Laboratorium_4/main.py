from app.game import Game
from pynput import keyboard

if __name__ == '__main__':
    game = Game()
    game.board.draw()

    with keyboard.Listener(on_release=game.on_press) as listener:
        listener.join()
