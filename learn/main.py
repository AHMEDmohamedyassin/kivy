import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("main.kv")


class Main (App):
    def build(self):
        Window.clearcolor = (100/255 , 150/255 , 100/255 , 1/10)
        Window.top = 100
        Window.left = 100
        Window.size = (500 , 600)
        self.title = "Ahmed App"    
        return ScreenC()

# grid layout
class ScreenA (Widget):
    l1 = ObjectProperty(None)
    i1 = ObjectProperty(None)
    i2 = ObjectProperty(None)

    def pressFunc (self ) : 
        if(self.l1.text != self.i1.text):
            self.l1.text = self.i1.text
        else: self.l1.text = self.i2.text

# box layout
class ScreenB (Widget):
    pass

class ScreenC(Widget):
    pass

if __name__ == "__main__":
    Main().run()


# number 9 boxlayout