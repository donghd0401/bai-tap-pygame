import pygame
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, pipe_gap):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        # position 1 la ong tren, -1 la ong duoi
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()