



import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
score=0
# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(0, screen_width)
food_y = random.randint(0, screen_height)

snake_size = 30
fps = 30

clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])



def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_list=[]
snk_length=1
def gameloop():
    exit_game=False
    game_over=Falsesnake_y=55
    velocity_x=0
    velocity_y=0
    snk_list=[]
    snk_length=1
    food_x=random.randint(0,screen_width)
    food_y=random.randint(0,screen_height)
    score=0
    snake_size=5
    fps=30

    

while not exit_game:
    if game_over:
        gameWindow.fill(white)
        text_screen("game over")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - 10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - 10
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
       score +=1
    
       food_x = random.randint(0, screen_width)
       food_y = random.randint(0, screen_height)
       snk_length +=5
       
       
       
    gameWindow.fill(white)
    text_screen("score:"+str(score*10),red,5,5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list)>snk_length:
        del snk_list[0]
    if snake_x<0 or snake_x>screen_width or snake_y>screen_height:
        game_over=True
        print("game over")

    #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

