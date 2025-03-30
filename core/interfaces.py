from abc import ABC, abstractmethod

class FielderLogicInterface(ABC):
    @abstractmethod
    def handle_click(self, pos, field_center, field_radius, inner_ring_radius): pass

    @abstractmethod
    def move_selected(self, keys, field_center, field_radius): pass

    @abstractmethod
    def get_fielders(self): pass


class RendererInterface(ABC):
    @abstractmethod
    def draw_fielders(self, screen, fielders): pass
