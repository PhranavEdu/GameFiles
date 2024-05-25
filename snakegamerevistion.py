import pygame
import random
pygame.init()

print(pygame.init())
width = 1200
height = 600
gamewindow=pygame.display.set_mode((width,height))
game_exit=False
while not game_exit:
    pass
pygame.quit()
quit()

pygame.display.set_caption("SNAKE GAME")
while not game_exit:
    for event in pygame,event.get():
        if event.type==pygampygame.display.e.QUIT:
            game_exit=True
#Setting mouse visibility:
pygame.mouse.set_visible(True)

#Setting Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


gamewindow.fill(blue)
pygame.display.flip()
#Background Image
img=pygame.image.load("bg.jpg")
img=pygame.transform.scale(img,(width,height))
game.window.blit(img,(0,0))
pygame.display.flip()
exit_game=False
game_over=False
snake_x=150
snake_y=100
i=20
w=20
pygame.draw.rect(gamewondow,red,[snake_x,snake_y,i,w])
pygame.display.update()
fps=5
clock=pygame.time.Clock

if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
#Velocity
velocity_x=10
velocity_y=10
snake_x=snake_x+velocity_y
snake_y=snake_y+velocity_y

#Food
foodx=random.randint(0,Screen_Width)
foody=random.randint(0,screen_height)
pygame.draw.rect(gamewindow,white,[foodx,foody,snake_size,snakesize])

if abs(snake_x_food_food_x)<30 and abs(snake_y_food_y)<30:
      score=score+2
      print("SCORE: ", score)
food_x=random.randint(20,screenwidth-5)
food_y=random.randint(20,screenheight-5)

if snake_x<0 or snake_x>screendwidth or snake_y<0 or snake_y>screen_height:
      game_over=True
      plot_snake(gamewindow,snk_list,snake_size)

