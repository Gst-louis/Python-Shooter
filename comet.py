import pygame, random

# classe qui gère les grosses boules
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associee a cette comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 6)
        self.rect.x = random.randint(20, 1900)
        self.comet_event = comet_event
    
    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 880:
            self.remove()

        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            self.remove()
            self.comet_event.game.player.damage(20)