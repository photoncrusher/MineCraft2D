from abc import ABC, abstractmethod


class Screen:
    """Screen abstract class"""

    def __init__(self, main):
        self.main = main

    @abstractmethod
    def show(self):
        pass
