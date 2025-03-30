from domain import config, constants

fielders = []

def handle_click(pos, field_center, field_radius, inner_ring_radius):
    x, y = pos
    dx, dy = x - field_center[0], y - field_center[1]
    dist_sq = dx ** 2 + dy ** 2

    if dist_sq > (field_radius - constants.BALL_RADIUS) ** 2:
        return

    if len(fielders) < config.NUM_PLAYERS - 2:
        is_outside = dist_sq > inner_ring_radius ** 2
        outer_count = sum(
            ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) > inner_ring_radius ** 2
            for f in fielders
        )
        if is_outside and outer_count >= config.NUM_OUTER_RING_PLAYERS:
            return

        fielders.append({"x": x, "y": y, "selected": False})
    else:
        for f in fielders:
            f["selected"] = False
        for f in fielders:
            dx = x - f["x"]
            dy = y - f["y"]
            if dx ** 2 + dy ** 2 <= constants.BALL_RADIUS ** 2:
                f["selected"] = True
                break

def move_selected(keys, field_center, field_radius):
    for f in fielders:
        if f["selected"]:
            new_x, new_y = f["x"], f["y"]
            if keys.get("down"): new_y += constants.SPEED
            if keys.get("up"): new_y -= constants.SPEED
            if keys.get("left"): new_x -= constants.SPEED
            if keys.get("right"): new_x += constants.SPEED
            dx, dy = new_x - field_center[0], new_y - field_center[1]
            if dx**2 + dy**2 <= (field_radius - constants.BALL_RADIUS) ** 2:
                f["x"], f["y"] = new_x, new_y
