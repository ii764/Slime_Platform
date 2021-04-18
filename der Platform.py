import pygame

pygame.init()

size = (680, 500)

display = pygame.display.set_mode(size)

x = 200
y = 200
gravity = 1

start = True
sten = pygame.Rect(0, 400, 600, 30)

clock = pygame.time.Clock()

while start:

    player = pygame.Rect(x, y, 50, 50)

    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(display, (200, 200, 0), player)
    pygame.draw.rect(display, (200, 200, 200), sten)

    mouse = pygame.mouse.get_pos()


    if sten.collidepoint(player.x, player.y+50):
        gravity = 0
    else:
        gravity = 1

    y += gravity

    clock.tick_busy_loop(60)

    pygame.display.update()
