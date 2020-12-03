import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
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
        # red, blue, None
        if cell[-1] >= 0 and cell[0] >= 0:
            print(cell, self.board)
            if self.board[cell[-1]][cell[0]] == 0:
                self.board[cell[-1]][cell[0]] = 1
                pygame.draw.rect(screen, pygame.Color('red'),
                                 (self.left + cell[0] * self.cell_size, self.top + cell[-1] * self.cell_size,
                                  self.cell_size,
                                  self.cell_size))
            elif self.board[cell[-1]][cell[0]] == 1:
                self.board[cell[-1]][cell[0]] = 2
                pygame.draw.rect(screen, pygame.Color('blue'),
                                 (self.left + cell[0] * self.cell_size, self.top + cell[-1] * self.cell_size,
                                  self.cell_size,
                                  self.cell_size))
            else:
                self.board[cell[-1]][cell[0]] = 0
                pygame.draw.rect(screen, pygame.Color('black'),
                                 (self.left + cell[0] * self.cell_size, self.top + cell[-1] * self.cell_size,
                                  self.cell_size,
                                  self.cell_size))

        else:
            return None

    def get_cell(self, mouse_pos):
        if mouse_pos[0] <= self.cell_size * self.width + self.left and mouse_pos[
            -1] <= self.cell_size * self.height + self.top:
            return (mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[-1] - self.top) // self.cell_size
        return (-1, -1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return self.on_click(cell)


if __name__ == '__main__':
    running = True
    SIZE = 400
    screen = pygame.display.set_mode((SIZE, SIZE))
    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()
    board = Board(5, 7)
    # board.set_view(100, 100, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_click(event.pos))
        pygame.display.flip()
        board.render()
        clock.tick(fps)
