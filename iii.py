# Developer - не только разработчик

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, current_floor, new_floor):
        if new_floor == current_floor:
            print("Вы уже находитесь на этом этаже.")
        elif new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует.")
        else:
            print("Приняли! Включаю 'Michael Jackson - Billie Jean'")
            for i in range(current_floor + 1, new_floor + 1):
                print(f'{i}-ый этаж')

h1 = House('ЖК KFC', 28)

current_floor = int(input("Введите номер этажа, на котором вы сейчас находитесь: "))
new_floor = int(input("Введите номер этажа, на который вы хотите попасть: "))

h1.go_to(current_floor, new_floor)