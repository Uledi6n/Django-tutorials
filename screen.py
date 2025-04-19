from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.label import Label
from kivy.uix.screenmanager import SlideTransition 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 


class home(Screen):
     def __init__(self,**kwargs):
         super(home,self).__init__(**kwargs)
         
         bx=BoxLayout(
         orientation="vertical"
         )
         bx.add_widget(Label(
         text="welcome on home"
         ))
         bx.add_widget(Button(
         text="next",
         on_press=self.go_setting,
         size_hint=(0.3,0.1),
         width=100
         
         
         ))
         self.add_widget(bx)
         
     def go_setting(self, instance):
         self.manager.current="Settings"     



class settings(Screen):
     def __init__(self,**kwargs):
         super().__init__(**kwargs)
         
         bs=BoxLayout()
         bs.add_widget(Label(
         text="view now the settings "
         ))
         
         
         bs.add_widget(Button(
         text="next page",
         on_press=self.go_contact
         ))
         self.add_widget(bs)  
                  
     def go_contact(self, instance):
         self.manager.current="Contact" 
    
class contact(Screen):
     def __init__(self,**kwargs):
         super().__init__(**kwargs)
         self.l1=Label(
         text="Home page"
         
         )
         self.add_widget(self.l1)    

   
class demo(ScreenManager):
    def swithhome(self):
        self.transition=SlideTransition(
        direction="left",
        duration=0.5
        )
        self.current="Home page"
        
    def swithset(self):
        self.transition=SlideTransition(
        direction="left",
        duration=0.5
        )
        self.current="Settings" 
        
    def swithcont(self):
        self.transition=SlideTransition(
        direction="left",
        duration=0.5
        )
        self.current="Contact"    
         
           

class demo(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(home(
        name="Home page"
        ))
        sm.add_widget(settings(
        name="Settings"
        ))
        sm.add_widget(contact(
        name="Contact"
        
        ))
        sm.current="Home page"
        return sm
        
demo().run()        