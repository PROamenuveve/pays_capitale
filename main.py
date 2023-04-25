from kivy import Config
Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '570')
# Config.set('graphics', 'minimum_width', '650')
# Config.set('graphics', 'minimum_height', '300')




from kivymd.app import MDApp
import plyer
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty,Clock,NumericProperty,BooleanProperty,ObjectProperty
from question import Question
import random



class MenuPrincipale(MDFloatLayout):
    A = ObjectProperty()
    B = ObjectProperty()
    C = ObjectProperty()
    D = ObjectProperty()
    E = ObjectProperty()
    repons = ObjectProperty()
    teste = StringProperty()
    resue =  ObjectProperty() 
    score = NumericProperty()
    continu = BooleanProperty()
    verite = BooleanProperty()
    erreur = 0
    colore = ObjectProperty()
    olds = []
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.teste = "Bienvenue a vous sur \n le jeux pays capitale"
        self.resue = Question().retour()["question"]
        self.la_question()
        self.colore = [.5,.5,.5,.7]
        # self.ids.BB.md_bg_color = "blue"

    def la_question(self):
        self.resue = Question().retour()["question"]
        if len(self.olds) == len(self.resue):
            print("fini.......................................")
            self.continu = False
        else:
            
            self.continu = True
            self.old = random.randint(0,(len(self.resue)-1))
            # print(len(self.resue))
            while self.old  in self.olds:
                self.old = random.randint(0,(len(self.resue)-1))
            print(self.old)
            self.olds.append(self.old)
            self.repons = self.resue[self.old]["capitale"]
            print(self.repons)
            self.teste = self.resue[self.old]["pays"]+" ?"
            del self.resue[self.old]
            x = random.randint(0,3)

            y = random.randint(0,(len(self.resue)-1))
            self.A = self.resue[y]["capitale"]
            del self.resue[y]
            y = random.randint(0,(len(self.resue)-1))
            self.B = self.resue[y]["capitale"]
            del self.resue[y]
            y = random.randint(0,(len(self.resue)-1))
            self.C = self.resue[y]["capitale"]
            del self.resue[y]
            y = random.randint(0,(len(self.resue)-1))
            self.D = self.resue[y]["capitale"]
            del self.resue[y]

            
            # print(self.D)
            if x == 0:
                self.A = self.repons
            elif x == 1:
                self.B = self.repons
            elif x == 2:
                self.C = self.repons
            else:
                self.D = self.repons
 

    def la_repons(self,repondre):
        
        if  self.continu and repondre == self.repons:
            self.colore = [.5,.5,.5,.7]
            self.score += 1
            self.erreur = 0
            self.la_question()
            self.verite = True
            # self.ids.menus.md_bg_color = "blue"
        else:
            self.colore=[.9,.2,.2,.7]
            print("perdue")
            self.erreur += 1
            self.verite = False
            if self.erreur > 1:
                self.score = 0
        # self.score += 1
        # self.la_question()





class Pays_capitalesApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Blue' 
        self.theme_cls.accent_palette = "Yellow"
        self.theme_cls.accent_hue = '400' 
        self.theme_cls.primary_hue = 'A700' 



Pays_capitalesApp().run()