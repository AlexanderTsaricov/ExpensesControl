import json
import pickle
import DataExpenses
import jsonpickle
def load():
    try:
        with open("expenses.json", "rb") as file:
            jsonTemp = file.read()
            print("Данные загружены из файла")
            print(jsonTemp)
            temp = jsonpickle.loads(jsonTemp)
            print(temp)
            temp.toExpense()
            return temp
    except Exception as inst:
        print("Данные не найдены, создаем новый список затрат")
        newData = DataExpenses.Data()
        return newData

def save(data):
    with open("expenses.json", "w") as file:
        print(data)
        jsonStr = jsonpickle.encode(data)
        print(jsonStr + "!!!!!!!!!!!!!!!!")
        file.write(jsonStr)