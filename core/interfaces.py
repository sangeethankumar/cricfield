"""
Defines abstract base interfaces for core components of the CricField application.

These interfaces enable clean separation of concerns and allow for flexible,
testable implementations of fielder logic and rendering.
"""

from abc import ABC, abstractmethod

class FielderLogicInterface(ABC):
    """
    Interface for implementing fielder interaction and movement logic.

    This abstract base class defines methods that any logic class must implement
    to handle player clicks, movement, and state retrieval.
    """

    @abstractmethod
    def handle_click(self, pos, field_center, field_radius, inner_ring_radius):
        """
        Handle a mouse click for selecting or placing a fielder.

        Args:
            pos (tuple): (x, y) position of the mouse click.
            field_center (tuple): (x, y) center of the field.
            field_radius (int): Maximum radius of the playable field.
            inner_ring_radius (int): Radius of the inner ring boundary.
        """
        pass

    @abstractmethod
    def move_selected(self, keys, field_center, field_radius, inner_ring_radius):
        """
        Move selected fielder(s) based on arrow key input.

        Args:
            keys (dict): Dictionary with arrow key states (e.g., {'up': True}).
            field_center (tuple): (x, y) center of the field.
            field_radius (int): Outer radius of the field.
            inner_ring_radius (int): Inner ring radius.
        """
        pass

    @abstractmethod
    def get_fielders(self):
        """
        Return the list of current fielders and their state.

        Returns:
            list: List of dictionaries with "x", "y", and "selected" keys.
        """
        pass


class RendererInterface(ABC):
    """
    Interface for rendering fielder visuals on the screen.

    Implementations are expected to draw fielders based on their position and state.
    """

    @abstractmethod
    def draw_fielders(self, screen, fielders):
        """
        Render fielders on the given screen surface.

        Args:
            screen (pygame.Surface): The surface on which to render.
            fielders (list): List of fielder dictionaries with position and selection.
        """
        pass
