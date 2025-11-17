## 🧩 Práctica 5: Fondo, sprites y animación

**Tema:** Mejorar la estética y animar al personaje.

### 🎯 Objetivo

**Aprender:**

- Cargar imágenes.

- Dibujar sprites.

- Simular desplazamiento.

### 🧠 Funciones nuevas

- **pygame.image.load()** – Carga imágenes.

- **pantalla.blit()** – Dibuja imágenes en la pantalla.

### 🧩 Tarea

- Anima el personaje cambiando imágenes.

- Mueve el fondo para simular desplazamiento.

- Combina salto, disparos y colisiones en un mini juego final.

### 💻 Código base

```python
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 5 - Sprites y fondo")

fondo = pygame.image.load("fondo.png")
sprite = pygame.image.load("personaje.png")
x = 100
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(sprite, (x, 300))
    pygame.display.update()

pygame.quit()

```