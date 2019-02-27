import pygame
import os
import sys
import random


def start_screen():
    intro_text = ["ПРИВЕТ!", "",
                  "Правила игры:",
                  "Нужно довести леммингов до выхода",
                  "Пользуйтесь способностями на нижней панели"]

    fon = load_image('start_screen.png')
    screen.blit(fon, (0, 0))
    font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 30)
    text_coord = 150
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('gold'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 75
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


def middle_screen():
    fon = load_image('start_screen.png')
    screen.blit(fon, (0, 0))

    start = load_image('start_game.png')
    screen.blit(start, (130, 110))

    stop = load_image('quit_game.png')
    screen.blit(stop, (250, 340))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                if event.pos[0] in range(130, 631) and event.pos[1] in range(110, 244):
                    start = load_image('start_game_chosen.png')
                    screen.blit(start, (130, 110))
                else:
                    start = load_image('start_game.png')
                    screen.blit(start, (130, 110))

                if event.pos[0] in range(250, 497) and event.pos[1] in range(340, 463):
                    stop = load_image('quit_game_chosen.png')
                    screen.blit(stop, (250, 340))
                else:
                    stop = load_image('quit_game.png')
                    screen.blit(stop, (250, 340))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(250, 497) and event.pos[1] in range(340, 463):
                    terminate()
                if event.pos[0] in range(130, 631) and event.pos[1] in range(110, 244):
                    return

        pygame.display.flip()
        clock.tick(fps)


def play_level_first():
    global to_dig, to_parachute, to_boom, to_hinder, v, fps, timing

    Menu()
    Dig_Menu()
    Boom_Menu()
    Parachute_Menu()
    Hinder_Menu()

    time = 60
    heroes_count = 0

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

                if event.pos[0] in range(400, 480) and event.pos[1] in range(515, 595):
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
                    to_parachute = False

        for f in finish:
            if f.show_outers() == 0:
                for sprite in all_sprites:
                    sprite.kill()
                return

        if time > 0:
            screen.fill((0, 0, 0))
            x = v / fps
            timing += x

            if timing > 250:
                heroes_count += 1
                if heroes_count <= 10:
                    for elem in starts:
                        pos = elem.give_pos()
                        Lemming((pos[0] + 1, pos[1]), load_image("lemmings.png", color_key=-1), 10, 1)
                    timing = 0
            starts.update(x)
            bloods.update()
            finish.update(x)
            heroes.update(x)
            hinders.update(x)
            digger_menu.update()
            booms_menu.update()
            parachutes_menu.update()
            hinders_menu.update()

            time -= 0.01

            all_sprites.draw(screen)

            draw_count()
            show_time(int(time))

            pygame.display.flip()
            clock.tick(fps)

            if to_boom:
                for sprites in heroes:
                    sprites.kill()
                    heroes_count = 10
        else:
            terminate()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 30
    # возможные скорости
    numbers = range(-4, 4)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def play_level_second():
    global to_dig, to_parachute, to_boom, to_hinder, v, fps, timing

    Menu()
    Dig_Menu()
    Boom_Menu()
    Parachute_Menu()
    Hinder_Menu()

    time = 120
    heroes_count = 0
    timing = 0

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

                if event.pos[0] in range(400, 480) and event.pos[1] in range(515, 595):
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
                    to_parachute = False

        if len(heroes) == 0:
            if heroes_count >= 10:
                for sprite in all_sprites:
                    sprite.kill()
                return True

        if time > 0:
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
            digger_menu.update()
            booms_menu.update()
            parachutes_menu.update()
            hinders_menu.update()
            starts.update(x)

            time -= 0.01

            all_sprites.draw(screen)

            draw_count()
            show_time(int(time))

            pygame.display.flip()
            clock.tick(fps)

            if to_boom:
                for sprites in heroes:
                    sprites.kill()
                    heroes_count = 10
        else:
            terminate()


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


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        image = image.convert_alpha()
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
                Start((x, y), load_image("start.png", color_key=-1), 1, 10)
            elif level[y][x] == '2':
                Finish((x, y), load_image("finish.png", color_key=-1), 1, 2)
            elif level[y][x] == '.':
                Space((x, y))
            elif level[y][x] == '@':
                Grass((x, y))
    return x, y


def draw_count():
    for f in finish:
        count = f.show_outers()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 50)

        text_out = font.render('OUT ' + str(count), 1, (100, 255, 100))
        text_out_x = 250
        text_out_y = 450
        screen.blit(text_out, (text_out_x, text_out_y))

        count = f.show_winners()
        text_in = font.render('IN ' + str(count * 10) + '%', 1, (100, 255, 100))
        text_in_x = 500
        text_in_y = 450
        screen.blit(text_in, (text_in_x, text_in_y))

    for d in digger_menu:
        count = d.give_count()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
        text = font.render(count, 1, (100, 255, 100))

        text_x = 130
        text_y = 570

        screen.blit(text, (text_x, text_y))

    for p in parachutes_menu:
        count = p.give_count()
        font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
        text = font.render(count, 1, (100, 255, 100))

        text_x = 230
        text_y = 570

        screen.blit(text, (text_x, text_y))

    for h in hinders_menu:
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

    def __init__(self, pos):
        super().__init__(platforms, all_sprites)
        self.image = load_image('dirt.png')
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)


