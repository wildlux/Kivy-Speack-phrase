import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from os import system 

kivy.require('1.0.9')
Builder.load_file("./style_page.kv")

class Speacking():
    def word(self,parola):
        os.system(say + parola)

class Speack(App ):
    def build(self):
        return Builder.load_file("./style_page.kv")


if __name__ == "__main__":
    Speack().run()
