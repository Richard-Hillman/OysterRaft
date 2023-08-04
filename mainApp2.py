import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import kivy.resources

class MidiPad(GridLayout):
    def __init__(self, **kwargs):
        super(MidiPad, self).__init__(**kwargs)

        # Setting the rows and columns for the grid
        self.cols = 8
        self.rows = 4

        # Setting size to 80% of window size, and centering the grid
        self.size_hint = (0.8, 0.8)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Adding padding between buttons
        self.spacing = [10, 10]  # [spacing_x, spacing_y]

        # Define colors
        self.colors = [
            (0.94, 0.92, 0.84, 1),  # eggshell
            (1, 1, 0, 1),           # yellow
            (0.5, 0, 0.5, 1),       # purple
            (1, 0.75, 0.8, 1),      # pink
            (0, 0, 1, 1),           # blue
            (1, 0.65, 0, 1),        # orange
            (1, 0, 0, 1),           # red
            (1, 1, 1, 1)            # white
        ]

        # Adding buttons to the grid
        for _ in range(4 * 8):  # 4 rows * 8 columns
            btn = Button(text="", background_color=self.colors[0])
            
            # This line removes the darkening effect
            btn.background_normal = 'oysterDrawn.png'
            
            btn.color_index = 0  # Store the current color index
            btn.bind(on_press=self.change_color)
            self.add_widget(btn)

    def change_color(self, instance):
        instance.color_index = (instance.color_index + 1) % len(self.colors)
        instance.background_color = self.colors[instance.color_index]

class MidiPadApp(App):
    def build(self):
        return MidiPad()

if __name__ == '__main__':
    MidiPadApp().run()
