import pygame as pg
from math import sin, cos, e


class PygameWindow:

    def __init__(self, commonResourse):
        self.resourse = commonResourse

        pg.init()

        self.font = pg.font.SysFont('Comic Sans MS', 24)

        self.screen = pg.display.set_mode([800, 800], pg.RESIZABLE)

        self.clock = pg.time.Clock()
        self.running = True

        self.BLACK, self.WHITE, self.GRAY, self.GREEN = [0] * 3, [255] * 3, [100] * 3, [0, 255, 0]
        self.RESOLUTION = 100
        self.QUALITY = 10000
        self.time = 0

    def text(self, text, x, y):
        text_surf = self.font.render(text, False, self.WHITE)
        self.screen.blit(text_surf, (x+3, y))

    def run(self):
        while self.running and not self.resourse.terminate:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                if event.type == pg.MOUSEWHEEL:
                    self.RESOLUTION *= .97 ** -event.y

            WIDTH, HEIGHT = self.screen.get_width(), self.screen.get_height()

            self.screen.fill(self.BLACK)

            if self.resourse.mode == 0:
                for i in range(int(HEIGHT/2/self.RESOLUTION)):
                    y = (i + 1)*self.RESOLUTION
                    pg.draw.line(self.screen, self.GRAY, [0, HEIGHT/2 + y], [WIDTH, HEIGHT/2 + y])
                    pg.draw.line(self.screen, self.GRAY, [0, HEIGHT/2 - y], [WIDTH, HEIGHT/2 - y])
                for i in range(int(WIDTH/2/self.RESOLUTION)):
                    x = (i + 1)*self.RESOLUTION
                    pg.draw.line(self.screen, self.GRAY, [WIDTH/2 + x, 0], [WIDTH/2 + x, HEIGHT])
                    pg.draw.line(self.screen, self.GRAY, [WIDTH/2 - x, 0], [WIDTH/2 - x, HEIGHT])
            else:
                for i in range(int((WIDTH**2 + HEIGHT**2)**.5 / 2 / self.RESOLUTION)):
                    r = (i + 1)*self.RESOLUTION
                    pg.draw.circle(self.screen, self.GRAY, [WIDTH/2, HEIGHT/2], r, 1)

            pg.draw.line(self.screen, self.WHITE, [0, HEIGHT/2], [WIDTH, HEIGHT/2], 2)
            pg.draw.line(self.screen, self.WHITE, [WIDTH/2, 0], [WIDTH/2, HEIGHT], 2)

            a, b, length = self.resourse.a, self.resourse.b, self.resourse.length
            px, py = 0, 0

            for i in range(self.QUALITY):
                t = (i/self.QUALITY - .5) * length
                x = WIDTH/2 + self.RESOLUTION * cos(t) * a * e ** (b * t)
                y = HEIGHT/2 - self.RESOLUTION * sin(t) * a * e ** (b * t)
                if i > 0:
                    pg.draw.line(self.screen, self.WHITE, [px, py], [x, y])
                px, py = x, y

            if a != 0:
                t = ((self.time / self.QUALITY) % 1 - .5) * length
                x = WIDTH/2 + self.RESOLUTION * cos(t) * a * e ** (b * t)
                y = HEIGHT/2 - self.RESOLUTION * sin(t) * a * e ** (b * t)
                size = 6
                pg.draw.rect(self.screen, self.GREEN, [x - size, y - size, size*2, size*2])
                self.time += self.resourse.speed
            else:
                self.time = 0

            self.text('0', WIDTH/2, HEIGHT/2)
            self.text('1', WIDTH/2 + self.RESOLUTION, HEIGHT/2)
            self.text('1', WIDTH/2, HEIGHT/2 - self.RESOLUTION)
            self.text('y', WIDTH/2, 0)
            self.text('x', WIDTH - 30, HEIGHT/2)

            pg.display.flip()
            self.clock.tick(60)

        self.resourse.terminate = True
        pg.quit()
