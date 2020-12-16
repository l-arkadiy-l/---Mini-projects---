import pygame

pygame.init()

pygame.display.set_caption("Test")
screen = pygame.display.set_mode([640, 640])
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = pygame.image.load('data/arrow.png')
running = True
while running:
    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            screen.fill(pygame.Color('black'))
            screen.blit(sprite.image, event.pos)
    pygame.display.flip()
