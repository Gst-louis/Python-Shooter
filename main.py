import pygame
from game import Game
pygame.init()

# generer la premiere fenetre
pygame.display.set_caption("Emrys Shooter")
screen = pygame.display.set_mode((1920, 1080))

black = (0, 0, 0)
screen.fill(black)

bg = pygame.image.load('assets/bg.jpg')



# la banniere de jeu
banner = pygame.image.load('assets/banner.png')
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 3.5

# import charger notre bouton pour la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 2.55
play_button_rect.y = screen.get_height() / 1.8 

game = Game()

running = True

while running:

    # appliquer le fond 
    screen.blit(bg, (0, 0))

    # verifier si le jeu a commence dcp
    if game.is_playing:
        # lancer le jeu
        game.update(screen)
    else:
        # ecran de jeu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    
    # mettre a jour l'ecran
    pygame.display.flip()        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # touche espace -> projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # souris collision avec le bouton de jeu au debut tsais
            if play_button_rect.collidepoint(event.pos):
                game.start()
        