from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('main.kv')

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