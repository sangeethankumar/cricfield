# Gameplay speed and ball size
SPEED = 5
BALL_RADIUS = 10

# Dimension scaling factors
PITCH_WIDTH_FACTOR = 15
PITCH_HEIGHT_FACTOR = 4
INNER_RING_RADIUS_FACTOR = 4
FIELD_RADIUS_FACTOR = 2

# Colors
BALL_COLOR = (255, 255, 255)
STATIC_BALL_COLOR = (255, 215, 0)
HIGHLIGHT_COLOR = (255, 0, 0)
BORDER_COLOR = (0, 0, 0)
FIELD_COLOR = (0, 100, 0)
BACKGROUND_COLOR = (200, 220, 255)
DASH_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
PITCH_COLOR = (150, 75, 0)

# Font settings
FONT_NAME = "Arial"
FONT_SIZE = 20

# Common fielding positions: (Label, Angle in degrees, Distance fraction of field radius)
BASE_FIELD_POSITIONS = [
    ("Third Man", -135, 0.95),
    ("Point", -110, 0.5),
    ("Cover", -90, 0.5),
    ("Mid-Off", -45, 0.5),
    ("Mid-On", 45, 0.5),
    ("Mid-Wicket", 90, 0.5),
    ("Square Leg", 110, 0.5),
    ("Fine Leg", 135, 0.95),
]
