"""
Field rendering module for CricField.

This module defines the FieldRenderer class, which draws static elements of the cricket field
such as the outer boundary, inner ring, pitch, stumps, creases, and reference fielding positions
based on batter handedness.
"""

import pygame
import math
from domain import constants, config

class FieldRenderer:
    """
    Responsible for rendering static elements of the cricket field using Pygame.
    """

    def __init__(self, field_center, field_radius, inner_ring_radius, pitch_rect, ball_radius):
        """
        Initializes the FieldRenderer with key layout and sizing values.

        Args:
            field_center (tuple): Center coordinates of the field (x, y).
            field_radius (int): Radius of the outer field boundary.
            inner_ring_radius (int): Radius of the inner circle.
            pitch_rect (pygame.Rect): Rectangular area for the pitch.
            ball_radius (int): Radius for drawing player position indicators.
        """
        self.center = field_center
        self.radius = field_radius
        self.inner_radius = inner_ring_radius
        self.pitch = pitch_rect
        self.ball_radius = ball_radius

    def draw(self, screen, font):
        """
        Draws the entire field layout including all static components.

        Args:
            screen (pygame.Surface): Pygame surface to draw onto.
            font (pygame.font.Font): Font object used to render labels.
        """
        self._draw_field(screen)
        self._draw_inner_ring(screen)
        self._draw_pitch(screen)
        self._draw_creases(screen)
        self._draw_static_players(screen)
        self._draw_stumps(screen)
        self._draw_labels(screen, font)
        self._draw_common_positions(screen, font)

    def _draw_field(self, screen):
        """
        Draws the outer circular field boundary.

        Args:
            screen (pygame.Surface): Surface to draw on.
        """
        pygame.draw.circle(screen, constants.FIELD_COLOR, self.center, self.radius)

    def _draw_inner_ring(self, screen):
        """
        Draws the dashed inner circle to represent the inner ring.

        Args:
            screen (pygame.Surface): Surface to draw on.
        """
        total_circ = 2 * math.pi * self.inner_radius
        dash_len, gap_len = 15, 10
        dash_count = int(total_circ // (dash_len + gap_len))
        for i in range(dash_count):
            start_angle = (i * (dash_len + gap_len)) / self.inner_radius
            end_angle = start_angle + dash_len / self.inner_radius
            pygame.draw.arc(screen, constants.DASH_COLOR,
                            (self.center[0] - self.inner_radius, self.center[1] - self.inner_radius,
                             self.inner_radius * 2, self.inner_radius * 2),
                            start_angle, end_angle, 3)

    def _draw_pitch(self, screen):
        """
        Draws the central pitch rectangle.

        Args:
            screen (pygame.Surface): Surface to draw on.
        """
        pygame.draw.rect(screen, constants.PITCH_COLOR, self.pitch)

    def _draw_creases(self, screen):
        """
        Draws the creases on the top and bottom ends of the pitch.

        Args:
            screen (pygame.Surface): Surface to draw on.
        """
        offset = 25
        half = self.pitch.width // 2 + 10
        top = self.pitch.top + offset
        bottom = self.pitch.bottom - offset
        pygame.draw.line(screen, constants.BORDER_COLOR, (self.center[0] - half, top),
                         (self.center[0] + half, top), 2)
        pygame.draw.line(screen, constants.BORDER_COLOR, (self.center[0] - half, bottom),
                         (self.center[0] + half, bottom), 2)

    def _draw_static_players(self, screen):
        """
        Draws the static bowler and wicketkeeper positions as filled circles.

        Args:
            screen (pygame.Surface): Surface to draw on.
        """
        top = (self.pitch.centerx, self.pitch.top)
        bottom = (self.pitch.centerx, self.pitch.bottom)
        pygame.draw.circle(screen, constants.STATIC_BALL_COLOR, top, self.ball_radius)
        pygame.draw.circle(screen, constants.STATIC_BALL_COLOR, bottom, self.ball_radius)

    def _draw_stumps(self, screen):
        """
        Draws stumps at both ends of the pitch.

        Args:
            screen (pygame.Surface): Surface to draw on.
        """
        def draw_stump_set(base_x, base_y, up=True):
            width = 2
            height = 12
            spacing = 6
            for i in range(-1, 2):
                x = base_x + i * spacing
                y1 = base_y
                y2 = base_y - height if up else base_y + height
                pygame.draw.line(screen, constants.BORDER_COLOR, (x, y1), (x, y2), width)

        draw_stump_set(self.pitch.centerx, self.pitch.top, up=False)
        draw_stump_set(self.pitch.centerx, self.pitch.bottom, up=True)

    def _draw_labels(self, screen, font):
        """
        Draws labels for the WK and Bowler above and below the pitch.

        Args:
            screen (pygame.Surface): Surface to draw on.
            font (pygame.font.Font): Font for text rendering.
        """
        mid_x = self.pitch.centerx
        top_y = self.pitch.top
        bot_y = self.pitch.bottom

        wk = font.render("WK", True, constants.TEXT_COLOR)
        bowler = font.render("Bowler", True, constants.TEXT_COLOR)

        screen.blit(wk, (mid_x - wk.get_width() // 2, top_y - 25))
        screen.blit(bowler, (mid_x - bowler.get_width() // 2, bot_y + 10))

    def _draw_common_positions(self, screen, font):
        """
        Draws outlines and labels for commonly used fielding positions.

        Field positions are flipped horizontally for left-handed batters.

        Args:
            screen (pygame.Surface): Surface to draw on.
            font (pygame.font.Font): Font for label rendering.
        """
        flip_x = config.BATTER_HANDEDNESS == "LHB"
        positions = []

        for label, angle_deg, frac in constants.BASE_FIELD_POSITIONS:
            angle_rad = math.radians(angle_deg)

            dx = math.sin(angle_rad) * self.radius * frac
            dy = math.cos(angle_rad) * self.radius * frac

            if flip_x:
                dx = -dx

            x = int(self.center[0] + dx)
            y = int(self.center[1] + dy)
            positions.append((label, x, y))

        for label, x, y in positions:
            pygame.draw.circle(screen, (180, 180, 180), (x, y), self.ball_radius, 2)
            text = font.render(label, True, (100, 100, 100))
            screen.blit(text, (x - text.get_width() // 2, y - text.get_height() - 5))
