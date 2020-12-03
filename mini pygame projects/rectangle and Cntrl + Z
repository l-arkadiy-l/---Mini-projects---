import pygame


def update_place(objects, screen):
    if not objects: return objects
    screen.fill(pygame.Color('black'))
    del objects[-1]
    for x1, y1, w, h in objects:
        pygame.draw.rect(screen, (255, 255, 255), (x1, y1, w, h), 5)
    return objects


if __name__ == '__main__':
    running = True
    screen = pygame.display.set_mode((800, 800))
    screen2 = pygame.Surface(screen.get_size())
    x1, y1, w, h = 0, 0, 0, 0
    all_objects = []
    drawing = False  # режим рисования выключен
    while running:
        all_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                # запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # сохраняем нарисованное (на втором холсте)
                screen2.blit(screen, (0, 0))
                drawing = False
                all_objects.append([x1, y1, w, h])
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                # запоминаем текущие размеры
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            if all_keys[pygame.K_z] and (all_keys[pygame.K_LCTRL] or all_keys[pygame.K_RCTRL]):
                all_objects = update_place(all_objects, screen2)
        # рисуем на экране сохранённое на втором холсте
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        if drawing:  # и, если надо, текущий прямоугольник
            if w > 0 and h > 0:
                pygame.draw.rect(screen, (255, 255, 255), ((x1, y1), (w, h)), 5)
                print(x1, y1, w, h)

        pygame.display.flip()
