from globals import *
from random import randint


class Pipe:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = w
        self.middle = randint(h*0.1 + pipe_gap/2, h*0.9 - pipe_gap/2)
        self.kill = False

        self.pipe_top = self.canvas.create_rectangle(self.x, 0, self.x + pipe_width, self.middle - pipe_gap/2, fill=pipe_color)
        self.pipe_bottom = self.canvas.create_rectangle(self.x, h, self.x + pipe_width, self.middle + pipe_gap/2, fill=pipe_color)

    def update(self):
        self.canvas.move(self.pipe_top, -pipe_speed, 0)
        self.canvas.move(self.pipe_bottom, -pipe_speed, 0)
        self.x = self.canvas.coords(self.pipe_top)[2]

    def death(self, bird):
        top = self.middle - pipe_gap/2 - death_forgiveness
        bottom = self.middle + pipe_gap/2 + death_forgiveness

        if (self.x - pipe_width + death_forgiveness*1.5) <= (bird.x + bird.size) and (self.x - death_forgiveness) >= bird.x:
            if bird.y <= top or (bird.y + bird.size) >= bottom:
                self.kill = True