class Lemming(pygame.sprite.Sprite):

    def __init__(self, pos, sheet, columns, rows):
        super().__init__(heroes, all_sprites)

        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cut_sheet(load_image('falling.png', color_key=-1), 4, 1)
        self.cut_sheet(load_image('falling_parachute_start.png', color_key=-1), 3, 1)
        self.cut_sheet(load_image('falling_parachute_continue.png', color_key=-1), 5, 1)
        self.cut_sheet(load_image('digger.png', color_key=-1), 8, 1)
        self.cur_frame = 0
        self.image = self.frames[0][self.cur_frame]

        self.work = False
        self.ground = False
        self.parach = False
        self.parach_used = False
        self.ground_kill = False
        self.hinder = False
        self.povorot = False
        self.distance = 0
        self.x = 0

        self.smena = 0

        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)
        self.vx = 1
        self.vy = 2

        self.open = True

        self.sound_effects = {'win': pygame.mixer.Sound('data/win.wav'),
                              'lose': pygame.mixer.Sound('data/lose.wav')}

    def update(self, x):
        self.smena += x

        if self.smena >= 7 and self.ground and self.work is False:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames[0])
            self.image = self.frames[0][self.cur_frame]
            self.image = pygame.transform.scale(self.image, (20, 20))
            if self.povorot:
                self.image = pygame.transform.flip(self.image, True, False)

            self.smena = 0

        if not self.rect.colliderect((0, 0, 800, 600)):
            create_particles((self.rect[0], self.rect[1]))
            self.sound_effects['lose'].play()
            self.kill()
            for elem in finish:
                elem.minus_outer()

        if self.rect[1] + 20 >= 500:
            create_particles((self.rect[0], self.rect[1]))
            self.sound_effects['lose'].play()
            self.kill()
            for elem in finish:
                elem.minus_outer()

        if self.hinder:
            Hinder((self.rect[0], self.rect[1]))
            self.kill()
            for elem in finish:
                elem.minus_outer()

        if len(pygame.sprite.spritecollide(self, platforms, False)) >= 3:
            self.vx = -self.vx
            if self.povorot:
                self.povorot = False
            else:
                self.povorot = True
        elif len(pygame.sprite.spritecollide(self, platforms, False)) >= 1 and \
                len(pygame.sprite.spritecollide(self, grass, False)) >= 1:
            self.vx = -self.vx
            if self.povorot:
                self.povorot = False
            else:
                self.povorot = True
        elif len(pygame.sprite.spritecollide(self, grass, False)) >= 3:
            self.rect = self.rect.move(self.vx, -10)
        elif len(pygame.sprite.spritecollide(self, hinders, False)) >= 3:
            self.vx = -self.vx
            if self.povorot:
                self.povorot = False
            else:
                self.povorot = True
        elif len(pygame.sprite.spritecollide(self, hinders, False)) >= 1 and \
                len(pygame.sprite.spritecollide(self, grass, False)) >= 1:
            self.vx = -self.vx
            if self.povorot:
                self.povorot = False
            else:
                self.povorot = True

        if pygame.sprite.spritecollideany(self, finish):
            for elem in finish:
                elem.plus_winner()
                elem.minus_outer()
            self.sound_effects['win'].play()
            self.kill()
        elif pygame.sprite.spritecollideany(self, platforms):
            if self.ground_kill:
                for elem in finish:
                    elem.minus_outer()
                create_particles((self.rect[0], self.rect[1]))
                self.sound_effects['lose'].play()
                self.kill()

            if self.parach_used:
                self.parach = False

            self.ground = True

            self.distance = 0

            if self.work:
                if self.smena >= 7:
                    self.cur_frame = (self.cur_frame + 1) % len(self.frames[4])
                    self.image = self.frames[4][self.cur_frame]
                    self.image = pygame.transform.scale(self.image, (20, 20))

                    self.smena = 0

                self.x += x
                if self.x > 250:
                    self.x = 0
                    pygame.sprite.spritecollide(self, platforms, True)
            else:
                self.rect = self.rect.move(self.vx, 0)
        elif pygame.sprite.spritecollideany(self, hinders):
            if self.ground_kill:
                for elem in finish:
                    elem.minus_outer()
                self.kill()

            if self.parach_used:
                self.parach = False
            else:
                self.open = True

            self.ground = True

            self.distance = 0

            self.rect = self.rect.move(self.vx, 0)
        elif pygame.sprite.spritecollideany(self, grass):
            if self.ground_kill:
                for elem in finish:
                    elem.minus_outer()
                create_particles((self.rect[0], self.rect[1]))
                self.sound_effects['lose'].play()
                self.kill()

            if self.parach_used:
                self.parach = False
            else:
                self.open = True

            self.ground = True

            self.distance = 0

            if self.work:
                if self.smena >= 7:
                    self.cur_frame = (self.cur_frame + 1) % len(self.frames[4])
                    self.image = self.frames[4][self.cur_frame]
                    self.image = pygame.transform.scale(self.image, (20, 20))

                    self.smena = 0

                self.x += x
                if self.x > 300:
                    self.x = 0
                    pygame.sprite.spritecollide(self, grass, True)
            else:
                self.rect = self.rect.move(self.vx, 0)
        else:
            self.ground = False

            if self.parach is False or self.distance < 150:
                if self.smena >= 7:
                    self.cur_frame = (self.cur_frame + 1) % len(self.frames[1])
                    self.image = self.frames[1][self.cur_frame]
                    self.image = pygame.transform.scale(self.image, (20, 20))

                    self.smena = 0

                self.rect = self.rect.move(0, self.vy)
                self.distance += self.vy

            if self.parach and self.distance >= 150:
                if self.smena >= 7 and self.open:
                    self.cur_frame = (self.cur_frame + 1) % len(self.frames[2])
                    self.image = self.frames[2][self.cur_frame]
                    self.image = pygame.transform.scale(self.image, (20, 20))

                    self.smena = 0

                    if self.cur_frame == 0:
                        self.open = False
                if self.smena >= 20 and self.open is False:
                    self.cur_frame = (self.cur_frame + 1) % len(self.frames[3])
                    self.image = self.frames[3][self.cur_frame]
                    self.image = pygame.transform.scale(self.image, (20, 20))

                    self.smena = 0

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

        for number in digger_menu:
            count = int(number.give_count())

        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_dig
            if to_dig and count >= 1 and self.work is False and self.ground:
                self.work = True
                to_dig = False
                for elem in digger_menu:
                    elem.change_count()

    def parachute(self, pos):
        count = None

        for number in parachutes_menu:
            count = int(number.give_count())

        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_parachute
            if to_parachute and count >= 1 and self.parach is False:
                self.parach = True
                to_parachute = False
                for elem in parachutes_menu:
                    elem.change_count()

    def hinderer(self, pos):
        count = None

        for number in hinders_menu:
            count = int(number.give_count())

        if pos[0] in range(self.rect[0], self.rect[0] + 20) and pos[1] in range(self.rect[1], self.rect[1] + 20):
            global to_hinder
            if to_hinder and count >= 1 and self.hinder is False and self.ground and self.work is False:
                self.hinder = True
                to_hinder = False
                for elem in hinders_menu:
                    elem.change_count()

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)

        self.frames.append([])
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames[len(self.frames) - 1].append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))


