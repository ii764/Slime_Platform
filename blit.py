import pygame

win = (600, 500)

display = pygame.display.set_mode(win)

win_tolse = pygame.Surface((600, 150))
win_but = pygame.Surface((198, 148))


while True:
    display.fill((80, 80, 80))
    win_but.fill((70, 70, 70))
    win_tolse.fill((60, 60, 60))

    win_tolse.blit(win_but, (0, 0))
    display.blit(win_tolse, (0, 350))


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()


    pygame.display.flip()
