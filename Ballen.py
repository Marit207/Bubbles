import pygame
import random

pygame.init()

radius = 50

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite example")

class Ball(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.color = random.randint(0, 20), random.randint(0, 255), random.randint(0, 255)
    self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(self.image, self.color, (radius, radius), 50)
    
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.velocity_x = random.randint(1,3)
    self.velocity_y = random.randint(1,3)

  def update(self):
    self.rect.x += self.velocity_x
    if self.rect.right >= WIDTH:
      self.rect.right = WIDTH
      self.velocity_x = -self.velocity_x
    
    if self.rect.left <= 0:
      self.rect.left = 0
      self.velocity_x = -self.velocity_x
      
    self.rect.y += self.velocity_y
    if self.rect.bottom >= HEIGHT:
      self.rect.bottom = HEIGHT
      self.velocity_y = -self.velocity_y
    
    if self.rect.top <= 0:
      self.rect.top = 0
      self.velocity_y = -self.velocity_y

balls = pygame.sprite.Group()

for ball in range(20):
  x = random.randint(100, WIDTH - radius)
  y = random.randint(100, HEIGHT - radius)
  ball = Ball(x, y)
  balls.add(ball)

running = True
clock = pygame.time.Clock()
while running:
  screen.fill((0, 0, 120))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  balls.update()
  
  balls.draw(screen)
  pygame.display.update()

  clock.tick(60)

pygame.quit()