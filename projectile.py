import pygame

# definir la classe qui gere les projectiles

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 200
        self.rect.y = player.rect.y + 350
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle -= 20
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un mooooonstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger des dégats
            monster.damage(self.player.attack)

        # supprimer le projectile si il sort de l'ecran
        if self.rect.x > 1920:
            self. remove()