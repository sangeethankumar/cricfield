import pygame
from domain import constants
from core.fielder_logic import FielderLogic
from adapters.fielder_drawer import FielderDrawer
from adapters.cricfield_design import draw_static_elements

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("CricField")

    pygame.font.init()
    font = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE, bold=True)

    field_center = (WIDTH // 2, HEIGHT // 2)
    field_radius = HEIGHT // constants.FIELD_RADIUS_FACTOR
    inner_ring_radius = HEIGHT // constants.INNER_RING_RADIUS_FACTOR
    pitch_width = WIDTH // constants.PITCH_WIDTH_FACTOR
    pitch_height = HEIGHT // constants.PITCH_HEIGHT_FACTOR

    pitch_rect = pygame.Rect(0, 0, pitch_width, pitch_height)
    pitch_rect.center = field_center

    logic = FielderLogic()
    renderer = FielderDrawer()
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(constants.BACKGROUND_COLOR)

        draw_static_elements(screen, field_center, field_radius, inner_ring_radius,
                             pitch_rect, constants.BALL_RADIUS, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                logic.handle_click(event.pos, field_center, field_radius, inner_ring_radius)

        keys_pressed = pygame.key.get_pressed()
        keys = {
            "up": keys_pressed[pygame.K_UP],
            "down": keys_pressed[pygame.K_DOWN],
            "left": keys_pressed[pygame.K_LEFT],
            "right": keys_pressed[pygame.K_RIGHT]
        }

        logic.move_selected(keys, field_center, field_radius)
        renderer.draw_fielders(screen, logic.get_fielders())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
