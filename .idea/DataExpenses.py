import json
import pickle

class Data ():
    list = []
    def __init__(self):
        try:
            with open("expenses.json", "rb") as file:
                jsonTemp = pickle.load(file)
                # Не загружается из файла
                temp = json.loads(jsonTemp, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
                self.list = temp.list
                print("Данные загружены из файла")
        except:
            print("Данные не найдены, создаем новый список затрат")

    def addExpense(self, x):
        self.list.append(x)
    def save(self):
        with open("expenses.json", "wb") as file:
            jsonString = json.dumps(self.__dict__)
            pickle.dump(jsonString, file)
def toDict(exp):
    return {"money":exp.money, "category":exp.category, "comment":exp.comment}
def toExpense(dicts):
    res = []
    for i in dicts:
        res.append(Expense(i["money"], i["category"], i["comment"]))
    return res
