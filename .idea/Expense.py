
import json
import pickle
class Expense ():
    money = 0
    category = "non kategory"
    comment = ""
    def __init__(self, money, category, comment):
        self.money = money
        self.category = category
        self.comment = comment
    def getMoney(self):
        return self.money
    def getCategory(self):
        return self.category
    def getComment(self):
        return self.comment
    def toJson(self):
        return self.encode(self)
    def toPrint(self):
        print("Покупка на сумму: " + str(self.money))
        print("Категория покупки: " + self.category)
        print("Комментарий: " + self.comment)
    def __setstate__(self):
        state = {}
        state["money"] = self.money
        state["category"] = self.category
        state["comment"] = self.comment
        return state
    def __getstate__(self, state: dict):
        self.money = state["money"]
        self.category = state["category"]
        self.comment = state["comment"]

