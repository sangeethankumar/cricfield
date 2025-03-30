import pygame
from domain import constants
from core import fielder_logic
from adapters.cricfield_design import draw_static_elements
from adapters.fielder_drawer import draw_fielders

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("CricField")

    pygame.font.init()
    font = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE, bold=True)

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

        draw_static_elements(screen, FIELD_CENTER, FIELD_RADIUS, INNER_RING_RADIUS,
                             PITCH_RECT, constants.BALL_RADIUS, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                fielder_logic.handle_click(event.pos, FIELD_CENTER, FIELD_RADIUS, INNER_RING_RADIUS)

        keys_pressed = pygame.key.get_pressed()
        keys = {
            "up": keys_pressed[pygame.K_UP],
            "down": keys_pressed[pygame.K_DOWN],
            "left": keys_pressed[pygame.K_LEFT],
            "right": keys_pressed[pygame.K_RIGHT]
        }

        fielder_logic.move_selected(keys, FIELD_CENTER, FIELD_RADIUS)
        draw_fielders(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
