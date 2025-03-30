import pygame
import math
from domain import constants

class FieldRenderer:
    def __init__(self, field_center, field_radius, inner_ring_radius, pitch_rect, ball_radius):
        self.center = field_center
        self.radius = field_radius
        self.inner_radius = inner_ring_radius
        self.pitch = pitch_rect
        self.ball_radius = ball_radius

    def draw(self, screen, font):
        self._draw_field(screen)
        self._draw_inner_ring(screen)
        self._draw_pitch(screen)
        self._draw_creases(screen)
        self._draw_static_players(screen)
        self._draw_stumps(screen)
        self._draw_labels(screen, font)
        self._draw_common_positions(screen, font)

    def _draw_field(self, screen):
        pygame.draw.circle(screen, constants.FIELD_COLOR, self.center, self.radius)

    def _draw_inner_ring(self, screen):
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
        pygame.draw.rect(screen, constants.PITCH_COLOR, self.pitch)

    def _draw_creases(self, screen):
        offset = 25
        half = self.pitch.width // 2 + 10
        top = self.pitch.top + offset
        bottom = self.pitch.bottom - offset
        pygame.draw.line(screen, constants.BORDER_COLOR, (self.center[0] - half, top),
                         (self.center[0] + half, top), 2)
        pygame.draw.line(screen, constants.BORDER_COLOR, (self.center[0] - half, bottom),
                         (self.center[0] + half, bottom), 2)

    def _draw_static_players(self, screen):
        top = (self.pitch.centerx, self.pitch.top)
        bottom = (self.pitch.centerx, self.pitch.bottom)
        pygame.draw.circle(screen, constants.STATIC_BALL_COLOR, top, self.ball_radius)
        pygame.draw.circle(screen, constants.STATIC_BALL_COLOR, bottom, self.ball_radius)

    def _draw_stumps(self, screen):
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
        mid_x = self.pitch.centerx
        top_y = self.pitch.top
        bot_y = self.pitch.bottom

        wk = font.render("WK", True, constants.TEXT_COLOR)
        bowler = font.render("Bowler", True, constants.TEXT_COLOR)

        screen.blit(wk, (mid_x - wk.get_width() // 2, top_y - 25))
        screen.blit(bowler, (mid_x - bowler.get_width() // 2, bot_y + 10))

    def _draw_common_positions(self, screen, font):
        import math
        from domain import config

        base_positions = [
            ("Third Man", -135, 0.95),
            ("Point", -110, 0.5),
            ("Cover", -90, 0.5),
            ("Mid-Off", -45, 0.5),
            ("Mid-On", 45, 0.5),
            ("Mid-Wicket", 90, 0.5),
            ("Square Leg", 110, 0.5),
            ("Fine Leg", 135, 0.95),
        ]

        flip_x = config.BATTER_HANDEDNESS == "LHB"
        positions = []

        for label, angle_deg, frac in base_positions:
            angle_rad = math.radians(angle_deg)

            dx = math.sin(angle_rad) * self.radius * frac
            dy = math.cos(angle_rad) * self.radius * frac

            if flip_x:
                dx = -dx  # only flip x-axis for LHB

            x = int(self.center[0] + dx)
            y = int(self.center[1] + dy)
            positions.append((label, x, y))

        for label, x, y in positions:
            pygame.draw.circle(screen, (180, 180, 180), (x, y), self.ball_radius, 2)
            text = font.render(label, True, (100, 100, 100))
            screen.blit(text, (x - text.get_width() // 2, y - text.get_height() - 5))
