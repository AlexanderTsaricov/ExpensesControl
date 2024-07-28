import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.garden.graph import Graph, MeshLinePlot
from math import sin
from kivy.core.window import Window
from matplotlib.pyplot import subplots
import Expense as Ex
import json
import pickle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import DataExpenses
import Saved




exp = Saved.load()

print(exp.listData)
class MyRoot(Screen, BoxLayout):
    def minus(self):
        return AddRoot()
    def build(self):
        # Create box layout
        layout = BoxLayout()

        return layout

class AddRoot(Screen, BoxLayout):
    money = ""
    category = ""
    comment = ""
    def build(self):
        # Create box layout
        layout = BoxLayout()
        return layout

    def addMoney(self):
        self.money = self.ids.inputMoney.text
    def addCategory(self):
        self.category = self.ids.inputCategory.text
    def addComment(self):
        self.comment = self.ids.inputComment.text
    def printer(self):
        self.money = int(self.money)
        tempExp = Ex.Expense(self.money, self.category, self.comment)
        exp.addExpense(tempExp)
        for i in exp.listData:
            print(i.toPrint())
        exp.toDict()
        Saved.save(exp)
        exp.toExpense()

class textinp(Widget):
    pass
class ExpensesControl(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyRoot())
        sm.add_widget(AddRoot(name = "addRoot"))
        return sm


app = ExpensesControl()

app.run()