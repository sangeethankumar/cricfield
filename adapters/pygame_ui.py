import pygame
from domain import constants, config
from core.fielder_logic import FielderLogic
from adapters.fielder_drawer import FielderDrawer
from adapters.cricfield_design import FieldRenderer
from adapters.hud_renderer import HUDRenderer  


def run_game(fullscreen=True):
    pygame.init()

    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((1000, 700))

    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("CricField")

    pygame.font.init()
    font = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE, bold=True)

    # Geometry
    field_center = (WIDTH // 2, HEIGHT // 2)
    field_radius = HEIGHT // constants.FIELD_RADIUS_FACTOR
    inner_ring_radius = HEIGHT // constants.INNER_RING_RADIUS_FACTOR
    pitch_width = WIDTH // constants.PITCH_WIDTH_FACTOR
    pitch_height = HEIGHT // constants.PITCH_HEIGHT_FACTOR

    pitch_rect = pygame.Rect(0, 0, pitch_width, pitch_height)
    pitch_rect.center = field_center

    # Initialize helpers
    logic = FielderLogic()
    renderer = FielderDrawer()
    field_renderer = FieldRenderer(
        field_center,
        field_radius,
        inner_ring_radius,
        pitch_rect,
        constants.BALL_RADIUS
    )
    hud = HUDRenderer(font)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(constants.BACKGROUND_COLOR)

        field_renderer.draw(screen, font)

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
        logic.move_selected(keys, field_center, field_radius, inner_ring_radius)

        # Draw fielders and HUD
        fielders = logic.get_fielders()
        renderer.draw_fielders(screen, fielders)

        hud.draw(
            screen,
            fielders,
            max_players=config.NUM_PLAYERS,
            max_outer=config.NUM_OUTER_RING_PLAYERS,
            field_center=field_center,
            inner_ring_radius=inner_ring_radius
        )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    exit()
