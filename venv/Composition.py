import pygame
import os
import sys


def play_level_first():
    global time_first, timing, heroes_count

    if time_first > 0:
        screen.fill((0, 0, 0))
        x = v / fps
        timing += x

        if timing > 250:
            heroes_count += 1
            if heroes_count <= 10:
                for elem in starts:
                    pos = elem.give_pos()
                    Lemming(pos)
                timing = 0

        heroes.update(x)
        digger.update()
        booms.update()
        parachutes.update()
        hinders.update()

        time_first -= 0.01

        all_sprites.draw(screen)

        draw_count()
        show_time(int(time_first))

        pygame.display.flip()
        clock.tick(fps)

        if to_boom:
            for sprites in heroes:
                sprites.kill()
                heroes_count = 10

        if len(heroes) == 0:
            for elems in finish:
                if elems.show_winners() > 0:
                    for sprite in all_sprites:
                        return True
    else:
        terminate()


def play_level_second():
    open_level_second()

    global time_first, timing, heroes_count

    if time_first > 0:
        screen.fill((0, 0, 0))
        x = v / fps
        timing += x

        if timing > 250:
            heroes_count += 1
            if heroes_count <= 10:
                for elem in starts:
                    pos = elem.give_pos()
                    Lemming(pos)
                timing = 0

        heroes.update(x)
        digger.update()
        booms.update()
        parachutes.update()
        hinders.update()

        time_first -= 0.01

        all_sprites.draw(screen)

        draw_count()
        show_time(int(time_first))

        pygame.display.flip()
        clock.tick(fps)

        if to_boom:
            for sprites in heroes:
                sprites.kill()
                heroes_count = 10
    else:
        terminate()


def open_level_first():
    generate_level(load_level("Level_1.txt"))


def open_level_second():
    generate_level(load_level("Level_2.txt"))


def load_level(filename):
    try:
        filename = "data/" + filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        max_width = max(map(len, level_map))

        return list(map(lambda x: x.ljust(max_width, '/'), level_map))
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
                Platform((x, y), 'default')
            elif level[y][x] == '1':
                Start((x, y))
            elif level[y][x] == '2':
                Finish((x, y))
            elif level[y][x] == '.':
                Space((x, y))
            elif level[y][x] == '@':
                Grass((x, y))
            elif level[y][x] == '/':
                Nothing((x, y))
    return x, y


def draw_count():
    for f in finish:
        count = f.show_outers()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 50)

        text_out = font.render('OUT ' + str(10 - count), 1, (100, 255, 100))
        text_out_x = 250
        text_out_y = 450
        screen.blit(text_out, (text_out_x, text_out_y))

        text_in = font.render('IN ' + str(count * 10) + '%', 1, (100, 255, 100))
        text_in_x = 500
        text_in_y = 450
        screen.blit(text_in, (text_in_x, text_in_y))

    for d in digger:
        count = d.give_count()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
        text = font.render(count, 1, (100, 255, 100))

        text_x = 130
        text_y = 570

        screen.blit(text, (text_x, text_y))

    for p in parachutes:
        count = p.give_count()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
        text = font.render(count, 1, (100, 255, 100))

        text_x = 230
        text_y = 570

        screen.blit(text, (text_x, text_y))

    for h in hinders:
        count = h.give_count()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
        text = font.render(count, 1, (100, 255, 100))

        text_x = 330
        text_y = 570

        screen.blit(text, (text_x, text_y))


def show_time(time):
    font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 50)
    text = font.render('TIME ' + str(time), 1, (100, 255, 100))

    text_x = 10
    text_y = 450

    screen.blit(text, (text_x, text_y))


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos, name):
        super().__init__(platforms, all_sprites)
        if name == 'default':
            self.image = pygame.Surface((20, 10))
            self.image.fill((65, 25, 0))
            self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)
        elif name == 'hinder':
            self.image = pygame.Surface((20, 20))
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(pos[0], pos[1], 20, 20)


class Lemming(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(heroes, all_sprites)

        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))

        self.work = False
        self.ground = False
        self.parach = False
        self.parach_used = False
        self.ground_kill = False
        self.hinder = False
        self.distance = 0
        self.x = 0

        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)
        self.vx = 1
        self.vy = 2

    def update(self, x):
        if not self.rect.colliderect((0, 0, 800, 600)):
            self.kill()

        if self.rect[1] + 20 >= 500:
            self.kill()

        if self.hinder:
            Platform((self.rect[0], self.rect[1]), 'hinder')
            self.kill()

        if len(pygame.sprite.spritecollide(self, platforms, False)) >= 3:
            self.vx = -self.vx
        elif len(pygame.sprite.spritecollide(self, platforms, False)) >= 1 and \
                len(pygame.sprite.spritecollide(self, grass, False)) >= 1:
            self.vx = -self.vx
        elif len(pygame.sprite.spritecollide(self, grass, False)) >= 3:
            self.rect = self.rect.move(self.vx, -10)

        if pygame.sprite.spritecollideany(self, finish):
            for elem in finish:
                elem.plus_winner()
            self.kill()
        elif pygame.sprite.spritecollideany(self, platforms):
            if self.ground_kill:
                self.kill()

            if self.parach_used:
                self.parach = False

            self.ground = True

            self.distance = 0

            if self.work:
                self.x += x
                if self.x > 300:
                    self.x = 0
                    pygame.sprite.spritecollide(self, platforms, True)
            else:
                self.rect = self.rect.move(self.vx, 0)
        elif pygame.sprite.spritecollideany(self, grass):
            if self.ground_kill:
                self.kill()

            if self.parach_used:
                self.parach = False

            self.ground = True

            self.distance = 0

            if self.work:
                self.x += x
                if self.x > 300:
                    self.x = 0
                    pygame.sprite.spritecollide(self, grass, True)
            else:
                self.rect = self.rect.move(self.vx, 0)
        else:
            self.ground = False

            if self.parach is False or self.distance < 150:
                self.rect = self.rect.move(0, self.vy)
                self.distance += self.vy

            if self.parach and self.distance >= 150:
                self.rect = self.rect.move(0, 1)
                self.parach_used = True
                self.ground_kill = False

            if self.parach is False and self.distance >= 150:
                self.ground_kill = True

            if self.work:
                for q in spaces:
                    pos = q.give_pos()
                    if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1],
                                                                                            self.rect[1] + 20):
                        self.work = False

    def dig(self, pos):
        count = None

        for number in digger:
            count = int(number.give_count())

        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_dig
            if to_dig and count >= 1 and self.work is False and self.ground:
                self.work = True
                to_dig = False
                for elem in digger:
                    elem.change_count()

    def parachute(self, pos):
        count = None

        for number in parachutes:
            count = int(number.give_count())

        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_parachute
            if to_parachute and count >= 1 and self.parach is False:
                self.parach = True
                to_parachute = False
                for elem in parachutes:
                    elem.change_count()

    def hinderer(self, pos):
        count = None

        for number in hinders:
            count = int(number.give_count())

        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_hinder
            if to_hinder and count >= 1 and self.hinder is False and self.ground:
                self.hinder = True
                to_hinder = False
                for elem in hinders:
                    elem.change_count()


