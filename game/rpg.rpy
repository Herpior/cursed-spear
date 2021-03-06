init -10 python:
    import math
    import pygame

    chars = []

    min_bound = (0,0)
    max_bound = (1280,720)

    def WaitForInput():
        #x, y = pygame.mouse.get_pos()
        x, y = renpy.get_mouse_pos()
        eri.move_toward(x, y)
        #renpy.restart_interaction()

    def check_deaths(killer, targets):
        deaths = []
        for target in targets:
            if killer.surface_dist(target) < 32:
                deaths.append(target)
        return deaths

    def isMousePressed():
        return sum(pygame.mouse.get_pressed()) > 0

    def update():
        for char in chars:
            if(char.img is not None):
                renpy.show(char.img, at_list = [charpos(int(char.x), int(char.y))], zorder = int(char.y))

    class AnimationAt(renpy.Displayable):
        """
        docstring for AnimationAt
        I use hacky ways to render the characters during rpg segments,
        renpy doesn't exactly like it, so it breaks default animations.
        using at instead of st for setting the frames is a hacky way
        to go around the problems caused by the other hacky solutions
        """
        def __init__(self, frames):
            super(AnimationAt, self).__init__()
            #self.mouse_coords = mouse_coords
            self.frames = [Image(frames[i]) for i in range(len(frames))]

        def render(self, width, height, st, at):
            #print(st, at)
            t = Transform(self.frames[int(12 * (at % 0.5))])
            child_render = renpy.render(t, width, height, st, at)
            cw, ch = child_render.get_size()
            rv = renpy.Render(cw, ch)
            rv.blit(child_render, (0,0))
            return rv

        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return self.frames

    class BooleanContainer(object):
        """docstring for BooleanContainer"""
        def __init__(self, initial_value = False):
            super(BooleanContainer, self).__init__()
            self.bool = initial_value


    class RPGCharacter(object):
        """docstring for RPGCharacter"""
        def __init__(self, speed = 1, pos = (0,0), radius = 64, img = None):
            super(RPGCharacter, self).__init__()
            self.x, self.y = pos
            self.speed = speed
            self.radius = radius
            self.img = img
            self.dir = "front"

        def set_dir(self, delta_x, delta_y):
            if delta_y >= 0:
                self.dir = "front"
            else:
                self.dir = "back"

        def dir_to(self, other):
            delta_x = other.x - self.x
            delta_y = other.y - self.y
            return math.atan2(delta_y, delta_x)*180/math.pi - 90

        def move_toward(self, _x, _y):
            #print("mouse pos", _x, _y)
            delta_x = _x - self.x
            delta_y = _y - self.y
            #print("delta", delta_x, delta_y)
            if(delta_x == 0 and delta_y == 0):
                return
            x, y = self.normalize(delta_x, delta_y)
            #print("normalized", x, y)
            if abs(x * self.speed) > abs(delta_x):
                x = delta_x
            else:
                x = x * self.speed

            if abs(y * self.speed) > abs(delta_y):
                y = delta_y
            else:
                y = y * self.speed

            self.move(x, y, self.speed)

        def follow(self, other):
            self.move_toward(other.x, other.y)

        def run_from(self, other):
            delta_x = other.x - self.x
            delta_y = other.y - self.y
            self.move_toward(self.x - delta_x, self.y - delta_y)

        def normalize(self, x, y):
            length_sq = (x*x) + (y*y)
            _length = math.sqrt(length_sq)
            if _length == 0:
                return (x, y)
            return (x / _length, y / _length)

        def move(self, delta_x, delta_y, delta_length):
            self.set_dir(delta_x, delta_y)
            #print("original pos", self.x, self.y)
            old_x = self.x
            old_y = self.y
            self.x += delta_x
            self.y += delta_y
            #print("target pos", self.x, self.y)
            for c in chars:
                dist = self.surface_dist(c)
                if c is not self and dist < 0:
                    d_x = c.x - self.x
                    d_y = c.y - self.y
                    x, y = self.normalize(d_x, d_y)
                    self.x += dist * x
                    self.y += dist * y
            #print("changed pos", self.x, self.y)
            backtrack = math.sqrt(self.dist2(old_x, old_y)) - delta_length
            if backtrack > 0:
                d_x = old_x - self.x
                d_y = old_y - self.y
                x, y = self.normalize(d_x, d_y)
                self.x += backtrack * x
                self.y += backtrack * y
            #print("backtracked pos", self.x, self.y)
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
            #print("bound pos", self.x, self.y)


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

    class MouseTracker(renpy.Displayable):
        """docstring for MouseTracker"""
        def __init__(self, bc):
            super(MouseTracker, self).__init__()
            #self.mouse_coords = mouse_coords
            self.bc = bc

        def render(self, width, height, st, at):
            return renpy.Render(0,0)

        def event(self, ev, x, y, st):
            #print("event checked", self.mouse_coords.x, self.mouse_coords.y, x, y)
            #self.mouse_coords.x = x
            #self.mouse_coords.y = y
            print(bc.bool)
            if ev.type == pygame.MOUSEBUTTONUP:
                print("mouse up")
                bc.bool = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print("mouse down")
                bc.bool = True

        def visit(self):
            return []

screen mouse_tracker(bc):
    add MouseTracker(bc)

screen rpg_view(bg):
    add bg

    for char in chars:
        add char.img:
            xpos char.x
            ypos char.y
            xanchor 0.5
            yanchor 0.5
