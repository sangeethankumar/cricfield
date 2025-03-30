import pygame
import pygame_menu
from adapters.pygame_ui import run_game

game_config = {
    "num_players": 11,
    "outer_fielders": 4,
    "speed": 5,
    "fullscreen": True,
    "batter_handedness": "RHB"
}

menu = None
inner_slider_index = None

def run_settings_menu():
    global menu, inner_slider_index

    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("CricField Settings")

    menu = pygame_menu.Menu("CricField Settings", 600, 400,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.range_slider(
        "Total Players",
        default=game_config["num_players"],
        range_values=(2, 11),
        increment=1,
        value_format=lambda v: str(int(v)),
        onchange=update_num_players
    )

    inner_slider_index = len(menu._widgets)
    add_outer_fielder_slider(max_value=game_config["num_players"] - 2)

    menu.add.range_slider(
        "Speed",
        default=game_config["speed"],
        range_values=(1, 10),
        increment=1,
        value_format=lambda v: str(int(v)),
        onchange=lambda val: update("speed", val)
    )

    menu.add.selector(
        "Fullscreen: ",
        [("Yes", True), ("No", False)],
        onchange=lambda _, val: update("fullscreen", val)
    )

    menu.add.selector(
        "Batter: ",
        [("Right-Handed", "RHB"), ("Left-Handed", "LHB")],
        onchange=lambda _, val: update("batter_handedness", val)
    )

    menu.add.button("Start Game", start_game)
    menu.add.button("Quit", pygame_menu.events.EXIT)

    try:
        menu.mainloop(surface)
    except Exception:
        pass


def update_num_players(value):
    game_config["num_players"] = int(value)
    max_outer = game_config["num_players"] - 2
    add_outer_fielder_slider(max_value=max_outer)


def add_outer_fielder_slider(max_value):
    global menu, inner_slider_index

    if len(menu._widgets) > inner_slider_index:
        menu.remove_widget(menu._widgets[inner_slider_index])

    slider = menu.add.range_slider(
        "Outer Fielders",
        default=min(game_config["outer_fielders"], max_value),
        range_values=(0, max_value),
        increment=1,
        value_format=lambda v: str(int(v)),
        onchange=lambda val: update("outer_fielders", val)
    )

    menu._widgets.insert(inner_slider_index, menu._widgets.pop())


def update(key, value):
    game_config[key] = int(value) if isinstance(value, float) else value


def start_game():
    from domain import config, constants

    config.NUM_PLAYERS = game_config["num_players"]
    config.NUM_OUTER_RING_PLAYERS = game_config["outer_fielders"]
    constants.SPEED = game_config["speed"]
    config.BATTER_HANDEDNESS = game_config["batter_handedness"]

    run_game(fullscreen=game_config["fullscreen"])
