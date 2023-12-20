from check import Check
from order import Order
from delivery import Delivery
from end_invoice import End_Invoice

# Определение класса 'Process' для управления списком различных объектов логистики
class Process:
    def __init__(self):
        # Инициализация пустого списка для хранения объектов логистики
        self.lst = []

    def __str__(self):
        return f"{self.lst}"

    # Метод для добавления объекта логистики в список
    def add(self, thing):
        self.lst.append(thing)

# Создание экземпляра класса Process для хранения объектов логистики
logistic_process = Process()

# Чтение данных из файла "order.txt" и создание объектов Order
with open("order.txt", "r", encoding="utf-8") as forder:
    # Итерация по каждой строке в файле
    for line in forder:
        # Извлечение данных из строки и преобразование их в соответствующие типы данных
        id, customer_name, address, issue_date, cargo, cargo_quantity, cargo_cost = line.split(';')
        id = int(id)
        cargo_quantity = int(cargo_quantity)

        # Создание объекта Order и добавление его в список logistic_process
        logistic_process.add(Order(id, customer_name, address, issue_date, cargo, cargo_quantity, cargo_cost))

# Чтение данных из файла "delivery.txt" и создание объектов Delivery
with open("delivery.txt", "r", encoding="utf-8") as fdelivery:
    # Итерация по каждой строке в файле
    for line in fdelivery:
        # Извлечение данных из строки и преобразование их в соответствующие типы данных
        id, id_order, delivery_date, courier_name, price, order_status = line.split(';')
        id = int(id)
        id_order = int(id_order)
        price = int(price)

        # Создание объекта Delivery и добавление его в список logistic_process
        logistic_process.add(Delivery(id, id_order, delivery_date, courier_name, price, order_status))

# Итерация по списку объектов логистики и вывод их строковых представлений
for thing in logistic_process.lst:
    print(str(thing), end='')
