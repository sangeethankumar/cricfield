import pygame
import config
import constants

fielders = []

def handle_mouse_click(pos, field_center, field_radius, inner_ring_radius):
    mouse_x, mouse_y = pos
    dx = mouse_x - field_center[0]
    dy = mouse_y - field_center[1]
    distance_squared = dx * dx + dy * dy

    if distance_squared <= (field_radius - constants.BALL_RADIUS) ** 2:
        if len(fielders) < config.NUM_PLAYERS - 2:
            is_outside_inner_ring = distance_squared > inner_ring_radius ** 2

            outer_count = sum(
                ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) > inner_ring_radius ** 2
                for f in fielders
            )

            if is_outside_inner_ring and outer_count >= config.NUM_OUTER_RING_PLAYERS:
                return

            fielders.append({
                "x": mouse_x,
                "y": mouse_y,
                "selected": False
            })

        else:
            clicked_on_any = False
            for ball in fielders:
                dx = mouse_x - ball["x"]
                dy = mouse_y - ball["y"]
                dist_sq = dx * dx + dy * dy
                if dist_sq <= constants.BALL_RADIUS ** 2:
                    clicked_on_any = True
                    for b in fielders:
                        b["selected"] = False
                    ball["selected"] = True
                    break
            if not clicked_on_any:
                for ball in fielders:
                    ball["selected"] = False


def move_selected(keys, field_center, field_radius):
    for ball in fielders:
        if ball["selected"]:
            new_x, new_y = ball["x"], ball["y"]

            if keys[pygame.K_DOWN]:
                new_y += constants.SPEED
            if keys[pygame.K_UP]:
                new_y -= constants.SPEED
            if keys[pygame.K_LEFT]:
                new_x -= constants.SPEED
            if keys[pygame.K_RIGHT]:
                new_x += constants.SPEED

            dx = new_x - field_center[0]
            dy = new_y - field_center[1]
            distance_squared = dx * dx + dy * dy

            if distance_squared <= (field_radius - constants.BALL_RADIUS) ** 2:
                ball["x"], ball["y"] = new_x, new_y


def draw_fielders(screen):
    for ball in fielders:
        pygame.draw.circle(
            screen, constants.BALL_COLOR, (int(ball["x"]), int(ball["y"])), constants.BALL_RADIUS
        )
        if ball["selected"]:
            pygame.draw.circle(
                screen, constants.HIGHLIGHT_COLOR, (int(ball["x"]), int(ball["y"])), constants.BALL_RADIUS
            )
            pygame.draw.circle(
                screen, constants.BORDER_COLOR, (int(ball["x"]), int(ball["y"])), constants.BALL_RADIUS + 3, 2
            )
