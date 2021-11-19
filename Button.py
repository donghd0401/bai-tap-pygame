import pygame
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):

        action = False

        # lay vi tri con tro chuot
        pos = pygame.mouse.get_pos()
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        return action