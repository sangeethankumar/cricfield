from domain import constants

class HUDRenderer:
    def __init__(self, font):
        self.font = font

    def draw(self, screen, fielders, max_players, max_outer, field_center, inner_ring_radius, handedness):
        total = len(fielders)
        outer = sum(
            ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) > inner_ring_radius ** 2
            for f in fielders
        )

        hud_lines = [
            f"Batter: {handedness}",
            f"Players placed: {total+2} / {max_players}",
            f"Outer fielders: {outer} / {max_outer}",
            "Arrow keys to move | Esc to quit"
        ]

        for i, line in enumerate(hud_lines):
            text = self.font.render(line, True, constants.TEXT_COLOR)
            screen.blit(text, (15, 15 + i * 25))
