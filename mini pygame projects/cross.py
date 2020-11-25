import pygame


def draw(width, height):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), 5)
    pygame.display.set_caption('Крест')


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = list(map(int, input().split()))
    if width <= 0 or height <= 0:
        print('ERROR')
    else:
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        draw(width, height)
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
