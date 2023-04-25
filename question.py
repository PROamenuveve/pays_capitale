import json


class Question():
    def __init__(self) :
        with open ("les_questions.json") as g:
            self.donner = json.load(g)
    def retour(self):
        return self.donner

Question()      