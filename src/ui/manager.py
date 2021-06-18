class Manager:
    def __init__(self, window_size):
        self.window_size = window_size
        self.elements = []

    def draw_ui(self, window):
        for e in self.elements:
            e.draw(window)

    def process_event(self, event):
        for e in self.elements:
            e.process_event(event)

    def add_element(self, element):
        self.elements.append(element)

