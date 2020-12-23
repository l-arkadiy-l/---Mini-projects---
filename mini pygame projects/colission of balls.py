import pygame
import random


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2, *group):
        super().__init__(*group)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, *group):
        super().__init__(*group)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)


if __name__ == '__main__':
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    SIZE = width, height = (500, 500)
    screen = pygame.display.set_mode(SIZE)
    b1 = Border(5, 5, width - 5, 5)
    b2 = Border(5, height - 5, width - 5, height - 5)
    b3 = Border(5, 5, 5, height - 5)
    b4 = Border(width - 5, 5, width - 5, height - 5)
    screen.blit(b1.image, (b1.rect.x, b1.rect.y))
    for i in range(10):
        ball = Ball(20, 100, 100)
        screen.blit(ball.image, (ball.vx, ball.vy))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
