import random
import time
from threading import Thread
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        random_number = random.randint(3,10)
        time.sleep(random_number)


class Cafe:

    def __init__(self, *tables_in_cafe):
        self.q = queue.Queue()
        self.tables_in_cafe = tables_in_cafe

    def guest_arrival(self, *guests_in_cafe):
        for guest in guests_in_cafe:
            for table in self.tables_in_cafe:
                if table.guest is None:
                    table.guest = guest
                    print(f"{guest.name} занял стол номер {table.number}")
                    guest.start()
                    random_number = random.randint(1, 2)
                    time.sleep(random_number)
                    break
            else:
                self.q.put(guest)
                print(f"{guest.name} в очереди")
                random_number = random.randint(2, 3)
                time.sleep(random_number)

    def discuss_guests(self):
        while self.q.empty() is False or any(table.guest for table in self.tables_in_cafe):
            for table in self.tables_in_cafe:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} поел(-а) и ушёл(ушла). \nСтол {table.number} свободен')
                    table.guest = None
                    random_number = random.randint(2, 4)
                    time.sleep(random_number)
                if not self.q.empty() and table.guest is None:
                    table.guest = self.q.get()
                    table.guest.start()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    random_number = random.randint(1, 2)
                    time.sleep(random_number)


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
