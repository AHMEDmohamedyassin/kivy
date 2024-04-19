from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_string(
    """
<Button>
    size_hint: .2,.2
    font_size:30
    background_color:(0.2 , 0.6 , 0.6)    

<ScreenA>
    BoxLayout:
        orientation: 'vertical'
        size: root.width,root.height

        TextInput:
            id: calc_input
            text:'0'
            size_hint:(1 , 0.3)
            background_color:(0.9 , 0.9 , 0.9 )
            font_size:50
            readonly:True

        GridLayout:
            cols:4

            GridLayout:
                cols:2
                size_hint:0.2 , 0.2
                Button:
                    text: 'C'
                    background_color:(0.2 , 0.4 , 0.6)
                    on_press:root.press(self.text)
                
                Button:
                    text: 'BS'
                    background_color:(0.2 , 0.4 , 0.6)
                    on_press:root.press(self.text)

            BoxLayout:
                orientation:"vertical"
                size_hint:0.2 , 0.2
                Button:
                    text: '0'
                    background_color:(0.2 , 0.4 , 0.6)
                    on_press:root.press(self.text)
                    size_hint: 1 , 1
                Button:
                    text: '.'
                    background_color:(0.2 , 0.4 , 0.6)
                    on_press:root.press(self.text)
                    size_hint: 1 , 1

            Button:
                text: '*'
                background_color:(0.2 , 0.4 , 0.6)
                on_press:root.press(self.text)

            Button:
                text: '/'
                background_color:(0.2 , 0.4 , 0.6)
                on_press:root.press(self.text)

            Button:
                text: '7'
                on_press:root.press(self.text)

            Button:
                text: '8'
                on_press:root.press(self.text)

            Button:
                text: '9'
                on_press:root.press(self.text)

            Button:
                text: '-'
                background_color:(0.2 , 0.4 , 0.6)
                on_press:root.press(self.text)

            Button:
                text: '4'
                on_press:root.press(self.text)

            Button:
                text: '5'
                on_press:root.press(self.text)

            Button:
                text: '6'
                on_press:root.press(self.text)

            Button:
                text: '+'
                background_color:(0.2 , 0.4 , 0.6)
                on_press:root.press(self.text)

            Button:
                text: '1'
                on_press:root.press(self.text)

            Button:
                text: '2'
                on_press:root.press(self.text)

            Button:
                text: '3'
                on_press:root.press(self.text)

            Button:
                text: '='
                background_color:(0.2 , 0.4 , 0.6)
                on_press:root.press(self.text)
        
    """
)

class ScreenA(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input = self.ids.calc_input.text

    def press (self , val):
        input = self.ids.calc_input.text
        if(val == "="):
            try:
                self.ids.calc_input.text = str(round(eval(input) , 1))
            except:
                self.ids.calc_input.text = "0"
        elif(val == "C"):
            self.ids.calc_input.text = "0"
        elif(val == "BS"):
            self.ids.calc_input.text = input[:-1]
            if(self.ids.calc_input.text == ''): self.ids.calc_input.text = "0"
        else:
            if(input == "0"): input = ""
            self.ids.calc_input.text = f"{input}{val}"
                
class Main(App):
    def build(self):
        return ScreenA()
    

if __name__ == "__main__":
    Main().run()