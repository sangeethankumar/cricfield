import pygame
from cricfield_design import draw_static_elements
import config
import fielders

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
            fielders.handle_mouse_click(event.pos, FIELD_CENTER, FIELD_RADIUS, INNER_RING_RADIUS)

    keys = pygame.key.get_pressed()
    fielders.move_selected(keys, FIELD_CENTER, FIELD_RADIUS)
    fielders.draw_fielders(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
