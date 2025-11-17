import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

sonido_disparo = pygame.mixer.Sound("disparo.mp3")

x, y = 50, 300
jugador = pygame.Rect(x, y, 40, 40)
direct = "derecha"
balas = []
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direct = "arriba"
            if event.key == pygame.K_DOWN:
                direct = "abajo"
            if event.key == pygame.K_LEFT:
                direct = "izquierda"
            if event.key == pygame.K_RIGHT:
                direct = "derecha"

            if event.key == pygame.K_SPACE:
                sonido_disparo.play()
                bala = pygame.Rect(jugador.centerx - 5, jugador.centery - 2, 10, 5)
                balas.append({"rect": bala, "dir": direct})
       

    for b in balas:
        if b["dir"] == "derecha":
            b["rect"].x += 10
        elif b["dir"] == "izquierda":
            b["rect"].x -= 10
        elif b["dir"] == "arriba":
            b["rect"].y -= 10
        elif b["dir"] == "abajo":
            b["rect"].y += 10

    balas = [b for b in balas if 0 <= b["rect"].x < 600 and 0 <= b["rect"].y <= 400]

    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b["rect"])
    pygame.display.update()

pygame.display.update()

pygame.quit()