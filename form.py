from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
import sqlite3
from kivymd.uix.dialog import MDDialog

# Database setup
def create_table():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL,
                      password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Insert user data
def insert_user(username, password):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

class LoginScreen(Screen):
    def submit(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if username and password:
            # Insert data into the database
            insert_user(username, password)
            SS=MDDialog(
            text=f"successfully insertion \n{username}\n{password}"
            )
            SS.open()
        else:
            print("Please enter both fields")

class LoginApp(MDApp):
    def build(self):
        create_table()
        return Builder.load_string(KV)

KV = '''
ScreenManager:
    LoginScreen:

<LoginScreen>:
    name: "login_screen"

    MDTextField:
        id: username
        hint_text: "Username"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: 0.8

    MDTextField:
        id: password
        hint_text: "Password"
        password: True
        helper_text:"enter your password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: 0.8

    MDRaisedButton:
        text: "Login"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.submit()
'''

if __name__ == '__main__':
    LoginApp().run()
