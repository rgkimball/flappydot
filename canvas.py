# FlappyDot
# rgkimball | 2016/12/11

from __future__ import division
from Tkinter import Tk, Canvas, Frame, BOTH
from globals import *
from bird import Bird
from pipe import Pipe
from time import sleep


class Flappy(Frame):

    def __init__(self, parent):
        self.root = Frame.__init__(self, parent)

        self.bg = "#222"
        self.parent = parent
        self.canvas = Canvas(self)
        self.pipes = []
        self.hiscore = 0

        self.setup()

    # Bind the keypress to move the bird object
    def keypress(self, v):
        self.bird.velocity -= self.bird.gravity * self.bird.lift

    def killall(self):
        self.pipes = []
        self.hiscore = max([self.hiscore, self.score])
        self.canvas.delete("all")

        self.newgame()

    # build frame & objects
    def setup(self):
        self.parent.title("Fappy")
        self.pack(fill=BOTH, expand=1)

        # Bind spacebar to keypress function
        self.parent.bind_all("<space>", self.keypress)
        self.canvas.pack(fill=BOTH, expand=1)

        size = str(w) + "x" + str(h)

        self.parent.geometry(size)

        self.newgame()

        self.parent.mainloop()

    def newgame(self):

        # Create bg object
        self.canvas.create_rectangle(0, 0, w, h, fill=self.bg, outline=self.bg)

        # Init bird object
        self.bird = Bird(self.canvas)

        self.score = 0

        self.scoreobj = self.canvas.create_text(w/2, h * 0.3, fill="yellow", font="Courier 30 bold", text=self.score)
        self.hiscoreobj = self.canvas.create_text(85, 20, fill="yellow", font="Courier 14", text="HIGH SCORE: %d" % self.hiscore)

        fcount = 0
        while 1:
            sleep(1/framerate)
            fcount += 1

            # if frame count is divisible by 90, make a pipe
            if fcount % pipe_frequency == 0:
                self.pipes.insert(0, Pipe(self.canvas))
            if fcount > 60:
                self.update()

    def update(self):
        self.bird.update()

        if self.bird.y + self.bird.size > h:
            self.killall()

        for pipe in self.pipes:
            pipe.update()

            # check death condition
            pipe.death(self.bird)

            if pipe.kill:
                self.killall()

            # If the pipe goes off the screen, remove it from the list
            if pipe.x < 0:
                self.score += 1
                self.canvas.itemconfigure(self.scoreobj, text=self.score)
                self.pipes.remove(pipe)


def main():
    root = Tk()
    run = Flappy(root)

if __name__ == '__main__':
    main()
