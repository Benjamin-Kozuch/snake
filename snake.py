import pygame
pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  

clock = pygame.time.Clock()


#Game Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255)) 

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(50, 50, 10, 10))

    pygame.display.flip()
    
    clock.tick(120)