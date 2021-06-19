from abc import ABC, abstractmethod


class Screen:
    """Screen abstract class"""

    @abstractmethod
    def show(self):
        pass
