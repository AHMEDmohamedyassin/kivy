from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import BooleanProperty


###########################
# interactive widget 
class InteractiveWidget(BoxLayout):
    button_enable = BooleanProperty(False)

    def click_action(self):
        self.ids.label.text = self.ids.textinput.text
    
    def toggle_action(self , btn):
        if(btn.state == 'down'):
            btn.text = "ON"
            self.button_enable = True
        else : 
            btn.text = "OFF"
            self.button_enable = False

###########################
###########################
###########################
#PageLayout
# class PageLayoutExample(PageLayout):
#     pass

###########################
#ScrollView
# class ScrollViewLayoutExample(ScrollView):
    # pass

###########################
#stackLayout
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1 , 101):
            b = Button(text = str(i) , size_hint=(None , None) , size=(dp(100) , dp(100)))
            self.add_widget(b)

###########################
#GridLayout
class GridLayoutExample(GridLayout):
    pass

###########################
#AnchorLayout
class AnchorLayoutExample(AnchorLayout):
    pass

###########################
#BoxLayout
class BoxLayoutExample(BoxLayout):
    pass

###########################
#Widget
class MainWidgetExample(Widget):
    pass 

class Main(App):
    def build(self):
        return super().build() 
    

if __name__ == "__main__" : 
    Main().run()