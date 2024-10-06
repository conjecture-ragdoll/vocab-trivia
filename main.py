# Importing required libraries
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HelloButtonsApp(App):
    def build(self):
        # Creating a vertical BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Creating 5 buttons
        for i in range(5):
            btn = Button(text='Button {}'.format(i+1))
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        print("Hello")  # You can replace this with any action you want

# Running the app
if __name__ == '__main__':
    HelloButtonsApp().run()

