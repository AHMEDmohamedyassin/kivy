import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image , AsyncImage
from kivy.core.window import Window

Window.clearcolor = (100/255 , 150/255 , 100/255 , 1/10)
Window.top = 100
Window.left = 100
Window.size = (500 , 600)

class Main (App):
    def build(self):
        self.title = "Ahmed App"
        B1 = Button(
            text="Home",
            size_hint = (0.33 , 0.1),
            pos_hint = {"x" : 0.5 , "y":0.1},
            color=(150/255 , 100/255 , 100/255),
            background_color=(100/255 , 100/255 , 150/250),
            font_size = (26),
            on_press = self.btn_press,
            on_release = self.btn_release
        )

        I1 = TextInput(
            text="default",
            multiline = False,
            size_hint=(0.2 , 0.1),
            pos_hint= {"x":.2 ,"y": .9},
        )

        L1 = Label(
            text="the label text",
            pos_hint={"x":0.1 , "y":0.9},
            size_hint=(0.3 , 0.1)
        )

        Img = Image(source="./assets/img.png" ,pos_hint={"x":0.1 , "y":0.9},size_hint=(0.3 , 0.1) )
        AsyncImg = AsyncImage(source="https://m.media-amazon.com/images/I/510F3M5LpoL._AC_UF894,1000_QL80_.jpg" ,pos_hint={"x":0.1 , "y":0.9},size_hint=(0.3 , 0.1))

        check = CheckBox()
        check.bind(active=self.check_active)

        return ScreenA()
    
    def btn_press (self , arg):
        arg.size_hint = (0.2 , 0.1)
        print('pressed')

    def btn_release (self , arg):
        arg.size_hint = (0.33 , 0.1)
        print('leaved')
    
    def check_active(self , arg , val):
        print('clicked' , val)

class ScreenA (GridLayout):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        # secondary grid and text input for secondary grid grid 
        labelGrid = GridLayout(
            pos_hint= (0 , 1),
            size_hint = (None , None),
            width = 400,
            height = 200
        )
        labelGrid.cols = 2
        self.I1 = TextInput(text="hello from ScreenA")
        self.I2 = TextInput(text="hello again from grid ScreenA")
        labelGrid.add_widget(self.I1)
        labelGrid.add_widget(self.I2)

        # button  for main grid
        self.B1 = Button(
            text="button" ,
            pos_hint={"x":0.0,"y":0.0},
            size_hint=(None , None),
            width=200, 
            height = 50 ,
            on_press = self.pressFunc
        )

        # label for main grid
        self.L1 = Label(
            color=(200/255 , 100/255 , 250/250),
            height=100,
            )

        self.add_widget(labelGrid)
        self.add_widget(self.L1)
        self.add_widget(self.B1)

    def pressFunc (self , args) : 
        if(self.L1.text != self.I1.text):
            self.L1.text = self.I1.text
        else: self.L1.text = self.I2.text

if __name__ == "__main__":
    Main().run()


# number 16 touchapp