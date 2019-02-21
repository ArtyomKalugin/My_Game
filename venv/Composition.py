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
            elif level[y][x] == '.':
                Space((x, y))
    return x, y


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(platforms)
        self.image = pygame.Surface((20, 10))
        self.image.fill((100, 100, 100))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)


class Lemming(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(heroes)

        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))

        self.work = False
        self.x = 0

        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)
        self.vx = 1
        self.vy = 1

    def update(self, x):
        if len(pygame.sprite.spritecollide(self, platforms, False)) >= 3:
            self.vx = -self.vx

        if pygame.sprite.spritecollideany(self, finish):
            for elem in finish:
                elem.plus_winner()
            self.kill()
        elif pygame.sprite.spritecollideany(self, platforms):
            if self.work:
                self.x += x
                if self.x > 300:
                    self.x = 0
                    pygame.sprite.spritecollide(self, platforms, True)
            else:
                self.rect = self.rect.move(self.vx, 0)
        else:
            self.rect = self.rect.move(0, self.vy)
            if self.work:
                for q in spaces:
                    pos = q.give_pos()
                    if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1],
                                                                                            self.rect[1] + 20):
                        self.work = False

    def dig(self, pos):
        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_dig
            if to_dig:
                self.work = True
                to_dig = False


class Start(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(starts)
        self.pos = pos
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 20)

    def give_pos(self):
        return self.pos


class Finish(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(finish)
        self.pos = pos
        self.winners = 0
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 9.4 , 20, 20)

    def give_pos(self):
        return self.pos

    def plus_winner(self):
        self.winners += 1
        print(self.winners)


class Space(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(spaces)
        self.image = pygame.Surface((20, 10))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)

    def give_pos(self):
        return self.rect


class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(panel)
        self.image = load_image("menu.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500


class Dig(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(digger)
        self.image = load_image("Dig.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 515

    def update(self):
        if to_dig:
            self.rect.x = 90
            self.rect.y = 505
        else:
            self.rect.x = 100
            self.rect.y = 515


pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

platforms = pygame.sprite.Group()
heroes = pygame.sprite.Group()
starts = pygame.sprite.Group()
finish = pygame.sprite.Group()
spaces = pygame.sprite.Group()
panel = pygame.sprite.Group()
digger = pygame.sprite.Group()

Menu()
Dig()

heroes_count = 0

to_dig = False

x = 0
v = 100
fps = 60
time = 0
clock = pygame.time.Clock()

generate_level(load_level("Test.txt"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in heroes:
                sprite.dig(event.pos)

            if event.pos[0] in range(100, 200) and event.pos[1] in range(515, 595):
                if to_dig:
                    to_dig = False
                else:
                    to_dig = True

    screen.fill((0, 0, 0))
    x = v / fps
    time += x

    if time > 250:
        heroes_count += 1
        if heroes_count <= 10:
            for elem in starts:
                pos = elem.give_pos()
                Lemming(pos)
            time = 0

    heroes.update(x)
    digger.update()

    heroes.draw(screen)
    platforms.draw(screen)
    starts.draw(screen)
    finish.draw(screen)
    panel.draw(screen)
    digger.draw(screen)

    pygame.display.flip()
    clock.tick(fps)
