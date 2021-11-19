import pygame
import random
from Bird import Bird
from Button import Button
from Pipe import Pipe

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
font = pygame.font.SysFont('Bauhaus 93', 60)
white = (255, 255, 255)
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
pass_pipe = False
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')
button_img = pygame.image.load('img/restart.png')
score = 0
max_score=0
with open("score.txt", 'r') as f:
    for i in f:
        max_score=int(i)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)
button = Button(screen_width // 2-50, screen_height // 2, button_img)

run = True
while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    bird_group.update(flying, game_over)
    screen.blit(ground_img, (ground_scroll, 768))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("score.txt", 'w') as f:
                f.write(str(max_score))
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    # dieu kien thua
    if game_over == True:
        if button.draw(screen) == True:
            game_over = False
            score = reset_game()

    # cap nhat diem
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
    draw_text("Score "+str(score), font, white, int(screen_width / 2)-120, 20)
    draw_text("Max Score "+str(max_score), font, white, int(screen_width / 2)-180, 80)
    # kiem tra va cham
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        if score > max_score:
            max_score = score
        game_over = True

    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False
    if game_over == False and flying == True:
        # sinh ong moi
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1, pipe_gap)
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1, pipe_gap)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        # draw and scroll the ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update(scroll_speed)

    pygame.display.update()
pygame.quit()
