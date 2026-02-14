'''Write a Python Program to create your first game screen using the Pygame library
Window size(500,500)
Set Caption - My first game screen
Image size(300,300),positioned at the centre of the screen
The background Colour of the Screen-Grey(58,,58,58)'''

import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
BG_COLOR = (58, 58, 58)
IMG_SIZE = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen")

image_surface = pygame.Surface((IMG_SIZE, IMG_SIZE))
image_surface.fill((200, 200, 200)) 

img_x = (WIDTH - IMG_SIZE) // 2
img_y = (HEIGHT - IMG_SIZE) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(BG_COLOR)
    
    screen.blit(image_surface, (img_x, img_y))

    pygame.display.flip()
    
pygame.quit()