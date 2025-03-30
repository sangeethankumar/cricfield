# fielders.py

import pygame
import config

fielders = [] 

def handle_mouse_click(pos, field_center, field_radius):
    mouse_x, mouse_y = pos
    dx = mouse_x - field_center[0]
    dy = mouse_y - field_center[1]
    distance_squared = dx * dx + dy * dy

    if distance_squared <= (field_radius - config.BALL_RADIUS) ** 2:
        if len(fielders) < config.NUM_PLAYERS - 2:
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
                if dist_sq <= config.BALL_RADIUS ** 2:
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
                new_y += config.SPEED
            if keys[pygame.K_UP]:
                new_y -= config.SPEED
            if keys[pygame.K_LEFT]:
                new_x -= config.SPEED
            if keys[pygame.K_RIGHT]:
                new_x += config.SPEED

            dx = new_x - field_center[0]
            dy = new_y - field_center[1]
            distance_squared = dx * dx + dy * dy
            if distance_squared <= (field_radius - config.BALL_RADIUS) ** 2:
                ball["x"], ball["y"] = new_x, new_y

def draw_fielders(screen):
    for ball in fielders:
        pygame.draw.circle(screen, config.BALL_COLOR, (int(ball["x"]), int(ball["y"])), config.BALL_RADIUS)

        if ball["selected"]:
            pygame.draw.circle(screen, config.HIGHLIGHT_COLOR, (int(ball["x"]), int(ball["y"])), config.BALL_RADIUS)
            pygame.draw.circle(screen, config.BORDER_COLOR, (int(ball["x"]), int(ball["y"])), config.BALL_RADIUS + 3, 2)
