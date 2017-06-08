import pygame
import scales
import random
import math

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  
clock = pygame.time.Clock()

def create_food():
    x_random = math.floor(random.random() * screen_width) 
    y_random = math.floor(random.random() * screen_height)

    x_random -= (x_random % 10)
    y_random -= (y_random % 10)

    food = scales.Scale(x_random, y_random)
    return food

#Every snake starts off with a head and then grows a tail
snake = scales.Snake()

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
        snake.x_direction = 0
        snake.y_direction = -1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        snake.x_direction = 0
        snake.y_direction = 1        
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        snake.x_direction = -1
        snake.y_direction = 0        
    if pygame.key.get_pressed()[pygame.K_RIGHT]: 
        snake.x_direction = 1
        snake.y_direction = 0       

    #Create New Food if the old one has not been eaten
    if food_is_eaten:
        food = create_food()
        food_is_eaten = False

    #Move the Snake
    if count % 5 == 0: snake.move()
    
    if snake.can_eat(food): #check for collision
        snake.eat_and_grow(food)
        food_is_eaten = True
        print (len(snake.scales))
    
    #Clear the previous screen
    screen.fill((0, 0, 0)) 
    
    #Draw Snake
    for scale in snake.scales:
        pygame.draw.rect(screen, (50,205,50), pygame.Rect(scale.x_position, scale.y_position, scale.size, scale.size))

    #Draw Food
    pygame.draw.rect(screen, (50,205,50), pygame.Rect(food.x_position, food.y_position, food.size, food.size))
    


    pygame.display.flip()
    clock.tick(60)




