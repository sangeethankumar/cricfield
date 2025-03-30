from domain.constants import TEXT_COLOR, BASE_FIELD_POSITIONS
import pygame
import math

class HUDRenderer:
    def __init__(self, font):
        self.font = font

    def draw(self, screen, fielders, max_players, max_outer, field_center, inner_ring_radius, handedness, field_radius):
        total = len(fielders)
        outer = sum(
            ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) > inner_ring_radius ** 2
            for f in fielders
        )

        # HUD header lines
        hud_lines = [
            f"Batter: {handedness}",
            f"Players placed: {total+2} / {max_players}",
            f"Outer fielders: {outer} / {max_outer}",
            "Arrow keys to move | Esc to quit"
        ]

        for i, line in enumerate(hud_lines):
            text = self.font.render(line, True, TEXT_COLOR)
            screen.blit(text, (15, 15 + i * 25))

        # Position checklist
        flip_x = handedness == "LHB"
        start_y = 15 + len(hud_lines) * 25 + 20
        radius = field_radius

        for i, (label, angle_deg, frac) in enumerate(BASE_FIELD_POSITIONS):
            angle_rad = math.radians(angle_deg)
            dx = math.sin(angle_rad) * radius * frac
            dy = math.cos(angle_rad) * radius * frac
            if flip_x:
                dx = -dx
            px = field_center[0] + dx
            py = field_center[1] + dy

            # Check if any fielder is close to this position
            occupied = any(
                math.hypot(f["x"] - px, f["y"] - py) <= 15  # Adjust radius tolerance as needed
                for f in fielders
            )

            color = (0, 200, 0) if occupied else (200, 0, 0)
            label_text = self.font.render(label, True, color)
            screen.blit(label_text, (15, start_y + i * 20))
