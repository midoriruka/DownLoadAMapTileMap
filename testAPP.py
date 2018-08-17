# coding:utf-8
import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


Builder.load_string('''
<OneScreen>
    Label:
        text:u'请输入左上角经度:'
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        font_size: '18sp'
        size_hint: None, None
        pos:150,335
        size:'50dp', '40dp'
        color: .5, .7, .9, 1
    TextInput:
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        size_hint: None, None
        pos:280,340
        size:'300dp', '30dp'
    Label:
        text:u'请输入左上角纬度:'
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        font_size: '18sp'
        size_hint: None, None
        pos:150,275
        size:'50dp', '40dp'
        color: .5, .7, .9, 1
    TextInput:
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        size_hint: None, None
        pos:280,280
        size:'300dp', '30dp'
    Label:
        text:u'请输入右下角经度:'
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        font_size: '18sp'
        size_hint: None, None
        pos:150,215
        size:'50dp', '40dp'
        color: .5, .7, .9, 1
    TextInput:
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        size_hint: None, None
        pos:280,220
        size:'300dp', '30dp'
    Label:
        text:u'请输入右下角纬度:'
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        font_size: '18sp'
        size_hint: None, None
        pos:150,155
        size:'50dp', '40dp'
        color: .5, .7, .9, 1
    TextInput:
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        size_hint: None, None
        pos:280,160
        size:'300dp', '30dp'
    Label:
        text:u'请输入级别:'
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        font_size: '18sp'
        size_hint: None, None
        pos:150,95
        size:'50dp', '40dp'
        color: .5, .7, .9, 1
    TextInput:
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'   
        size_hint: None, None
        pos:280,100
        size:'300dp', '30dp'  
    Button:
        text:u'开始下载'
        font_name:r'C:\Windows\Fonts\STZHONGS.TTF'
        font_size: '18sp'
        size_hint: None, None
        pos:280,30
        size:'100dp', '50dp'
        color: .5, .7, .9, 1     
''')

class OneScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        Window.size = (650, 400)  # 窗口大小
        return OneScreen()

if __name__ == '__main__':
    TestApp().run()