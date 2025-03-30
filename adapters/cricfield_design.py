import pygame
import math
from domain import constants

def draw_dashed_circle(surface, color, center, radius, dash_length=10, gap_length=10, width=1):
    total_circumference = 2 * math.pi * radius
    dash_count = int(total_circumference // (dash_length + gap_length))
    for i in range(dash_count):
        start_angle = (i * (dash_length + gap_length)) / radius
        end_angle = start_angle + dash_length / radius
        pygame.draw.arc(surface, color,
                        (center[0] - radius, center[1] - radius, radius * 2, radius * 2),
                        start_angle, end_angle, width)

def draw_stumps(surface, base_x, base_y, up=True):
    width = 2
    height = 12
    spacing = 6
    for i in range(-1, 2):
        x = base_x + i * spacing
        y1 = base_y
        y2 = base_y - height if up else base_y + height
        pygame.draw.line(surface, constants.BORDER_COLOR, (x, y1), (x, y2), width)

def draw_static_elements(screen, field_center, field_radius, inner_ring_radius,
                         pitch_rect, ball_radius, font):
    pygame.draw.circle(screen, constants.FIELD_COLOR, field_center, field_radius)
    draw_dashed_circle(screen, constants.DASH_COLOR, field_center, inner_ring_radius, 15, 10, 3)
    pygame.draw.rect(screen, constants.PITCH_COLOR, pitch_rect)

    top = pitch_rect.top
    bottom = pitch_rect.bottom
    mid_x = pitch_rect.centerx

    # Creases
    offset = 25
    crease_half = pitch_rect.width // 2 + 10
    pygame.draw.line(screen, constants.BORDER_COLOR, (field_center[0] - crease_half, top + offset),
                     (field_center[0] + crease_half, top + offset), 2)
    pygame.draw.line(screen, constants.BORDER_COLOR, (field_center[0] - crease_half, bottom - offset),
                     (field_center[0] + crease_half, bottom - offset), 2)

    # WK & Bowler
    pygame.draw.circle(screen, constants.STATIC_BALL_COLOR, (mid_x, top), ball_radius)
    pygame.draw.circle(screen, constants.STATIC_BALL_COLOR, (mid_x, bottom), ball_radius)

    draw_stumps(screen, mid_x, top, up=False)
    draw_stumps(screen, mid_x, bottom, up=True)

    wk_text = font.render("WK", True, constants.TEXT_COLOR)
    bowler_text = font.render("Bowler", True, constants.TEXT_COLOR)
    screen.blit(wk_text, (mid_x - wk_text.get_width() // 2, top - 25))
    screen.blit(bowler_text, (mid_x - bowler_text.get_width() // 2, bottom + 10))
