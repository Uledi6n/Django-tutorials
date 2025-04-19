from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFloatingActionButton, MDIconButton,MDRaisedButton 
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.slider import MDSlider 
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.bottomnavigation import MDBottomNavigation 
from kivymd.uix.boxlayout import BoxLayout 


class home(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        ca=MDCard(
        orientation="vertical",
        pos_hint={
        "center_x":0.5,"center_y":0.5
        },
        size_hint=(0.8,0.8),
        md_bg_color=(0.2,0.3,0.5,1)

        )
        ca.add_widget(
        MDLabel(
        text="Sign In",
        halign="center",
        
        font_style='H2', theme_text_color="Custom",
        text_color=(0.6,0,0.5,1)
        )
        
        )
        
        
        ca.add_widget(
        MDTextField(
        hint_text="enter your name",
        icon_right="account",
        required=True
        )
        )
        
        ca.add_widget(
        MDTextField(
        hint_text="enter your email",
        icon_right="email",
        required=True
        )
        )
        
        
        
        ca.add_widget(
        MDTextField(
        password=True,
        hint_text="enter your password",
        icon_right="lock",
        required=True,
        
        )
        )
        

        ca.add_widget(
        MDRaisedButton(
        icon="login",
        text="sign in",
        theme_text_color="Custom",
        text_color=(0,1,0,1),
        size_hint=(0.7,0.1),
        disabled=False,
        pos_hint={
        "center_x":0.5,
        "center_y":0.1
        },
        md_bg_color=(0.6,0,0.5,1)
        )
        )
        ca.add_widget(
        MDLabel() 
        )
        
        
    
        return ca
        
home().run()        