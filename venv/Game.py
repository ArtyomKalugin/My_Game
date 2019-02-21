import pygame
import os
import sys


def load_level(filename):
    try:
        filename = "data/" + filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        max_width = max(map(len, level_map))

        return list(map(lambda x: x.ljust(max_width, '.'), level_map))
    except Exception as message:
        print('Cannot load file:', filename)
        raise SystemExit(message)


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Platform((x, y))
            elif level[y][x] == '1':
                Start((x, y))
            elif level[y][x] == '2':
                Finish((x, y))
    return x, y


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(platforms)
        self.image = pygame.Surface((20, 20))
        self.image.fill((100, 100, 100))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)


class Lemming(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(heroes)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)
        self.vx = 1
        self.vy = 1

    def update(self):
        if len(pygame.sprite.spritecollide(self, platforms, False)) == 3:
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, finish):
            for elem in finish:
                elem.plus_winner()
            self.kill()
        elif pygame.sprite.spritecollideany(self, platforms):
            self.rect = self.rect.move(self.vx, 0)
        else:
            self.rect = self.rect.move(0, self.vy)


class Start(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(starts)
        self.pos = pos
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)

    def give_pos(self):
        return self.pos


class Finish(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(finish)
        self.pos = pos
        self.winners = 0
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)

    def give_pos(self):
        return self.pos

    def plus_winner(self):
        self.winners += 1
        print(self.winners)


pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

platforms = pygame.sprite.Group()
heroes = pygame.sprite.Group()
starts = pygame.sprite.Group()
finish = pygame.sprite.Group()

y = 0
v = 100
fps = 60
time = 0
clock = pygame.time.Clock()

generate_level(load_level("Test.txt"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    screen.fill((0, 0, 0))
    y = v / fps
    time += y
    if time > 300 and len(heroes) <= 9:
        for elem in starts:
            pos = elem.give_pos()
            Lemming(pos)
        time = 0

    heroes.update()

    heroes.draw(screen)
    platforms.draw(screen)
    starts.draw(screen)
    finish.draw(screen)

    pygame.display.flip()
    clock.tick(fps)
