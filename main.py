"""Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:

кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
Задача №1
Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
"""

# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
import random

class Pets():
    # константы состояния - активно что-то одно
    STATE_FEEDING = 'FEEDING'
    STATE_WALK = 'WALK'

    # состояние
    state = STATE_WALK
    # вид
    sort = None
    # вес, кг
    weight = None
    # имя
    name = None
    # цвет
    color = None
    # голос
    voice = None

    # обновить статус
    def update_status(self):
        # меняем рандомно статус
        i = random.randint(1, 5)
        if i % 2:
            self.state = 'FEEDING'
            print(f'{self.sort} {self.name} сейчас гуляет!')
        else:
            self.state = 'WALK'
            print(f'{self.sort} {self.name} сейчас ест!')

    # установить цвет
    def set_color(self, new_color):
        self.color = new_color

    # установить имя
    def set_name(self, new_name):
        self.name = new_name

    # установить вес
    def set_weight(self, new_weight):
        self.weight = new_weight

    # взаимодействие с домашним животным
    def utilization(self):
        pass

    # подать голос
    def get_voice(self):
        return self.voice

    # подать голос
    def get_status(self):
        return self.state

    # вернуть вес
    def get_weight(self):
        return self.weight

class Goose(Pets):
    """
    Класс Гусь
    """
    # общие признаки гусей
    voice = 'га-га-га-аа'
    sort = 'гусь'

    def __init__(self, pets_name, pets_color, pets_weight):
        #общие признаки животных
        self.name = pets_name
        self.color = pets_color
        self.weight = pets_weight
        self.state == 'FEEDING'

    # переопределяем взаимодействие
    def utilization(self):
        print(f'Гусь {self.name} снес 2 яйца!')

class Сhicken(Pets):
    """
    Класс Курица
    """
    # общие признаки куриц
    voice = 'ко-ко-ко-ко'
    sort = 'курица'

    def __init__(self, pets_name, pets_color, pets_weight):
        #общие признаки животных
        self.name = pets_name
        self.color = pets_color
        self.weight = pets_weight
        self.state == 'FEEDING'
    # переопределяем взаимодействие
    def utilization(self):
        print(f'Курица {self.name} снесла 1 яйцо!')

class Duck(Pets):
    """
    Класс Утка
    """
    # общие признаки уток
    voice = 'кря-кря-кря'
    sort = 'утка'

    def __init__(self, pets_name, pets_color, pets_weight):
        #общие признаки животных
        self.name = pets_name
        self.color = pets_color
        self.weight = pets_weight
        self.state == 'FEEDING'
    # переопределяем взаимодействие
    def utilization(self):
        print(f'Утка {self.name} снесла 1 яйцо!')

class Cow(Pets):
    """
    Класс Корова
    """
    # общие признаки коров
    voice = 'му-у-у-ууууу'
    sort = 'корова'

    def __init__(self, pets_name, pets_color, pets_weight):
        #общие признаки животных
        self.name = pets_name
        self.color = pets_color
        self.weight = pets_weight
        self.state == 'FEEDING'
    # переопределяем взаимодействие
    def utilization(self):
        print(f'Корова {self.name} надоила 10 литров молока!')

class Goat(Pets):
    """
    Класс козы
    """
    # общие признаки коз
    voice = 'ме-е-е-еее'
    sort = 'коза'

    def __init__(self, pets_name, pets_color, pets_weight):
        #общие признаки животных
        self.name = pets_name
        self.color = pets_color
        self.weight = pets_weight
        self.state == 'FEEDING'
    # переопределяем взаимодействие
    def utilization(self):
        print(f'Коза {self.name} надоила 1 литр молока!')


class Sheep(Pets):
    """
    Класс овец
    """
    # общие признаки овец
    voice = 'бе-ее-е-еее'
    sort = 'овца'

    def __init__(self, pets_name, pets_color, pets_weight):
        #общие признаки животных
        self.name = pets_name
        self.color = pets_color
        self.weight = pets_weight
        self.state == 'FEEDING'
    # переопределяем взаимодействие
    def utilization(self):
        print(f'Овца {self.name} принесла 1 кг шерсти!')

# print(Pets.__dict__)
# print(Goose.__dict__)
# print(Goose.__doc__)

# создаю ферму
farm={}

# создаю стадо гусей
goose_troop = [Goose('Серый' + str(x + 1), 'белый', random.randint(10, 15)) for x in range(2)]
farm.setdefault(Goose.sort,goose_troop)

goose_troop[0].set_name('Серый')
goose_troop[1].set_name('Белый')

# создаю поголовье кур
chicken_troop = [Сhicken('Ко-Ко' + str(x + 1), 'белый', random.randint(3, 5)) for x in range(2)]
farm.setdefault(Сhicken.sort,chicken_troop)

chicken_troop[0].set_name('Ко-Ко')
chicken_troop[1].set_name('Кукареку')

# создаю стадо коз
goat_troop = [Goat('Рога' + str(x + 1), 'белый', random.randint(35, 50)) for x in range(2)]
farm.setdefault(Goat.sort,goat_troop)

goat_troop[0].set_name('Рога')
goat_troop[1].set_name('Копыта')

# создаю стадо овец
sheep_troop = [Sheep('Серый' + str(x + 1), 'белый', random.randint(45, 60)) for x in range(2)]
farm.setdefault(Sheep.sort,sheep_troop)

sheep_troop[0].set_name('Барашек')
sheep_troop[1].set_name('Кудрявый')


# корова
cow=Cow('Манька','рыжий', random.randint(450, 700))
farm.setdefault(Cow.sort,cow)
# утка
duck=Duck('Кряква','коричневый', random.randint(3, 5))
farm.setdefault(Duck.sort,duck)

# выгуливаем стадо))
max_weight, total_weight = 0,0
amoung_pets=0

for sort, pets  in farm.items():
    #print(sort)
    if isinstance(pets,list):
        for pet in pets:
            #print(pet)
            print(f'Это {sort}. Его зовут {pet.name}. {pet.get_voice()}!')
            pet.update_status()
            pet.utilization()
            print('\n')

            # расчеты
            amoung_pets+=1
            weight=pet.get_weight()
            total_weight+=weight
            if weight > max_weight:
                max_weight = weight
                most_heavy_pet=pet

    else:
        #print(pets)
        print(f'Это {sort}. Его зовут {pets.name}. {pets.get_voice()}!')
        pets.update_status()
        pets.utilization()
        print('\n')

        # расчеты
        amoung_pets += 1
        weight = pets.get_weight()
        total_weight += weight
        if weight > max_weight:
            max_weight = weight
            most_heavy_pet = pets

# отчет:
# общий вес животных на ферме
print(f'Общий вес животных на ферме: {total_weight} кг')
print(f'Всего животных на ферме: {amoung_pets}!')
print(f'Средний вес животных на ферме: {total_weight/amoung_pets} кг')
print(f'Самое тяжелое животное на ферме - {most_heavy_pet.sort} {most_heavy_pet.name} - {most_heavy_pet.weight} кг!')

