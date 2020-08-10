import pygame
import time
import random

pygame.init()

white = (255 , 255, 255)
black = ( 0 , 0 , 0 )
red = (255, 0 , 0 )
green = (0 , 255, 0)
blue = (0 , 0, 255)


screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width , screen_height))

pygame.display.set_caption('Snek')

clock = pygame.time.Clock()

snek_block = 10
snek_speed = 20


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snek_block , snek_list):
    for x in snek_list:
        pygame.draw.rect(screen, green, [int(x[0]), int(x[1]), snek_block, snek_block])


def message(msg , color):
    mesg = font_style.render(msg , True , red)
    screen.blit(mesg, [int(screen_width/3) , int(screen_height/3)])


def game_loop():
    game_over = False
    game_close = False

    snek_x = screen_width/2
    snek_y = screen_height/2

    x_change = 0
    y_change = 0

    snek_list   = []
    length_of_snek = 1
    food_x = round(random.randrange(0 , screen_width - snek_block) / 10) * 10
    food_y = round(random.randrange(0 , screen_height - snek_block)/10) * 10

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snek_block
                    y_change = 0

                if event.key == pygame.K_RIGHT:
                    x_change = snek_block
                    y_change = 0

                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snek_block

                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snek_block

        if snek_x < 0:
            snek_x = screen_width
        if snek_x > screen_width:
            snek_x = 0
        if snek_y < 0:
            snek_y = screen_height
        if snek_y > screen_height:
            snek_y = 0

        snek_x += x_change
        snek_y += y_change

        screen.fill(black)

        pygame.draw.rect(screen , red , [int(food_x) , int(food_y) , snek_block , snek_block])

        snek_head = []
        snek_head.append(snek_x)
        snek_head.append(snek_y)
        snek_list.append(snek_head)

        if len(snek_list) > length_of_snek:
                del snek_list[0]

        for x in snek_list[:-1]:
            if x == snek_head:
                game_close = True

        our_snake(snek_block, snek_list)

        pygame.display.update()
        if (snek_x == food_x and snek_y == food_y):
            food_x = round(random.randrange(0, screen_width - snek_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snek_block) / 10.0) * 10.0
            length_of_snek += 1

        clock.tick(snek_speed)

    pygame.quit()
    quit()


game_loop()
