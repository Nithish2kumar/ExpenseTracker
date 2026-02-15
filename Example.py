from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivymd.font_definitions import theme_font_styles


KV = '''
MDScreen:
    md_bg_color: 240/255, 241/255, 243/255, 1

    MDRelativeLayout:
    
        MDCard:
            pos_hint: {"center_x": .22, "center_y": .95}
            size_hint: None, None
            size: dp(40), dp(40)
            radius: [50]
            theme_bg_color: "Custom"
            md_bg_color: 1, 1, 1, 1

            MDIconButton:
                icon: "chevron-left"
                icon_color: 76/255,76/255,76/255,1


        MDCard:
            style: "filled"
            pos_hint: {"center_x": .5, "center_y": .67}
            padding: dp(40)
            size_hint: None, None
            size: dp(500), dp(250)
            theme_bg_color: "Custom"
            md_bg_color: 1, 1, 1, 1
            padding: 8
            spacing: 8

            MDRelativeLayout:

                MDIconButton:
                    icon: "eye"
                    color: "grey"
                    pos_hint: {"right": 1, "top": 1}


                MDLabel:
                    text: "Account balance"
                    spacing: "8dp"
                    text_color: "grey"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    halign: "center"
                    bold: True
                    adaptive_height: True
                MDLabel:
                    text: "$34,567"
                    theme_text_color: "Primary"
                    pos_hint: {"center_x": .45, "center_y": .5}
                    halign: "center"
                    font_style: "Display"
                    role: "small"
                    bold: True
                    adaptive_height: True
                MDLabel:
                    text: ".90"
                    theme_text_color: "Secondary"
                    pos_hint: {"center_x": .63, "center_y": .5}
                    halign: "center"
                    color:"grey"
                    font_style: "Display"
                    role: "small"
                    bold: True
                    adaptive_height: True

                MDIconButton:
                    icon: "eye"
                    color: "grey"
                    pos_hint: {"right": 1, "top": 1}

                MDIconButton:
                    icon: "clipboard-multiple-outline"
                    color: "grey"
                    font_size: "5sp"
                    pos_hint: {"center_x": .3, "center_y": .4}                
                    
                MDLabel:
                    text: "1289440585"
                    theme_text_color: "Secondary"
                    pos_hint: {"center_x": .5, "center_y": .36}
                    halign: "center"
                    color:"grey"
                    bold: True
                    adaptive_height: True



'''



class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)


Example().run()