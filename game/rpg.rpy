init -10 python:
    import math

    chars = []

    min_bound = (0,0)
    max_bound = (1280,720)

    def WaitForInput():
        eri.follow(cam)
        #renpy.restart_interaction()


    class RPGCharacter(object):
        """docstring for RPGCharacter"""
        def __init__(self, speed = 1, pos = (0,0), radius = 64, img = None):
            super(RPGCharacter, self).__init__()
            self.x, self.y = pos
            self.speed = speed
            self.radius = radius
            self.img = img

        def move_toward(self, _x, _y):
            delta_x = other.x - _x
            delta_y = other.y - _y
            x, y = self.normalize(delta_x, delta_y)
            self.move(x * self.speed, y * self.speed, self.speed)

        def follow(self, other):
            self.move_toward(other.x, other.y)

        def normalize(self, x, y):
            length_sq = x*x + y*y
            length = math.sqrt(length_sq)
            return (x / length, y / length)

        def move(self, delta_x, delta_y, delta_length):
            old_x = self.x
            old_y = self.y
            self.x += delta_x
            self.y += delta_y
            for c in chars:
                dist = self.surface_dist(c)
                if c is not self and dist < 0:
                    d_x = c.x - self.x
                    d_y = c.y - self.y
                    x, y = self.normalize(d_x, d_y)
                    self.x += dist * x
                    self.y += dist * y
            backtrack = math.sqrt(self.dist2(old_x, old_y)) - delta_length
            if backtrack > 0:
                d_x = old_x - self.x
                d_y = old_y - self.y
                x, y = self.normalize(d_x, d_y)
                self.x += backtrack * x
                self.y += backtrack * y
            min_bx, min_by = min_bound
            if self.x < min_bx:
                self.x = min_bx
            if self.y < min_by:
                self.y = min_by
            max_bx, max_by = max_bound
            if self.x > max_bx:
                self.x = max_bx
            if self.y > max_by:
                self.y = max_by


        def dist2(self, x, y):
            delta_x = x - self.x
            delta_y = y - self.y
            return delta_x*delta_x + delta_y*delta_y

        def dist(self, other):
            delta_length_sq = self.dist2(other.x, other.y)
            return  math.sqrt(delta_length_sq)

        def surface_dist(self, other):
            dist = self.dist(other)
            return dist - self.radius - other.radius



screen rpg_view(bg):
    #xminimum bg.width
    #yminimum bg.height
    add bg

    for char in chars:
        add char.img:
            xpos char.x
            ypos char.y
            xanchor 0.5
            yanchor 0.5
