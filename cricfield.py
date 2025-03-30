import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CricField")

ball_radius = 20
ball_color = (255, 255, 255)
speed = 5
clock = pygame.time.Clock()

balls = [
    {"x": width // 3, "y": height // 2, "selected": False},
    {"x": 2 * width // 3, "y": height // 2, "selected": False}
]

running = True
while running:
    screen.fill((200, 220, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            clicked_on_any = False

            for ball in balls:
                dx = mouse_x - ball["x"]
                dy = mouse_y - ball["y"]
                distance_squared = dx * dx + dy * dy

                if distance_squared <= ball_radius * ball_radius:
                    clicked_on_any = True
                    for b in balls:
                        b["selected"] = False
                    ball["selected"] = True
                    break  

            if not clicked_on_any:
                for ball in balls:
                    ball["selected"] = False
                        

    keys = pygame.key.get_pressed()
    for ball in balls:
        if ball["selected"]:
            if keys[pygame.K_DOWN]:
                ball["y"] += speed
            if keys[pygame.K_UP]:
                ball["y"] -= speed
            if keys[pygame.K_LEFT]:
                ball["x"] -= speed
            if keys[pygame.K_RIGHT]:
                ball["x"] += speed

        ball["x"] = max(ball_radius, min(width - ball_radius, ball["x"]))
        ball["y"] = max(ball_radius, min(height - ball_radius, ball["y"]))

        pygame.draw.circle(screen, ball_color, (ball["x"], ball["y"]), ball_radius)

        if ball["selected"]:
            pygame.draw.circle(screen, (255, 0, 0), (ball["x"], ball["y"]), ball_radius)
            pygame.draw.circle(screen, (0, 0, 0), (ball["x"], ball["y"]), ball_radius + 3, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
