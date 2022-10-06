
from os import path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file('design.kv')
import json, glob
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from hoverable import HoverBehavior
from datetime import datetime
import random
from pathlib import Path


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'
    def login(self,uu,pp):
        with open("users.json") as file:
            users = json.load(file)
        if uu in users and users[uu]['password'] == pp:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = 'Wrong username or password'

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uu,pp):
        with open("users.json") as file:
            users = json.load(file)

        users[uu] = {'username':uu, 'password':pp,
        'created':datetime.now().strftime("%Y-%m-%d %H %M %S")}
        #print(users)

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = 'sign_up_screen_success'

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'
    pass

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

    def get_quote(self, feel):
        feel = feel.lower()
        availabel_feelings = glob.glob('quotes/*txt')
        #print(availabel_feelings)
        availabel_feelings = [Path(filename).stem for filename in 
        availabel_feelings]
        #print(availabel_feelings)
        if feel in availabel_feelings:
            with open(f'quotes/{feel}.txt') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()