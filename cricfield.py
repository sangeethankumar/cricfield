import pygame

pygame.init()

# screen properties
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CricField")

# ball properties
ball_color = (255, 0, 0)
ball_radius = 20

xpos_init = width // 2
ypos_init = height // 2

dh = 0
dw = 0
xpos = xpos_init
ypos = ypos_init

running = True
while running:
    # background color
    screen.fill((200, 220, 255))
    ball_position = (xpos, ypos)
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius )

    # loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            dh = 100
            ypos = ypos + dh if (ypos + dh) < width else ypos_init
        if keys[pygame.K_UP]:
            dh = -100
            ypos = ypos + dh if (ypos + dh) > 0 else ypos_init
        ball_position = (xpos, ypos)
        pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

    # update display
    pygame.display.flip()

pygame.quit()