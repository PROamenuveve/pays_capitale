# from kivy.animation import Animation
# from kivy.lang import Builder
# from kivy.uix.behaviors import ButtonBehavior

# from kivymd.app import MDApp
# from kivymd.uix.behaviors import ScaleBehavior
# from kivymd.uix.boxlayout import MDBoxLayout

# KV = '''
# MDScreen:

#     ScaleBox:
#         size_hint: .5, .5
#         pos_hint: {"center_x": .5, "center_y": .5}
#         on_release: app.change_scale(self)
#         md_bg_color: "red"
# '''


# class ScaleBox(ButtonBehavior, ScaleBehavior, MDBoxLayout):
#     pass


# class Test(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def change_scale(self, instance_button: ScaleBox) -> None:
#         Animation(
#             scale_value_x=0.9,
#             scale_value_y=0.5,
#             scale_value_z=0.5,
#             d=0.3,
#         ).start(instance_button)


# Test().run()


from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.fitimage import FitImage

KV = '''
#:import os os
#:import images_path kivymd.images_path


MDCarousel:

    StencilImage:
        size_hint: .9, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        source: os.path.join(images_path, "logo", "kivymd-icon-512.png")
'''


class StencilImage(FitImage, StencilBehavior):
    pass


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
