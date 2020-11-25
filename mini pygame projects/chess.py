import pygame


def draw(field, cell):
    screen.fill((100, 100, 100))
    black = pygame.Color('black')
    white = pygame.Color('white')
    counter = 0
    cell_1 = round(field / cell)
    if (field // cell) % 2 == 0:
        counter += 1
    if cell % 2 == 0:
        cell += 1
    for i in range(cell):
        for j in range(cell):
            if counter % 2 != 0:
                pygame.draw.rect(screen, black, (i * cell_1, j * cell_1, cell_1, cell_1))
            else:
                pygame.draw.rect(screen, white, (i * cell_1, j * cell_1, cell_1, cell_1))
            counter += 1


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    width, height = list(map(int, input().split()))
    if width <= 0 or height <= 0:
        print('ERROR')
    else:
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode((width, width))
        draw(width, height)
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
