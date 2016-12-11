from globals import *


class Bird:

    def __init__(self, canvas):
        self.canvas = canvas

        self.size = h * bird_size
        self.y = h / 2 - self.size/2
        self.x = w * 0.1

        self.gravity = gravity
        self.lift = bird_lift
        self.velocity = 0
        self.thisbird = self.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size*0.85, fill=birdcolor)

    def update(self):
        self.velocity += self.gravity
        self.y = self.canvas.coords(self.thisbird)[1]

        # Fix to top speeds
        self.velocity = min([self.velocity, maxvelocity * fall_multiplier])
        self.velocity = max([self.velocity, -maxvelocity])

        if self.y < (h - self.size):
            self.canvas.move(self.thisbird, 0, self.velocity)
        else:
            self.velocity = 0

        self.canvas.update()
