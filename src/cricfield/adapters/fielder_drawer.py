"""
Fielder Renderer for CricField.

This module defines the FielderDrawer class, which is responsible for rendering
the fielders on the screen, including selection highlights.
"""

import pygame
from cricfield.domain import constants
from cricfield.core.interfaces import RendererInterface

class FielderDrawer(RendererInterface):
    """
    Renderer class for drawing player markers (fielders) on the field.

    Implements the RendererInterface used by the game loop to display active fielders.
    """

    def draw_fielders(self, screen, fielders):
        """
        Draws all fielders as circles, highlighting the selected one.

        Args:
            screen (pygame.Surface): The surface to draw fielders onto.
            fielders (list): List of dictionaries with keys:
                - "x": X coordinate of the fielder
                - "y": Y coordinate of the fielder
                - "selected": Boolean indicating if the fielder is currently selected
        """
        for f in fielders:
            pygame.draw.circle(
                screen,
                constants.BALL_COLOR,
                (int(f["x"]), int(f["y"])),
                constants.BALL_RADIUS
            )
            if f["selected"]:
                pygame.draw.circle(
                    screen,
                    constants.HIGHLIGHT_COLOR,
                    (int(f["x"]), int(f["y"])),
                    constants.BALL_RADIUS
                )
                pygame.draw.circle(
                    screen,
                    constants.BORDER_COLOR,
                    (int(f["x"]), int(f["y"])),
                    constants.BALL_RADIUS + 3,
                    2
                )
