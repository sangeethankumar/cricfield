"""
Settings Menu for CricField.

This module provides a user interface to customize game settings such as:
- Number of players
- Number of outer fielders
- Game speed
- Batter handedness (Right or Left)
- Fullscreen toggle

The settings are applied globally before launching the game loop.
"""

import pygame
import pygame_menu
from cricfield.adapters.pygame_ui import run_game
from cricfield.domain import config, constants


# Holds selected configuration values
game_config = {
    "num_players": 11,
    "outer_fielders": 4,
    "speed": 5,
    "fullscreen": True,
    "batter_handedness": "RHB"
}

# Internal UI references
menu = None
inner_slider_index = None

def run_settings_menu():
    """
    Launch the CricField settings menu using pygame-menu.

    This menu allows users to configure core gameplay options before launching
    the main game. Handles UI creation and event loop.
    """
    global menu, inner_slider_index

    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("CricField Settings")

    menu = pygame_menu.Menu("CricField Settings", 600, 400,
                            theme=pygame_menu.themes.THEME_BLUE)

    # Player count setting
    menu.add.range_slider(
        "Total Players",
        default=game_config["num_players"],
        range_values=(2, 11),
        increment=1,
        value_format=lambda v: str(int(v)),
        onchange=update_num_players
    )

    # Outer fielder count (depends on player count)
    inner_slider_index = len(menu._widgets)
    add_outer_fielder_slider(max_value=game_config["num_players"] - 2)

    # Game speed
    menu.add.range_slider(
        "Speed",
        default=game_config["speed"],
        range_values=(1, 10),
        increment=1,
        value_format=lambda v: str(int(v)),
        onchange=lambda val: update("speed", val)
    )

    # Fullscreen mode
    menu.add.selector(
        "Fullscreen: ",
        [("Yes", True), ("No", False)],
        onchange=lambda _, val: update("fullscreen", val)
    )

    # Batter handedness
    menu.add.selector(
        "Batter: ",
        [("Right-Handed", "RHB"), ("Left-Handed", "LHB")],
        onchange=lambda _, val: update("batter_handedness", val)
    )

    # Start and exit buttons
    menu.add.button("Start Game", start_game)
    menu.add.button("Quit", pygame_menu.events.EXIT)

    try:
        menu.mainloop(surface)
    except Exception:
        pass


def update_num_players(value):
    """
    Updates the number of players and dynamically adjusts outer fielder range.

    Args:
        value (int): New total player count from slider input.
    """
    game_config["num_players"] = int(value)
    max_outer = game_config["num_players"] - 2
    add_outer_fielder_slider(max_value=max_outer)


def add_outer_fielder_slider(max_value):
    """
    Updates or creates the outer fielders slider with a new maximum value.

    Args:
        max_value (int): The maximum number of outer fielders allowed.
    """
    global menu, inner_slider_index

    # Remove existing slider (if present)
    if len(menu._widgets) > inner_slider_index:
        menu.remove_widget(menu._widgets[inner_slider_index])

    # Add new slider with updated range
    slider = menu.add.range_slider(
        "Outer Fielders",
        default=min(game_config["outer_fielders"], max_value),
        range_values=(0, max_value),
        increment=1,
        value_format=lambda v: str(int(v)),
        onchange=lambda val: update("outer_fielders", val)
    )

    # Ensure it appears at the right place in the menu
    menu._widgets.insert(inner_slider_index, menu._widgets.pop())


def update(key, value):
    """
    Updates the game_config dictionary with validated value.

    Args:
        key (str): Configuration key to update.
        value (Any): New value to assign (converted to int if float).
    """
    game_config[key] = int(value) if isinstance(value, float) else value


def start_game():
    """
    Applies selected settings to the game's configuration and launches CricField.
    """

    config.NUM_PLAYERS = game_config["num_players"]
    config.NUM_OUTER_RING_PLAYERS = game_config["outer_fielders"]
    constants.SPEED = game_config["speed"]
    config.BATTER_HANDEDNESS = game_config["batter_handedness"]

    run_game(fullscreen=game_config["fullscreen"])
