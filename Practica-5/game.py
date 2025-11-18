import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 5 - Sprites y fondo")

# Cargar imágenes
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (600, 400))

sprite = pygame.image.load("Fox.webp")
sprite = pygame.transform.scale(sprite, (100, 100))

sprite_dis = pygame.image.load("Fox1.webp")
sprite_dis = pygame.transform.scale(sprite_dis, (100, 100))

sprite_act = sprite

bala_img = pygame.Surface((10,5))
bala_img.fill((255,0,0))


#variables

x = 500
y = 220
velocidad = 5

salto = False
vel_y = 0
gravedad = 1
fuerza_salto = -15

balas = []
direct = "derecha"
bala_vel = 10
sonido_disparo = pygame.mixer.Sound("disparo.mp3")
tiempo_dis = 0
duracion_dis = 10
enemigos = [pygame.Rect(10, 231, 50, 80)]
clock = pygame.time.Clock()
running = True

#posición para scroll
fondo_x1 = 0
fondo_x2 = 600 # la segunda imagen empieza justo pegada a la primera
velocidad_fondo = 2 # velocidad de desplazamiento del fondo

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #disparo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direct = "arriba"
            if event.key == pygame.K_s:
                direct = "abajo"
            if event.key == pygame.K_a:
                direct = "izquierda"
            if event.key == pygame.K_d:
                direct = "derecha"
            if event.key == pygame.K_f:
                sonido_disparo.play()
                bala = pygame.Rect(x + 90, y + 45, 10, 5)
                balas.append({"rect": bala, "dir": direct})
            
            sprite_act = sprite_dis
            tiempo_dis = duracion_dis
    
    if tiempo_dis > 0:
        tiempo_dis -= 1
        if tiempo_dis == 0:
            sprite_act = sprite
#movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += velocidad
    if keys[pygame.K_LEFT]:
        x -= velocidad
    
    if x > 600:
        x = -100
    if x < -100:
        x = 600
#salto
    if keys[pygame.K_SPACE] and not salto:
            salto = True
            vel_y = fuerza_salto
    if salto: 
        y += vel_y
        vel_y += gravedad

        if y >= 300:
            y = 300
            salto = False

# Mover el fondo para crear efecto de scroll
    fondo_x1 -= velocidad_fondo
    fondo_x2 -= velocidad_fondo

    if fondo_x1 <= -600:
        fondo_x1 = 600
    if fondo_x2 <= -600:
        fondo_x2 = 600
    # Dibujar fondos en sus nuevas posiciones
    pantalla.blit(fondo, (fondo_x1, 0))
    pantalla.blit(fondo, (fondo_x2, 0))
    # Mover y dibujar balas
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

    # ELIMINAR ENEMIGOS FUERA DE PANTALLA
    enemigos = [e for e in enemigos if e.x > -50]

    for b in balas[:]:
        for e in enemigos[:]:
            if b["rect"].colliderect(e):
                balas.remove(b)
                enemigos.remove(e)
                puntos += 1
                
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b["rect"]) #bala
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e) #enemigo

    pantalla.blit(sprite_act, (x, y))
    pygame.display.update()

pygame.quit()