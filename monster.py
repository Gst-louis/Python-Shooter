import pygame
import random
import animation

# créer une classe moooonstre
class Monster(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3  
        self.image = pygame.transform.scale(self.image, (320, 320))
        self.rect = self.image.get_rect()
        self.rect.x = 1600 + random.randint(0, 300)
        self.rect.y = 570
        self.velocity = random.randint(1, 15)
    
    def damage(self, amount):
        # Pour mettre des degats
        self.health -= amount

        # si vie = 0 bah il est mort
        if self.health <= 0:
            # c'est tchao (pas vraiment mais tkt)
            self.rect.x = 1980
            self.health = self.max_health
            
    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 100, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 100, self.rect.y - 10, self.health, 5])
        

    def forward(self):
        # le deplacement se fait que si il y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):  
            self.rect.x -= self.velocity

        # si il est en collision par contre
        else:
            self.game.player.damage(self.attack)