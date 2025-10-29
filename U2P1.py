import pygame
import random

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# --- Classes ---
class Player:
    def __init__(self):
        self.pos = pygame.Vector2(400, 300)
        self.color = "red"
        self.radius = 30
        self.hp = 100
        self.dmg = 25
        self.attacking = False
    #keybinds
    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= 250 * dt
        if keys[pygame.K_s]:
            self.pos.y += 250 * dt
        if keys[pygame.K_a]:
            self.pos.x -= 250 * dt
        if keys[pygame.K_d]:
            self.pos.x += 250 * dt

    def attack(self):
        self.attacking = True

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

class Enemy:
    def __init__(self):
        self.pos = pygame.Vector2(random.randint(100, 700), random.randint(100, 500))
        self.color = "green"
        self.radius = 25
        self.hp = 50
        self.speed = 100
        self.attacking = False

    def move(self, player_pos, dt):
        direction = (player_pos - self.pos)
        if direction.length() > 0:
            self.pos += direction.normalize() * self.speed * dt

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

# --- game setup ---
player = Player()
enemy = Enemy()
font = pygame.font.SysFont(None, 30)

# --- game loop ---
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.attack()

    # --- update logic ---
    player.move(dt)
    enemy.move(player.pos, dt)

    # check collisions
    if player.attacking and player.pos.distance_to(enemy.pos) < player.radius + enemy.radius:
        enemy.hp -= player.dmg
        player.attacking = False
    if enemy.hp <= 0:
        enemy = Enemy()  # new enemy appears

    # --- Draw game ---
    screen.fill("purple")
    player.draw(screen)
    enemy.draw(screen)

    # UI
    text = font.render(f"Player HP: {player.hp} | Enemy HP: {enemy.hp}", True, "white")
    screen.blit(text, (20, 20))

    controls = font.render("WASD = Move | Left Click = Attack", True, "white")
    screen.blit(controls, (20, 50))

    pygame.display.flip()

pygame.quit()
#aaadd