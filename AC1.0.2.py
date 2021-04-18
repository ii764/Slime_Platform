import pygame

pygame.init()

size = [400, 220]

display = pygame.display.set_mode(size)
pygame.display.set_caption('Absolut Colculator 1.0.2')


start = True

class Button():

    def __init__(self, x, y, w, h, cola = (90, 90, 90), cold = (70, 70, 70)):
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.rect.w = w
        self.rect.h = h
        self.cola = cola
        self.cold = cold
        self.col = self.cold


    def FunBut1(self):
        global manu, math

        if event.type == pygame.MOUSEBUTTONDOWN:

            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()


            if self.rect.collidepoint(mouse):
                self.col = self.cola

                if click[0]:
                    manu = False
                    math = True

        else:
            self.col = self.cold

    def FunBut2(self):

        if event.type == pygame.MOUSEBUTTONDOWN:

            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse):
                self.col = self.cola

                if click[0]:
                    pass

        else:
            self.col = self.cold

    def FunBut3(self):

        if event.type == pygame.MOUSEBUTTONDOWN:

            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse):
                self.col = self.cola

                if click[0]:
                    pass

        else:
            self.col = self.cold


def printText(mas, x, y, col = (255, 255, 255), typef = None, size = 26):

    typef = pygame.font.Font(typef, size)
    text = typef.render(mas, True, col)
    display.blit(text, (x, y))

def pdr(col, rect):
    pygame.draw.rect(display, col, rect)


##############################################Manu
but_matem = Button(10, 20, 180, 50)
but_geom = Button(200, 20, 180, 50)
but_algeb = Button(10, 90, 180, 50)
but_trigan = Button(200, 90, 180, 50)
but_phisic = Button(10, 160, 180, 50)
but_electric = Button(200, 160, 180, 50)
##############################################Math

next = Button(0, 0, 80, 30)
k_0 = Button(0, 0, 80, 30)
k_1 = Button(0, 0, 80, 30)
k_2 = Button(0, 0, 80, 30)
k_3 = Button(0, 0, 80, 30)
k_4 = Button(0, 0, 80, 30)
k_5 = Button(0, 0, 80, 30)
k_6 = Button(0, 0, 80, 30)
k_7 = Button(0, 0, 80, 30)
k_8 = Button(0, 0, 80, 30)
k_9 = Button(0, 0, 80, 30)
k_p = Button(0, 0, 80, 30)
k_m = Button(0, 0, 80, 30)
k_u = Button(0, 0, 80, 30)
k_d = Button(0, 0, 80, 30)
k_r = Button(0, 0, 80, 30)




##############################################
size = [400, 220]
name_scen = 'Absolut Colculator 1.0.2'
##############################################
manu = True
math = False







##############################################
while start:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    display = pygame.display.set_mode(size)
    pygame.display.set_caption(name_scen)



    if manu:
        size = [400, 220]
        display.fill((200, 200, 0))
        pdr(but_matem.col, but_matem.rect)
        but_matem.FunBut1()
        printText('Математика', 20, 28)

        pdr(but_geom.col, but_geom.rect)
        but_geom.FunBut2()
        printText('Геометрия', 210, 28)

        pdr(but_algeb.col, but_algeb.rect)
        but_algeb.FunBut3()
        printText('Алгебра', 20, 98)

        pdr(but_trigan.col, but_trigan.rect)
        but_trigan.FunBut1()
        printText('Триганометрия', 210, 98)

        pdr(but_phisic.col, but_phisic.rect)
        but_phisic.FunBut1()
        printText('Физика', 20, 168)

        pdr(but_electric.col, but_electric.rect)
        but_electric.FunBut1()
        printText('Электроника', 210, 168)

    elif math:
        size = [400, 560]
        name_scen = 'Math Colculator'



    pygame.display.update()