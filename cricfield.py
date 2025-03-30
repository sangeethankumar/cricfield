import pygame
import config
import constants
import fielders
from cricfield_design import draw_static_elements

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("CricField")

pygame.font.init()
FONT = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE, bold=True)

FIELD_CENTER = (WIDTH // 2, HEIGHT // 2)
FIELD_RADIUS = HEIGHT // constants.FIELD_RADIUS_FACTOR
INNER_RING_RADIUS = HEIGHT // constants.INNER_RING_RADIUS_FACTOR
PITCH_WIDTH = WIDTH // constants.PITCH_WIDTH_FACTOR
PITCH_HEIGHT = HEIGHT // constants.PITCH_HEIGHT_FACTOR

PITCH_RECT = pygame.Rect(0, 0, PITCH_WIDTH, PITCH_HEIGHT)
PITCH_RECT.center = FIELD_CENTER

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(constants.BACKGROUND_COLOR)

    draw_static_elements(
        screen,
        FIELD_CENTER,
        FIELD_RADIUS,
        INNER_RING_RADIUS,
        PITCH_RECT,
        constants.BALL_RADIUS,
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
