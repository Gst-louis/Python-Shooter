import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.animations = {}
        self.images = self.animations.get(sprite_name)

    def animate(self):
        self.current_image+=1
        if self.current_image >= len(self.images):
            self.current_image = 0
        
        self.image = self.images[self.current_image]

    # charger les images d'un sprite
    def load_animation_images(sprite_name):
        # charger les images
        images = []
        # recuperer le chemin du dossier pour ce sprite
        path = f"assets/{sprite_name}/{sprite_name}"

        # boucler sur chaque image dans le dossier
        for num in range(1, 24):
            image_path = path + num + '.png'
            images.append(pygame.image.load(image_path))

        # renvoyer les images
        return images
    
        # dictionnaire chaque sprite images
        self.animations = {
            'mummy' : load_animation_images('mummy')
        }