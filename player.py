from aabb import Aabb


class Actor:

    def __init__(self, x, y, width, height, sprite=None, color=None):
        self.aabb = Aabb(x, y, x+width, y+height)
        self.sprite = None

    def move(self,dx, dy):
        self.aabb.move(dx, dy)

class Player(Actor):

    def __init__(self, x, y, width, height, name, color='black', **kwargs):
        self.name = name
        self.color = color
        Actor.__init__(self, x, y, width, height)

