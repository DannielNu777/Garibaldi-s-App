from kivy.app import App
from kivy.lang import Builder
from app.controllers.order_controller import OrderController

class RestaurantApp(App):
    def build(self):
        return Builder.load_file("app/views/main_view.kv")

if __name__ == "__main__":
    RestaurantApp().run()