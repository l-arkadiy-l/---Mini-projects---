import pygame as pg

FILEDIR = 'data'
tile_images = {
    'wall': pg.image.load('{}/box.png'.format(FILEDIR)),
    'empty': pg.image.load('{}/grass.png'.format(FILEDIR))
}
player_image = pg.image.load('{}/mario.png'.format(FILEDIR))

tile_width = tile_height = 50
player = None

# группы спрайтов
all_sprites = pg.sprite.Group()
tiles_group = pg.sprite.Group()
player_group = pg.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y, True)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Tile(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, is_wall=False):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.is_wall = is_wall


class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.speed = 50
        self.vel = pg.math.Vector2((0, 0))

    def move(self, event):
        if event.key == pg.K_DOWN:
            self.rect.y += self.speed
            if pg.sprite.spritecollideany(self, tiles_group).is_wall:
                self.rect.y -= self.speed
        if event.key == pg.K_UP:
            self.rect.y -= self.speed
            if pg.sprite.spritecollideany(self, tiles_group).is_wall:
                self.rect.y += self.speed
        if event.key == pg.K_RIGHT:
            self.rect.x += self.speed
            if pg.sprite.spritecollideany(self, tiles_group).is_wall:
                self.rect.x -= self.speed
        if event.key == pg.K_LEFT:
            self.rect.x -= self.speed
            if pg.sprite.spritecollideany(self, tiles_group).is_wall:
                self.rect.x += self.speed


def start_screen(filedir):
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pg.transform.scale(pg.image.load('{}/fon.jpg'.format(filedir)), (width, height))
    screen.blit(fon, (0, 0))
    font = pg.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pg.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def load_level(filename):
    filename = FILEDIR + "/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


SIZE = width, height = (550, 500)
if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()
    running = True
    draw_area = False
    try:
        player, level_x, level_y = generate_level(load_level('map.txt'))
    except FileNotFoundError:
        print('Походу случился error')
        exit(0)
    camera = Camera()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                draw_area = True
            if event.type == pg.KEYDOWN and draw_area:
                player.move(event)
        screen.fill(pg.Color('black'))
        if not draw_area:
            start_screen(FILEDIR)
        else:
            tiles_group.draw(screen)
            # all_sprites.draw(screen)
            player_group.draw(screen)
            for i in all_sprites:
                camera.apply(i)
            camera.update(player)

        clock.tick(100)
        pg.display.flip()
    pg.quit()
