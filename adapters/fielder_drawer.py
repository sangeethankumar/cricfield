import pygame
from domain import constants
from core import fielder_logic

def draw_fielders(screen):
    for f in fielder_logic.fielders:
        pygame.draw.circle(screen, constants.BALL_COLOR, (int(f["x"]), int(f["y"])), constants.BALL_RADIUS)
        if f["selected"]:
            pygame.draw.circle(screen, constants.HIGHLIGHT_COLOR, (int(f["x"]), int(f["y"])), constants.BALL_RADIUS)
            pygame.draw.circle(screen, constants.BORDER_COLOR, (int(f["x"]), int(f["y"])), constants.BALL_RADIUS + 3, 2)
