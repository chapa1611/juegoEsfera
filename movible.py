import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Definir colores
WHITE = (255, 255, 255)

# Definir la velocidad máxima para que el desplazamiento dure al menos 20 segundos
MAX_SPEED = SCREEN_WIDTH / 40  # 20 segundos para cruzar la pantalla

# Cargar imágenes
background_image = pygame.image.load(os.path.join("imagenes", "fondo.jpg"))
background_image = pygame.transform.scale(background_image, SCREEN_SIZE)
sphere_image = pygame.image.load(os.path.join("imagenes", "ball.webp"))

# Clase para la esfera
class Sphere(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(sphere_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        # Actualizar la posición de la esfera
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Si la esfera sale de la pantalla, reaparece en el lado opuesto
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

# Inicializar pantalla
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Moving Sphere")

# Crear sprites
all_sprites = pygame.sprite.Group()
sphere = Sphere()
all_sprites.add(sphere)

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener teclas presionadas
    keys = pygame.key.get_pressed()

    # Modificar la velocidad de la esfera según las teclas presionadas
    if keys[pygame.K_LEFT]:
        sphere.speed_x = -MAX_SPEED
    elif keys[pygame.K_RIGHT]:
        sphere.speed_x = MAX_SPEED
    else:
        sphere.speed_x = 0

    if keys[pygame.K_UP]:
        sphere.speed_y = -MAX_SPEED
    elif keys[pygame.K_DOWN]:
        sphere.speed_y = MAX_SPEED
    else:
        sphere.speed_y = 0

    # Actualizar sprites
    all_sprites.update()

    # Dibujar fondo
    screen.blit(background_image, (0, 0))

    # Dibujar sprites
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
hola
