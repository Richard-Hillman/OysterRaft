from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

class MidiPad(BoxLayout):

    def __init__(self, **kwargs):
        super(MidiPad, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.size_hint = (0.8, 0.8)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.colors = [
            (0.94, 0.92, 0.84, 1),
            (1, 1, 0, 1),
            (0.5, 0, 0.5, 1),
            (1, 0.75, 0.8, 1),
            (0, 0, 1, 1),
            (1, 0.65, 0, 1),
            (1, 0, 0, 1),
            (1, 1, 1, 1)
        ]

        for row in range(4):
            h_layout = BoxLayout(spacing=10)
            for col in range(8):
                btn = Button(text="", background_color=self.colors[0], size_hint=(1/8, 1))
                btn.background_normal = 'oysterDrawn.png'
                btn.color_index = 0
                btn.bind(on_press=self.change_color)
                h_layout.add_widget(btn)
                if col == 3:  # after the fourth column
                    with h_layout.canvas:
                        Color(0, 0, 0, 1)  # Set the color to black
                        Rectangle(pos=(btn.x + btn.width, btn.y), size=(10, btn.height))
            self.add_widget(h_layout)
            if row == 1:  # after the second row
                with self.canvas:
                    Color(0, 0, 0, 1)
                    Rectangle(pos=(self.x, h_layout.y + h_layout.height), size=(self.width, 10))

    def change_color(self, instance):
        instance.color_index = (instance.color_index + 1) % len(self.colors)
        instance.background_color = self.colors[instance.color_index]

class MidiPadApp(App):
    def build(self):
        Window.clearcolor = (0.5, 0.5, 0.5, 1)
        return MidiPad()

if __name__ == '__main__':
    MidiPadApp().run()
