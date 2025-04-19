from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from sklearn.linear_model import LinearRegression
import numpy as np

class MainApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_field = MDTextField(hint_text="Enter a value")
        layout.add_widget(self.input_field)

        self.result_label = MDTextField(hint_text="Result", readonly=True)
        layout.add_widget(self.result_label)

        self.predict_button = MDFlatButton(text="Predict", on_release=self.predict)
        layout.add_widget(self.predict_button)

        return layout

    def predict(self, instance):
        # Sample data for training the model
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 3, 4, 5, 6])

        # Create and train the model
        model = LinearRegression()
        model.fit(X, y)

        # Get input value and make prediction
        input_value = float(self.input_field.text)
        prediction = model.predict(np.array([[input_value]]))
        
        # Update the result label with the prediction
        self.result_label.text = str(prediction[0])

if __name__ == '__main__':
    MainApp().run()
    