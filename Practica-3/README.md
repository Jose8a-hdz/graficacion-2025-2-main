## 🧩 Práctica 3: Disparos

**Tema:** Crear y mover proyectiles.

### 🎯 Objetivo

**Aprender:**

- Uso de listas para manejar múltiples objetos.

- Movimiento de balas.

- Crear nuevas instancias de objetos.

### 🧠 Funciones nuevas

- **pygame.Rect()** – Representa objetos con posición y tamaño.

- Listas dinámicas para agregar o eliminar balas.

### 🧩 Tarea

- Cambia la velocidad del disparo.

- Dispara en diferentes direcciones.

- Agrega sonido con pygame.mixer.Sound.

### 💻 Código base

```python
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

x, y = 50, 300
balas = []
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(x + 40, y + 15, 10, 5))

    for bala in balas:
        bala.x += 10

    balas = [b for b in balas if b.x < 600]

    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b)
    pygame.display.update()

pygame.quit()

```