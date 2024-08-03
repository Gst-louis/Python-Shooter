import pygame, comet
from player import Player
from comet_event import CometFallEvent
from monster import Monster

# classe jeu
class Game:
    def __init__(self):
        # running 0 or 1
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        # générer notre joueur
        self.player = Player(self)
        self.all_players.add(self.player)

        # manager de cometes
        self.comet_event = CometFallEvent(self)

        # groupe de moooonstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {} # ça sert  a quoi ca deja
        self.spawn_monster()
    
    def start(self): 
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        # repartir de 0
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la life bar
        self.player.update_health_bar(screen)

        # barre evenement de jeu
        self.comet_event.update_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()
    
        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # aappliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1600:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -200:
            self.player.move_left()  

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self):
        monster = Monster(self)  # Pass 'self' to Monster
        self.all_monsters.add(monster)
