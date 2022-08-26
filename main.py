from direct.showbase.ShowBase import ShowBase


# extends the [ShowBase] class
class MyGame(ShowBase):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    game = MyGame()
    game.run()
