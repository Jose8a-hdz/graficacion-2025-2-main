import pygame
import random
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones")

sonido_disparo = pygame.mixer.Sound("disparo.mp3") 

jugador = pygame.Rect(50, 300, 40, 40)
direct = "derecha"
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]

clock = pygame.time.Clock()
running = True
puntos = 0
font = pygame.font.Font(None, 36)

contador_enemigos = 0
tiempo_generacion = 60  # frames (2 segundos si el juego va a 30 FPS)

while running:
    clock.tick(30)

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


    contador_enemigos += 1
    if contador_enemigos >= tiempo_generacion:
        contador_enemigos = 0
        y_random = random.randint(200, 320)  # posición vertical
        enemigos.append(pygame.Rect(600, y_random, 40, 40))

    for e in enemigos:
        e.x -= 5
    
    # ELIMINAR ENEMIGOS FUERA DE PANTALLA
    enemigos = [e for e in enemigos if e.x > -50]

    for b in balas[:]:
        for e in enemigos[:]:
            if b["rect"].colliderect(e):
                balas.remove(b)
                enemigos.remove(e)
                puntos += 1

    pantalla.fill((0, 181, 226))
    pygame.draw.rect(pantalla, (0, 0, 0), jugador)
    pygame.draw.rect(pantalla, (0, 255, 0), (0, 340, 600, 60))
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b["rect"]) #bala
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e) #enemigo

    texto_puntos = font.render(f"Puntos: {puntos}", True, (0, 0, 0))
    pantalla.blit(texto_puntos, (10, 10))
    pygame.display.update()


pygame.quit()