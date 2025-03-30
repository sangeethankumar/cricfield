import pygame

pygame.init()

NUM_PLAYERS = 11

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("CricField")

ball_radius = 20
ball_color = (255, 255, 255)
speed = 5
clock = pygame.time.Clock()

field_center = (width // 2, height // 2)
field_radius = height // 2

balls = []

running = True
while running:
    screen.fill((200, 220, 255))

    pygame.draw.circle(screen, (0, 100, 0), field_center, field_radius, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - field_center[0]
            dy = mouse_y - field_center[1]
            distance_squared = dx * dx + dy * dy

            if distance_squared <= (field_radius - ball_radius) ** 2:
                if len(balls) < NUM_PLAYERS - 2:
                    balls.append({
                        "x": mouse_x,
                        "y": mouse_y,
                        "selected": False
                    })
                else:
                    clicked_on_any = False
                    for ball in balls:
                        dx = mouse_x - ball["x"]
                        dy = mouse_y - ball["y"]
                        dist_sq = dx * dx + dy * dy

                        if dist_sq <= ball_radius * ball_radius:
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
            new_x, new_y = ball["x"], ball["y"]

            if keys[pygame.K_DOWN]:
                new_y += speed
            if keys[pygame.K_UP]:
                new_y -= speed
            if keys[pygame.K_LEFT]:
                new_x -= speed
            if keys[pygame.K_RIGHT]:
                new_x += speed

            dx = new_x - field_center[0]
            dy = new_y - field_center[1]
            distance_squared = dx * dx + dy * dy

            if distance_squared <= (field_radius - ball_radius) ** 2:
                ball["x"], ball["y"] = new_x, new_y

        pygame.draw.circle(screen, ball_color, (int(ball["x"]), int(ball["y"])), ball_radius)

        if ball["selected"]:
            pygame.draw.circle(screen, (255, 0, 0), (int(ball["x"]), int(ball["y"])), ball_radius)
            pygame.draw.circle(screen, (0, 0, 0), (int(ball["x"]), int(ball["y"])), ball_radius + 3, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
