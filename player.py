import pygame
from projectile import Projectile

# classe pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 760
        self.rect.y = 340

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # bah si il est mort quoi mdr
            self.game.game_over()

    def update_health_bar(self, surface):
        
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 200, self.rect.y + 180, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 200, self.rect.y + 180, self.health, 5])
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):  
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity