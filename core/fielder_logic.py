"""
Core logic for managing fielder placement and movement.

This module contains the `FielderLogic` class, which enforces rules for how
fielders are added, selected, and moved on the field, including constraints
on ring boundaries and player limits.
"""

from domain import config, constants
from core.interfaces import FielderLogicInterface

class FielderLogic(FielderLogicInterface):
    """
    Handles the logic related to fielder placement, selection, and movement.

    This class ensures the number of fielders and their placement respect 
    game rules (e.g., number of outer fielders).
    """

    def __init__(self):
        """
        Initializes the FielderLogic instance with an empty list of fielders.
        """
        self.fielders = []

    def handle_click(self, pos, field_center, field_radius, inner_ring_radius):
        """
        Handles mouse click events for either placing or selecting a fielder.

        Args:
            pos (tuple): (x, y) position of the mouse click.
            field_center (tuple): (x, y) coordinates of the field center.
            field_radius (int): Maximum allowed radius for placing players.
            inner_ring_radius (int): Radius defining the inner circle boundary.
        """
        x, y = pos
        dx, dy = x - field_center[0], y - field_center[1]
        dist_sq = dx ** 2 + dy ** 2

        if dist_sq > (field_radius - constants.BALL_RADIUS) ** 2:
            return

        if len(self.fielders) < config.NUM_PLAYERS - 2:
            is_outside = dist_sq > inner_ring_radius ** 2
            outer_count = sum(
                ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) > inner_ring_radius ** 2
                for f in self.fielders
            )
            if is_outside and outer_count >= config.NUM_OUTER_RING_PLAYERS:
                return

            self.fielders.append({"x": x, "y": y, "selected": False})
        else:
            for f in self.fielders:
                f["selected"] = False
            for f in self.fielders:
                dx = x - f["x"]
                dy = y - f["y"]
                if dx ** 2 + dy ** 2 <= constants.BALL_RADIUS ** 2:
                    f["selected"] = True
                    break

    def move_selected(self, keys, field_center, field_radius, inner_ring_radius):
        """
        Moves selected fielders based on keyboard arrow inputs.

        Movement is restricted by:
        - Field boundary (outer radius)
        - Maximum allowed outer fielders

        Args:
            keys (dict): Dictionary with key states: up, down, left, right.
            field_center (tuple): Center (x, y) of the field.
            field_radius (int): Outer boundary of the field.
            inner_ring_radius (int): Inner ring radius to constrain outer placement.
        """
        outer_count = sum(
            ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) > inner_ring_radius ** 2
            for f in self.fielders
        )

        for f in self.fielders:
            if f["selected"]:
                new_x, new_y = f["x"], f["y"]

                if keys.get("down"): new_y += constants.SPEED
                if keys.get("up"): new_y -= constants.SPEED
                if keys.get("left"): new_x -= constants.SPEED
                if keys.get("right"): new_x += constants.SPEED

                dx = new_x - field_center[0]
                dy = new_y - field_center[1]
                dist_sq = dx ** 2 + dy ** 2

                if dist_sq > (field_radius - constants.BALL_RADIUS) ** 2:
                    continue

                was_inside = ((f["x"] - field_center[0]) ** 2 + (f["y"] - field_center[1]) ** 2) <= inner_ring_radius ** 2
                moving_outside = dist_sq > inner_ring_radius ** 2

                if was_inside and moving_outside and outer_count >= config.NUM_OUTER_RING_PLAYERS:
                    continue

                f["x"], f["y"] = new_x, new_y

    def get_fielders(self):
        """
        Returns the list of all fielders with their current state.

        Returns:
            list: List of dictionaries with keys "x", "y", and "selected".
        """
        return self.fielders