class Start(pygame.sprite.Sprite):

    def __init__(self, pos, sheet, columns, rows):
        super().__init__(starts, all_sprites)
        self.pos = pos
        self.image = pygame.Surface((41, 25))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] * 20
        self.rect.y = pos[1] * 10

        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        self.smena = 0

        self.stop = False

    def give_pos(self):
        return self.pos

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(self.rect[0], self.rect[1], sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x):
        self.smena += x
        if self.smena >= 10:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            if self.cur_frame == 0:
                self.stop = True
            if self.stop is False:
                self.image = self.frames[self.cur_frame]

            self.smena = 0


class Finish(pygame.sprite.Sprite):

    def __init__(self, pos, sheet, columns, rows):
        super().__init__(finish, all_sprites)
        self.winners = 0
        self.outers = 10

        self.image = pygame.Surface((33, 25))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] * 19.5
        self.rect.y = pos[1] * 9.6

        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        self.pos = pos
        self.smena = 0

    def give_pos(self):
        return self.pos

    def plus_winner(self):
        self.winners += 1

    def show_winners(self):
        return self.winners

    def minus_outer(self):
        self.outers -= 1

    def show_outers(self):
        return self.outers

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(self.rect[0], self.rect[1], sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x):
        self.smena += x
        if self.smena >= 10:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]

            self.smena = 0


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
        self.image = load_image('grass.png')
        self.rect = pygame.Rect(pos[0] * 20, pos[1] * 10, 20, 10)


