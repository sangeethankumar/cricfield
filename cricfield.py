import pygame
from cricfield_design import draw_static_elements
import config  # Import constants

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("CricField")

pygame.font.init()
FONT = pygame.font.SysFont(config.FONT_NAME, config.FONT_SIZE, bold=True)

FIELD_CENTER = (WIDTH // 2, HEIGHT // 2)
FIELD_RADIUS = HEIGHT // config.FIELD_RADIUS_FACTOR
INNER_RING_RADIUS = HEIGHT // config.INNER_RING_RADIUS_FACTOR
PITCH_WIDTH = WIDTH // config.PITCH_WIDTH_FACTOR
PITCH_HEIGHT = HEIGHT // config.PITCH_HEIGHT_FACTOR

PITCH_RECT = pygame.Rect(0, 0, PITCH_WIDTH, PITCH_HEIGHT)
PITCH_RECT.center = FIELD_CENTER

balls = []
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(config.BACKGROUND_COLOR)

    draw_static_elements(
        screen,
        FIELD_CENTER,
        FIELD_RADIUS,
        INNER_RING_RADIUS,
        PITCH_RECT,
        config.BALL_RADIUS,
        FONT
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - FIELD_CENTER[0]
            dy = mouse_y - FIELD_CENTER[1]
            distance_squared = dx * dx + dy * dy

            if distance_squared <= (FIELD_RADIUS - config.BALL_RADIUS) ** 2:
                if len(balls) < config.NUM_PLAYERS - 2:
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
                        if dist_sq <= config.BALL_RADIUS ** 2:
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
                new_y += config.SPEED
            if keys[pygame.K_UP]:
                new_y -= config.SPEED
            if keys[pygame.K_LEFT]:
                new_x -= config.SPEED
            if keys[pygame.K_RIGHT]:
                new_x += config.SPEED

            dx = new_x - FIELD_CENTER[0]
            dy = new_y - FIELD_CENTER[1]
            distance_squared = dx * dx + dy * dy
            if distance_squared <= (FIELD_RADIUS - config.BALL_RADIUS) ** 2:
                ball["x"], ball["y"] = new_x, new_y

        pygame.draw.circle(screen, config.BALL_COLOR, (int(ball["x"]), int(ball["y"])), config.BALL_RADIUS)

        if ball["selected"]:
            pygame.draw.circle(screen, config.HIGHLIGHT_COLOR, (int(ball["x"]), int(ball["y"])), config.BALL_RADIUS)
            pygame.draw.circle(screen, config.BORDER_COLOR, (int(ball["x"]), int(ball["y"])), config.BALL_RADIUS + 3, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
