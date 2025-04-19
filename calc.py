import math
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

# Set window size (for testing)


KV = '''
MDBoxLayout:
    orientation: 'vertical'
    pos_hint:{"x_center":0.5,"y_center":0.5}
    spacing: 10

    # Result display (larger text area)
    MDTextField:
        id: result
        hint_text: "0"
        size_hint_y: None
        height: "80dp"
        font_size: "28sp"
        halign: "right"
        multiline: True
        readonly: True

    # Main grid layout with 5 rows and 4 columns
    GridLayout:
        cols: 4
        rows: 6
        size_hint_y: None
        height: self.minimum_height
        spacing: 5

        # Row 1: Basic numbers and operations
        MDRaisedButton:
            text: "7"
            on_release: app.on_button_click("7")
        MDRaisedButton:
            text: "8"
            on_release: app.on_button_click("8")
        MDRaisedButton:
            text: "9"
            on_release: app.on_button_click("9")
        MDRaisedButton:
            text: "/"
            on_release: app.on_button_click("/")

        # Row 2: More numbers and operations
        MDRaisedButton:
            text: "4"
            on_release: app.on_button_click("4")
        MDRaisedButton:
            text: "5"
            on_release: app.on_button_click("5")
        MDRaisedButton:
            text: "6"
            on_release: app.on_button_click("6")
        MDRaisedButton:
            text: "*"
            on_release: app.on_button_click("*")

        # Row 3: Basic numbers and operations
        MDRaisedButton:
            text: "1"
            on_release: app.on_button_click("1")
        MDRaisedButton:
            text: "2"
            on_release: app.on_button_click("2")
        MDRaisedButton:
            text: "3"
            on_release: app.on_button_click("3")
        MDRaisedButton:
            text: "-"
            on_release: app.on_button_click("-")

        # Row 4: Special functions
        MDRaisedButton:
            text: "0"
            on_release: app.on_button_click("0")
        MDRaisedButton:
            text: "."
            on_release: app.on_button_click(".")
        MDRaisedButton:
            text: "="
            on_release: app.calculate()
        MDRaisedButton:
            text: "+"
            on_release: app.on_button_click("+")

        # Row 5: Scientific and Memory functions
        MDRaisedButton:
            text: "sin"
            on_release: app.on_button_click("sin(")
        MDRaisedButton:
            text: "cos"
            on_release: app.on_button_click("cos(")
        MDRaisedButton:
            text: "tan"
            on_release: app.on_button_click("tan(")
        MDRaisedButton:
            text: "sqrt"
            on_release: app.on_button_click("sqrt(")

        # Row 6: Extra functions like Mode, AC, Memory
        MDRaisedButton:
            text: "AC"
            on_release: app.clear()
        MDRaisedButton:
            text: "M+"
            on_release: app.memory_add()
        MDRaisedButton:
            text: "MR"
            on_release: app.memory_recall()
        MDRaisedButton:
            text: "M-"
            on_release: app.memory_subtract()

        # Row 7: Shift, Backspace, Replay, Alfa
        MDRaisedButton:
            text: "Shift"
            on_release: app.shift_function()
        MDRaisedButton:
            text: "←"
            on_release: app.backspace()
        MDRaisedButton:
            text: "Replay"
            on_release: app.replay()
        MDRaisedButton:
            text: "Alfa"
            on_release: app.alfa_function()

'''

# Define the calculator application class
class CalculatorApp(MDApp):

    def build(self):
        self.memory = 0  # Store memory value
        self.last_result = ""  # Store last calculation result
        return Builder.load_string(KV)

    def on_button_click(self, text):
        current_text = self.root.ids.result.text
        # If the screen is showing 0, replace it
        if current_text == "0":
            self.root.ids.result.text = text
        else:
            self.root.ids.result.text += text

    def calculate(self):
        try:
            expression = self.root.ids.result.text
            result = str(eval(expression, {"__builtins__": None}, {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "exp": math.exp,
                "pi": math.pi,
                "**": math.pow
            }))
            self.last_result = result  # Store the result for Replay
            self.root.ids.result.text = result
        except Exception:
            self.root.ids.result.text = "Error"

    def clear(self):
        self.root.ids.result.text = "0"
        self.last_result = ""

    def backspace(self):
        current_text = self.root.ids.result.text
        if current_text != "0":
            self.root.ids.result.text = current_text[:-1]
            if not self.root.ids.result.text:
                self.root.ids.result.text = "0"

    def shift_function(self):
        # Placeholder for Shift functionality
        # Example: inverse trig functions or other shifted operations
        self.root.ids.result.text = "Shift activated"

    def memory_add(self):
        try:
            self.memory += float(self.root.ids.result.text)
        except ValueError:
            self.root.ids.result.text = "Error"

    def memory_recall(self):
        self.root.ids.result.text = str(self.memory)

    def memory_subtract(self):
        try:
            self.memory -= float(self.root.ids.result.text)
        except ValueError:
            self.root.ids.result.text = "Error"

    def replay(self):
        self.root.ids.result.text = self.last_result

    def alfa_function(self):
        # Placeholder for Alfa function
        self.root.ids.result.text = "Alfa activated"

# Run the app
if __name__ == "__main__":
    CalculatorApp().run()
    