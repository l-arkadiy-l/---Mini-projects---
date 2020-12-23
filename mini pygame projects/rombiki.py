import pygame
from copy import deepcopy

import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                                  self.cell_size), 1)

    def on_click(self, cell):
        if cell[0] >= 0 and cell[-1] >= 0:
            self.board[cell[0]][cell[-1]] = 1
            pygame.draw.rect(screen, pygame.Color('green'),
                             (self.left + cell[0] * self.cell_size, self.top + cell[-1] * self.cell_size,
                              self.cell_size,
                              self.cell_size))
        else:
            return None

    def get_cell(self, mouse_pos):
        if mouse_pos[0] <= self.cell_size * self.width + self.left and mouse_pos[
            -1] <= self.cell_size * self.height + self.top:
            return (mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[-1] - self.top) // self.cell_size
        return -1, -1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return self.on_click(cell)


class Life(Board):
    def __init__(self, board, width, height):
        super(Life, self).__init__(width, height)
        self.current_field = board

    def check_cell(self, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if self.current_field[j][i]:
                    count += 1
        if self.current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0


if __name__ == '__main__':
    running = True
    SIZE = 400
    screen = pygame.display.set_mode((SIZE, SIZE))
    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()
    board = Board(13, 13)
    life = Life(board.board, board.width, board.height)
    # board.set_view(100, 100, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                print('ok')
                for x_y in board.board:
                    life.check_cell(x_y[0], x_y[-1])
        pygame.display.flip()
        board.render()
        clock.tick(fps)
