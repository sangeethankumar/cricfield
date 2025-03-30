import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CricField")

ball_color = (255, 0, 0)
ball_radius = 20

xpos = width // 2
ypos = height // 2
speed = 5

selected = False  # Ball is not selected initially

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((200, 220, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - xpos
            dy = mouse_y - ypos
            distance_squared = dx * dx + dy * dy

            selected = distance_squared <= ball_radius * ball_radius


    keys = pygame.key.get_pressed()
    if selected:
        if keys[pygame.K_DOWN]:
            ypos += speed
        if keys[pygame.K_UP]:
            ypos -= speed
        if keys[pygame.K_LEFT]:
            xpos -= speed
        if keys[pygame.K_RIGHT]:
            xpos += speed

    xpos = max(ball_radius, min(width - ball_radius, xpos))
    ypos = max(ball_radius, min(height - ball_radius, ypos))

    pygame.draw.circle(screen, ball_color, (xpos, ypos), ball_radius)

    if selected:
        pygame.draw.circle(screen, (0, 0, 0), (xpos, ypos), ball_radius + 3, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
