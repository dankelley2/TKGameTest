
class Aabb:
    def __init__(self, x, y, mx, my):

        self.x = x
        self.y = y
        self.mx = mx
        self.my = my

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.mx += dx
        self.my += dy
