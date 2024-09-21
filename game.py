from pygame import *
import pygame

pygame.init()

width = 800
height = 600
racket_width = 10
racket_height = 100
racket_speed = 5
ball_size = 20
ball_speed_x = 3
ball_speed_y = 3
offsetfromthewin = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("bruh game")
racket1 = pygame.Rect(offsetfromthewin, height // 2 - racket_height // 2, racket_width, racket_height)
racket2 = pygame.Rect(width-offsetfromthewin*2-racket_width*3, height // 2 - racket_height // 2, racket_width, racket_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
imageracket = pygame.image.load("racket.png")
tennis = pygame.image.load("tennis_ball.png")


run = True
clock = pygame.time.Clock()
fps = 60
screenupt = True
font1 = pygame.font.Font(None, 80)
win = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and racket1.top > 0:
        racket1.y -= racket_speed
    if keys[pygame.K_s] and racket1.bottom < height:
        racket1.y += racket_speed
    if keys[pygame.K_UP] and racket2.top > 0:
        racket2.y -= racket_speed
    if keys[pygame.K_DOWN] and racket2.bottom < height:
        racket2.y += racket_speed
    
    if screenupt:
        ball.x += ball_speed_x
        if ball.colliderect(racket1) or ball.colliderect(racket2):
            ball.x -= ball_speed_x
            ball_speed_x = -ball_speed_x
        ball.y += ball_speed_y
        if ball.colliderect(racket1) or ball.colliderect(racket2):
            ball.y -= ball_speed_y
            ball_speed_y = -ball_speed_y

        if ball.top <= 0 or ball.bottom >= height:
            ball.y -= ball_speed_y*2
            ball_speed_y = -ball_speed_y
            
        if ball.left <= 0:
            ball.x -= ball_speed_x*2
            ball_speed_x = -ball_speed_x
            screenupt = False
            screen.blit(font1.render("Player 2 wins", True, (255, 255, 255)), (width // 2 - 200, height // 2 - 50))
            win = 2

        if ball.right >= width:
            ball.x -= ball_speed_x*2
            ball_speed_x = -ball_speed_x
            screenupt = False
            screen.blit(font1.render("Player 1 wins", True, (255, 255, 255)), (width // 2 - 200, height // 2 - 50))
            win = 1
        screen.fill((0, 0, 0))
        screen.blit(imageracket,(racket1.x,racket1.y))
        screen.blit(imageracket,(racket2.x,racket2.y))
        screen.blit(tennis,(ball.x,ball.y))
        pygame.display.flip()
    else:
        if win == 1:
            screen.blit(font1.render("Player 1 wins", True, (255, 255, 255)), (width // 2 - 200, height // 2 - 50))
        else:
            screen.blit(font1.render("Player 2 wins", True, (255, 255, 255)), (width // 2 - 200, height // 2 - 50))
        pygame.display.flip()
    clock.tick(fps)
