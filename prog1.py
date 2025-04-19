from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem, TwoLineListItem,IconLeftWidget,TwoLineIconListItem 
from kivymd.uix.scrollview import ScrollView 
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.button import MDRaisedButton,MDFillRoundFlatButton,MDIconButton, MDFloatingActionButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd .uix.card import MDCard
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.boxlayout import MDBoxLayout 
from kivymd.uix.label import MDLabel
from kivymd .uix.progressbar import MDProgressBar
from kivy.clock import Clock
from kivymd.uix.chip import MDChip
from kivymd.uix.tab import MDTabs
from kivymd.uix.spinner import MDSpinner 
from kivymd.uix.scrollview import MDScrollView

class bottom(MDApp):
    def build(self):
        
        
        ca=MDCard(
        orientation="vertical",
        size_hint=(0.9,0.9),
        pos_hint={
        "center_x":0.5,
        "center_y":0.5
        },
        
        md_bg_color=(0.2,0.3,0.9,1)
        
        )
        jn=MDLabel(
        text="Uledi Stanslaus Bulegea",
        font_style="H4",
        theme_text_color="Custom",
        text_color=(1,0.2,0.8,1),
        underline=True
        )
        ca.add_widget(jn)
        
        
        self.lbp=MDLabel(
        text="Progress: 0%",
        font_style="H4",
        theme_text_color="Custom",
        text_color=(1,0.7,0.6,1),
        underline=True
        
        )
        ca.add_widget(self.lbp)
        
        self.pr=MDProgressBar(
        max=200,
        value=0,
        pos_hint={
        "center_x":0.5,
        "center_y":0.5
        
        },
        back_color=(0,0.3,0.4,1)
        )
        
        self.sp=MDSpinner(
        size_hint=(None,None),
        
        
        )
        ca.add_widget(self.sp)
        
        
        
        ca.add_widget(self.pr)
        fb=MDFloatingActionButton(
        icon="plus",
        md_bg_color=(0,0.3,0.4,1)
        )
       
        fb1=MDFloatingActionButton(
        icon="minus",
        md_bg_color=(0,0.3,0.4,1),
        )
        ca.add_widget(fb1)
        ca.add_widget(fb)
        fb.bind(
        on_release=self.start_prog
        )
        fb1.bind(
        on_release=self.reduce_prog
        )
        
        
        btn=MDFloatingActionButton(
        icon="eye",
        md_bg_color=(0,0.3,0.4,1),
        
        )
        
        ca.add_widget(btn)
        btn.bind(
        on_release=self.open_drop
        )
      
        
        
        
        
        
        
        
        
    
        
         
        
        return ca 
    
    def start_prog(self,ca):
        self.pr.value+=1
        self.lbp.text=f"Progress:{int(self.pr.value)}%"
           
    def reduce_prog(self,ca):
        self.pr.value-=1
        self.lbp.text=f"Progress:{int(self.pr.value)}%"   
        
        
    def open_drop(self,ca):
        menu_item=[
        {
        "text":"SAVE",
        },
        {
        "text":"EDIT",
        },
        {
        "text":"VIEW",
        },
        {
        "text":"NAME",
        },
        {
        "text":"UPDATE",
        },
        {
        "text":"DELETE"
        },
        {
        "text":"REDO"
        },
        {
        "text":"UNDO"
        }
        
        
        ]
        self.menu=MDDropdownMenu (
        items=menu_item,
        width_mult=4,
        pos_hint={
        "center_x":0.5,
        "center_y":0.5
        },
        md_bg_color=(0.4,0.3,0.8,1)
       
        )
        btn2=MDRaisedButton(
        text="QUIT",
        size_hint=(1,None),
        icon="delete"
        
        )
        self.menu.add_widget(btn2)
        self.menu.caller=ca
        self.menu.open()
    def select(self):
        self.menu.dismiss()
   
        
    

bottom().run()                 