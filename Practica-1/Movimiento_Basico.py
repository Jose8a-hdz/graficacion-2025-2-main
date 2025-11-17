import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

x, y = 300, 200
vel = 5
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= vel
    if teclas[pygame.K_RIGHT]:
        x += vel
    if teclas[pygame.K_UP]:
        y -= vel
    if teclas[pygame.K_DOWN]:
        y += vel
    if teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
        vel = 15
    else:
        vel = 5

    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, (0, 200, 255), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()