class Start(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(starts, all_sprites)
        self.pos = pos
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 20)

    def give_pos(self):
        return self.pos


class Finish(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(finish, all_sprites)
        self.pos = pos
        self.winners = 0
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 9.4 , 20, 20)

    def give_pos(self):
        return self.pos

    def plus_winner(self):
        self.winners += 1

    def show_outers(self):
        return self.winners

    def show_winners(self):
        return self.winners


class Space(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(spaces, all_sprites)
        self.image = pygame.Surface((20, 10))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)

    def give_pos(self):
        return self.rect


class Grass(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(grass, all_sprites)
        self.image = pygame.Surface((20, 10))
        self.image.fill((100, 255, 100))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)


class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(panel, all_sprites)
        self.image = load_image("menu.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500


class Dig(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(digger, all_sprites)
        self.image = load_image("Dig.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 515

        self.count = 10

    def update(self):
        if to_dig:
            self.image = load_image("Dig_chosen.png")
        else:
            self.image = load_image("Dig.png")

    def give_count(self):
        return str(self.count)

    def change_count(self):
        self.count -= 1


class Boom(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(booms, all_sprites)
        self.image = load_image("boom.png")
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = 515

    def update(self):
        if to_boom:
            self.image = load_image("boom_chosen.png")
        else:
            self.image = load_image("boom.png")


class Parachute(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(parachutes, all_sprites)
        self.image = load_image("parachute.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 515

        self.count = 10

    def update(self):
        if to_parachute:
            self.image = load_image("parachute_chosen.png")
        else:
            self.image = load_image("parachute.png")

    def give_count(self):
        return str(self.count)

    def change_count(self):
        self.count -= 1


class Nothing(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(nothings, all_sprites)
        self.image = pygame.Surface((20, 10))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)


class Hinder(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(hinders, all_sprites)
        self.image = load_image("hinder.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 515

        self.count = 10

    def update(self):
        if to_hinder:
            self.image = load_image("hinder_chosen.png")
        else:
            self.image = load_image("hinder.png")

    def give_count(self):
        return str(self.count)

    def change_count(self):
        self.count -= 1


pygame.init()

width = 800
height = 600
size = width, height
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
heroes = pygame.sprite.Group()
starts = pygame.sprite.Group()
finish = pygame.sprite.Group()
spaces = pygame.sprite.Group()
panel = pygame.sprite.Group()
digger = pygame.sprite.Group()
grass = pygame.sprite.Group()
booms = pygame.sprite.Group()
parachutes = pygame.sprite.Group()
nothings = pygame.sprite.Group()
hinders = pygame.sprite.Group()

Menu()
Dig()
Boom()
Parachute()
Hinder()

heroes_count = 0

to_dig = False
to_boom = False
to_parachute = False
to_hinder = False

x = 0
v = 100
fps = 60
timing = 0
time_first = 60
clock = pygame.time.Clock()

generate_level(load_level("Level_1.txt"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in heroes:
                sprite.dig(event.pos)

            for sprite in heroes:
                sprite.parachute(event.pos)

            for sprite in heroes:
                sprite.hinderer(event.pos)

            if event.pos[0] in range(650, 730) and event.pos[1] in range(515, 595):
                to_boom = True

                to_dig = False
                to_parachute = False
                to_hinder = False

            if event.pos[0] in range(100, 180) and event.pos[1] in range(515, 565):
                if to_dig:
                    to_dig = False
                else:
                    to_dig = True

                to_boom = False
                to_parachute = False
                to_hinder = False

            elif event.pos[0] in range(200, 280) and event.pos[1] in range(515, 595):
                if to_parachute:
                    to_parachute = False
                else:
                    to_parachute = True

                to_boom = False
                to_dig = False
                to_hinder = False

            elif event.pos[0] in range(300, 380) and event.pos[1] in range(515, 595):
                if to_hinder:
                    to_hinder = False
                else:
                    to_hinder = True

                to_boom = False
                to_dig = False
                to_parachire = False

    play_level_first()

    if play_level_first():
        print('ALL')
