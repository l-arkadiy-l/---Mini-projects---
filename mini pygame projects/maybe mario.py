import pygame as pg


class Hero(pg.sprite.Sprite):
    def __init__(self, pos, create, *group):
        super(Hero, self).__init__(*group)
        self.create = create
        self.image = pg.Surface((20, 20))
        self.image.fill(pg.Color('blue'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[-1]
        self.pos = pg.math.Vector2(pos)
        self.vel = pg.math.Vector2((0, 0))
        self.speed = 10

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[-1]

    def move_hero(self, event, group_stairs):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                self.vel.x = self.speed
            if event.key == pg.K_LEFT:
                self.vel.x = -self.speed
            self.update()
            s = pg.sprite.spritecollideany(self, group_stairs)
            # БАГ
            # персонаж, если зажать кнопку вверхи или вниз улетает
            if s:
                if event.key == pg.K_UP:
                    self.vel.y = -self.speed
                if event.key == pg.K_DOWN:
                    self.vel.y = self.speed
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                self.vel.x = 0
            if event.key == pg.K_LEFT:
                self.vel.x = 0
            if event.key == pg.K_UP:
                self.vel.y = 0
            if event.key == pg.K_DOWN:
                self.vel.y = 0


class Floor(pg.sprite.Sprite):
    def __init__(self, pos, *group):
        super(Floor, self).__init__(*group)
        self.image = pg.Surface((50, 10))
        self.image.fill(pg.Color('gray'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[-1]


class Stair(pg.sprite.Sprite):
    def __init__(self, pos, *group):
        super(Stair, self).__init__(*group)
        self.image = pg.Surface((10, 50))
        self.image.fill(pg.Color('red'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[-1]


def subtraction_tuples(tuple_update: tuple, tuple_delete: tuple):
    tuple_update = [i for i in tuple_update]
    tuple_delete = [i for i in tuple_delete]
    for i in range(len(tuple_delete)):
        tuple_update[i] += tuple_delete[i]
    return tuple_update


if __name__ == '__main__':
    SIZE = WIDTH, HEIGHT = (500, 500)
    screen = pg.display.set_mode(SIZE)
    group_floors = pg.sprite.Group()
    group_stairs = pg.sprite.Group()
    running = True
    hero = Hero((0, 0), False)
    clock = pg.time.Clock()
    fps = 30
    stop = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3 and pg.key.get_mods() & pg.KMOD_CTRL:
                print('ok')
                group_stairs.add(Stair(event.pos))
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                hero.create = True
                hero.pos = event.pos
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                floor = Floor(event.pos)
                group_floors.add(floor)

            hero.move_hero(event, group_stairs)
        screen.fill(pg.Color('black'))
        sp = pg.sprite.spritecollideany(hero, group_floors)
        collide_stair = pg.sprite.spritecollideany(hero, group_stairs)
        group_floors.draw(screen)
        group_stairs.draw(screen)
        if hero.create:
            hero.update()
            screen.blit(hero.image, hero.pos)
        if not sp and not collide_stair:
            hero.pos = subtraction_tuples(hero.pos, (0, 3))
        hero.rect.x = hero.pos[0]
        hero.rect.y = hero.pos[-1]
        clock.tick(fps)
        pg.display.flip()
