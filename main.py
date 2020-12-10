import pygame
import sys
import os
import keyboard

pygame.init()

# random color statics
CHROMA_BG = (0, 255, 0)
# load images
L_UP = pygame.image.load(os.path.join('imgs','bongo l up.png'))
L_DOWN = pygame.image.load(os.path.join('imgs','bongo l down.png'))
R_UP = pygame.image.load(os.path.join('imgs','bongo r up.png'))
R_DOWN = pygame.image.load(os.path.join('imgs','bongo r down.png'))

# keyboard stuff

class Controller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.larm_image = L_UP
        self.rarm_image = R_UP
        self.larm_rect = self.rarm_image.get_rect().move(476, 210)
        self.rarm_rect = self.larm_image.get_rect().move(187, 144)
    
    def update(self):
        if keyboard.is_pressed('f'):
            self.rarm_image = R_DOWN
        else:
            self.rarm_image = R_UP
        if keyboard.is_pressed('j'):
            self.larm_image = L_DOWN
        else:
            self.larm_image = L_UP

    def draw(self, surface):
        surface.blit(self.larm_image, self.larm_rect)
        surface.blit(self.rarm_image, self.rarm_rect)
        return

class Background(pygame.sprite.Sprite):
    # smth i stole from stack overflow
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('imgs', image_file))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# Main function
if __name__ == "__main__":
    bg = Background('bongo base.png', [0, 0])
    #init surface             
    DISPLAYSURF = pygame.display.set_mode((890,441))
    DISPLAYSURF.fill(CHROMA_BG)
    DISPLAYSURF.blit(bg.image, bg.rect)
    pygame.display.set_caption("")

    ctrlr = Controller()

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # UPDATE INPUTS AND SQUASH
        ctrlr.update()

        # REDRAW GARBAGE
        DISPLAYSURF.fill(CHROMA_BG)
        DISPLAYSURF.blit(bg.image, bg.rect)
        ctrlr.draw(DISPLAYSURF)

        pygame.display.update()