class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(panel, all_sprites)
        self.image = load_image("menu.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500


class Dig_Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(digger_menu, all_sprites)
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


class Boom_Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(booms_menu, all_sprites)
        self.image = load_image("boom.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 515

    def update(self):
        if to_boom:
            self.image = load_image("boom_chosen.png")
        else:
            self.image = load_image("boom.png")


class Parachute_Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(parachutes_menu, all_sprites)
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


class Hinder_Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(hinders_menu, all_sprites)
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


class Particle(pygame.sprite.Sprite):

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites, bloods)
        # сгенерируем частицы разного размера
        self.fire = [load_image("blood.png")]
        for scale in (5, 7, 10):
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))

        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.2

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


class Hinder(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(hinders, all_sprites)

        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.frames = []
        self.cut_sheet(load_image('hind.png', color_key=-1), 16, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        self.smena = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(self.rect[0], self.rect[1], sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x):
        self.smena += x
        if self.smena >= 10:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.scale(self.image, (20, 20))

            self.smena = 0


pygame.init()

width = 800
height = 600
size = width, height
screen = pygame.display.set_mode(size)
screen_rect = (0, 0, width, height)

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
heroes = pygame.sprite.Group()
starts = pygame.sprite.Group()
finish = pygame.sprite.Group()
spaces = pygame.sprite.Group()
panel = pygame.sprite.Group()
digger_menu = pygame.sprite.Group()
grass = pygame.sprite.Group()
booms_menu = pygame.sprite.Group()
parachutes_menu = pygame.sprite.Group()
nothings = pygame.sprite.Group()
hinders_menu = pygame.sprite.Group()
hinders = pygame.sprite.Group()
bloods = pygame.sprite.Group()

to_dig = False
to_boom = False
to_parachute = False
to_hinder = False

v = 100
fps = 60
timing = 0

clock = pygame.time.Clock()

music = pygame.mixer.music.load('data/main_theme.wav')
pygame.mixer.music.play(-1, 0.0)

start_screen()

middle_screen()

generate_level(load_level("Level_1.txt"))
play_level_first()

generate_level(load_level("Level_2.txt"))
play_level_second()

pygame.quit()
