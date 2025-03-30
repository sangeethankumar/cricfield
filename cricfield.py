import math
import pygame

pygame.init()

NUM_PLAYERS = 11

def draw_dashed_circle(surface, color, center, radius, dash_length=10, gap_length=10, width=1):
    total_circumference = 2 * math.pi * radius
    dash_count = int(total_circumference // (dash_length + gap_length))

    for i in range(dash_count):
        start_angle = (i * (dash_length + gap_length)) / radius
        end_angle = start_angle + dash_length / radius
        pygame.draw.arc(surface, color, 
                        (center[0] - radius, center[1] - radius, radius * 2, radius * 2), 
                        start_angle, end_angle, width)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("CricField")

pygame.font.init()
font = pygame.font.SysFont("Arial", 20, bold=True)

ball_radius = 10
ball_color = (255, 255, 255)
static_ball_color = (255, 215, 0)  
speed = 5
clock = pygame.time.Clock()

field_center = (width // 2, height // 2)
field_radius = height // 2
inner_ring_radius = height // 4
pitch_width = width // 15
pitch_height = height // 4

balls = []

running = True
while running:
    screen.fill((200, 220, 255))

    pygame.draw.circle(screen, (0, 100, 0), field_center, field_radius, 0)

    draw_dashed_circle(screen, (255, 255, 255), field_center, inner_ring_radius, dash_length=15, gap_length=10, width=3)

    pitch_rect = pygame.Rect(0, 0, pitch_width, pitch_height)
    pitch_rect.center = field_center
    pygame.draw.rect(screen, (150, 75, 0), pitch_rect)

    top_of_pitch = (pitch_rect.centerx, pitch_rect.top)
    bottom_of_pitch = (pitch_rect.centerx, pitch_rect.bottom)

    pygame.draw.circle(screen, static_ball_color, top_of_pitch, ball_radius)
    pygame.draw.circle(screen, static_ball_color, bottom_of_pitch, ball_radius)

    wk_text = font.render("WK", True, (0, 0, 0))
    bowler_text = font.render("Bowler", True, (0, 0, 0))
    screen.blit(wk_text, (top_of_pitch[0] - wk_text.get_width() // 2, top_of_pitch[1] - 25))
    screen.blit(bowler_text, (bottom_of_pitch[0] - bowler_text.get_width() // 2, bottom_of_pitch[1] + 10))

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
