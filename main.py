from game import Game
from hud import HUD

def main():
    # Cria o objeto game e chama o loop básico
    game = Game("resolution", "fullscreen")
    game.loop()
# main()

# Chama a função main
if __name__ == '__main__':
    main()