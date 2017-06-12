import pygame
from scales import Snake, Scale
import random
import math

pygame.init()
screen_width = 200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))  
clock = pygame.time.Clock()

def create_food():
    x_random = math.floor(random.random() * screen_width) 
    y_random = math.floor(random.random() * screen_height)

    x_random -= (x_random % 10)
    y_random -= (y_random % 10)

    food = Scale(x_random, y_random)
    return food

snake = Snake()

#Game Loop
done = False
food_is_eaten = False
food = create_food()
count = 0

while not done:
    
    count+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Change Snake Direction
    if pygame.key.get_pressed()[pygame.K_UP]:
        if(snake.x_direction != 0 and snake.y_direction != 1):
            snake.x_direction = 0
            snake.y_direction = -1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if(snake.x_direction != 0 and snake.y_direction != -1):
            snake.x_direction = 0
            snake.y_direction = 1        
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if(snake.x_direction != 1 and snake.y_direction != 0):
            snake.x_direction = -1
            snake.y_direction = 0        
    if pygame.key.get_pressed()[pygame.K_RIGHT]: 
        if(snake.x_direction != -1 and snake.y_direction != 0):
            snake.x_direction = 1
            snake.y_direction = 0       

    #Create New Food if the old one has not been eaten
    if food_is_eaten:
        food = create_food()
        food_is_eaten = False

    #Move the Snake
    if count % 5 == 0: snake.move()
    
    #Check for collision with self
    for index, scale in reversed(list(enumerate(snake.scales))):
        if index >= 1:
            if snake.scales[0].x_position == snake.scales[index].x_position and snake.scales[0].y_position == snake.scales[index].y_position :
                done = True

    #Check for collision with walls
    if snake.scales[0].x_position < 0 or \
       snake.scales[0].x_position > screen_width - snake.scales[0].size or \
       snake.scales[0].y_position < 0 or \
       snake.scales[0].y_position > screen_height - snake.scales[0].size:
        done = True

    
    if snake.can_eat(food): #check for collision
        snake.eat(food)
        food_is_eaten = True
        #print (len(snake.scales))
    
    #Clear the previous screen
    screen.fill((0, 0, 0)) 
    
    #Draw Snake
    for scale in snake.scales:
        pygame.draw.rect(screen, (50,205,50), pygame.Rect(scale.x_position, scale.y_position, scale.size, scale.size))

    #Draw Food
    pygame.draw.rect(screen, (50,205,50), pygame.Rect(food.x_position, food.y_position, food.size, food.size))
    


    pygame.display.flip()
    clock.tick(60)




