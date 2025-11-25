import pygame
pygame.init()

# --- Configuración ---
ANCHO, ALTO = 1300, 630
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional - Sprite Sheet")

fondo = pygame.image.load("fondo1.jpg")
fondo = pygame.transform.scale(fondo, (1300, 620))

# --- Sprite caminando ---
sheet_walk = pygame.image.load("personaje_direcciones1.png").convert_alpha()

FRAME_W_W = 230
FRAME_H_W = 300
COLUMNAS_W = 4      

escala_ = 0.2  # Escala de las imágenes
escala_1 = 0.1

def obtener_frames_walk(fila):
    frames = []
    for i in range(COLUMNAS_W): 
        frame = sheet_walk.subsurface(pygame.Rect(i * FRAME_W_W, fila * FRAME_H_W, FRAME_W_W, FRAME_H_W))
        frame = pygame.transform.scale(frame, (int(FRAME_W_W * escala_), int(FRAME_H_W * escala_)))
        frames.append(frame)
    return frames

anim_walk = {
    "arriba": obtener_frames_walk(3),
    "izquierda": obtener_frames_walk(2),
    "abajo": obtener_frames_walk(0),
    "derecha": obtener_frames_walk(1)
}

# --- Sprite ataque ---
sheet_attack = pygame.image.load("ataque.png").convert_alpha()
FRAME_W_A = 512
FRAME_H_A = 512
COLUMNAS_A = 3

def obtener_frames_attack(fila):
    frames = []
    for i in range(COLUMNAS_A): 
        frame = sheet_attack.subsurface(pygame.Rect(i * FRAME_W_A, fila * FRAME_H_A, FRAME_W_A, FRAME_H_A))
        frame = pygame.transform.scale(frame, (int(FRAME_W_A * escala_1), int(FRAME_H_A * escala_1)))
        frames.append(frame)
    return frames

anim_attack = {
    "arriba": obtener_frames_attack(1),
    "abajo": obtener_frames_attack(1)
}

# --- Variables ---
x, y = ANCHO // 2, ALTO // 2
velocidad = 3
direccion = "abajo"
frame_index = 0
modo_ataque = False
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 120
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    moviendo = False
    modo_ataque = teclas[pygame.K_SPACE]  # si se presiona espacio → ataque

    # Movimiento solo si NO está atacando
    if not modo_ataque:
        if teclas[pygame.K_UP]:
            y -= velocidad
            direccion = "arriba"
            moviendo = True
        elif teclas[pygame.K_DOWN]:
            y += velocidad
            direccion = "abajo"
            moviendo = True
        elif teclas[pygame.K_LEFT]:
            x -= velocidad
            direccion = "izquierda"
            moviendo = True
        elif teclas[pygame.K_RIGHT]:
            x += velocidad
            direccion = "derecha"
            moviendo = True
        
        # EVITAR QUE SALGA DE LA PANTALLA 
    x = max(0, min(x, ANCHO - anim_walk[direccion][0].get_width()))
    y = max(0, min(y, ALTO - anim_walk[direccion][0].get_height()))


    # Animación
    ahora = pygame.time.get_ticks()
    if ahora - ultimo_tiempo > tiempo_animacion:
        frame_index += 1
        ultimo_tiempo = ahora

    VENTANA.blit(fondo, (0, 0))

    if modo_ataque:
        frames = anim_attack[direccion if direccion in anim_attack else "abajo"]
        frame_index %= len(frames)
        VENTANA.blit(frames[frame_index], (x, y))
    else:
        frames = anim_walk[direccion]
        if not moviendo:
            frame_index = 1
        else:
            frame_index %= len(frames)
        VENTANA.blit(frames[frame_index], (x, y))

    pygame.display.flip()
    reloj.tick(80)

pygame.quit()
