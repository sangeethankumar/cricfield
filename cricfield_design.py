import pygame
import math

def draw_dashed_circle(surface, color, center, radius, dash_length=10, gap_length=10, width=1):
    total_circumference = 2 * math.pi * radius
    dash_count = int(total_circumference // (dash_length + gap_length))

    for i in range(dash_count):
        start_angle = (i * (dash_length + gap_length)) / radius
        end_angle = start_angle + dash_length / radius
        pygame.draw.arc(surface, color, 
                        (center[0] - radius, center[1] - radius, radius * 2, radius * 2), 
                        start_angle, end_angle, width)

def draw_static_elements(screen, field_center, field_radius, inner_ring_radius, pitch_rect, ball_radius, font):
    pygame.draw.circle(screen, (0, 100, 0), field_center, field_radius, 0)
    draw_dashed_circle(screen, (255, 255, 255), field_center, inner_ring_radius, dash_length=15, gap_length=10, width=3)

    pygame.draw.rect(screen, (150, 75, 0), pitch_rect)

    top_crease_y = pitch_rect.top + 25
    bottom_crease_y = pitch_rect.bottom - 25
    crease_half_len = pitch_rect.width // 2 + 10
    pygame.draw.line(screen, (0, 0, 0), (field_center[0] - crease_half_len, top_crease_y), (field_center[0] + crease_half_len, top_crease_y), 2)
    pygame.draw.line(screen, (0, 0, 0), (field_center[0] - crease_half_len, bottom_crease_y), (field_center[0] + crease_half_len, bottom_crease_y), 2)

    static_ball_color = (255, 215, 0)
    top_of_pitch = (pitch_rect.centerx, pitch_rect.top)
    bottom_of_pitch = (pitch_rect.centerx, pitch_rect.bottom)
    pygame.draw.circle(screen, static_ball_color, top_of_pitch, ball_radius)
    pygame.draw.circle(screen, static_ball_color, bottom_of_pitch, ball_radius)

    wk_text = font.render("WK", True, (0, 0, 0))
    bowler_text = font.render("Bowler", True, (0, 0, 0))
    screen.blit(wk_text, (top_of_pitch[0] - wk_text.get_width() // 2, top_of_pitch[1] - 25))
    screen.blit(bowler_text, (bottom_of_pitch[0] - bowler_text.get_width() // 2, bottom_of_pitch[1] + 10))
