import pygame
import random
import time

#Setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
points = 0
pygame.font.init()

#Classes
class Player:
    def __init__(self):
        self.pos = pygame.Vector2(400, 300)
        self.color = "green"
        self.radius = 30
        self.hp = 100
        self.dmg = 25
        self.attacking = False

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
        self.color = "red"
        self.radius = 35
        self.hp = 50
        self.speed = 150
        self.attacking = False

    def move(self, player_pos, dt):
        direction = (player_pos - self.pos)
        if direction.length() > 0:
            self.pos += direction.normalize() * self.speed * dt

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


#game setup
player = Player()
enemy = Enemy()
font = pygame.font.SysFont(None, 30)

#game loop
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if player clicked enemy
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            if (mouse_pos - enemy.pos).length() < enemy.radius:
                enemy.hp -= player.dmg
                print("Enemy hit!")

    #update logic
    player.move(dt)
    enemy.move(player.pos, dt)

    #Enemy touches player
    if (enemy.pos - player.pos).length() < (enemy.radius + player.radius):
        player.hp -= 1  # slowly lose health
        if player.hp <= 0:
            print("Alas, a villainous knave hath struck me down!")
            time.sleep(2)
            running = False

    #Enemy defeated
    if enemy.hp <= 0:
        print("Enemy defeated!")
        enemy = Enemy()
        points += 1

    #Draw game
    screen.fill("purple")
    player.draw(screen)
    enemy.draw(screen)

    #UI
    text = font.render(f"Player HP: {player.hp} | Enemy HP: {enemy.hp}", True, "white")
    screen.blit(text, (20, 20))

    controls = font.render("WASD = Move | Left Click Enemy = Attack", True, "white")
    screen.blit(controls, (20, 50))

    points_text = font.render(f"Points: {points}", True, "white")
    screen.blit(points_text, (20, 80))

    pygame.display.flip()

pygame.quit()
