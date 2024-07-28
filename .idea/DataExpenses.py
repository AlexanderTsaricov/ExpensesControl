import json
import pickle
from Expense import Expense

class Data ():
    listData = []
    count = 0
    def __init__(self):
        pass
    def addExpense(self, x):
        self.listData.append(x)
        self.count += 1
    def toDict(self):
        tempList = []
        for x in self.listData:
            tempList.append(x.toDict())
        self.listData = tempList
    def toExpense(self):
        tempList = []
        for i in self.listData:
            tempList.append(Expense(i["money"], i["category"], i["comment"]))
        self.listData = tempList
