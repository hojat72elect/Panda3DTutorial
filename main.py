from panda3d.core import loadPrcFile
from direct.showbase.ShowBase import ShowBase


# extends the [ShowBase] class
class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        print(self.render)
        print(self.cam)
        print(self.camera)


if __name__ == '__main__':
    loadPrcFile("config/conf.prc")
    game = MyGame()
    game.run()
