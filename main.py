from threading import Thread
from pygame.time import Clock

from CommonResource import CommonResource
from PygameWindow import PygameWindow
from TKinterWindow import TKinterWindow


class Main:

    def __init__(self):
        self.resource = CommonResource()
        self.clock = Clock()

        self.pgThread = None
        self.tkThread = None

    def runTK(self):
        w = TKinterWindow(self.resource)
        w.run()

    def runPG(self):
        w = PygameWindow(self.resource)
        w.run()

    def run(self):
        self.tkThread = Thread(target=self.runTK, args=())
        self.pgThread = Thread(target=self.runPG, args=())

        self.tkThread.start()
        self.pgThread.start()

        while not self.resource.terminate:
            self.clock.tick(60)


if __name__ == '__main__':
    m = Main()
    m.run()
