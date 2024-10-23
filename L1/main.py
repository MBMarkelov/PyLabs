import tasks  as T


menu = {
        0 : ("0. Расстояния между городами", T.one.solve),
        1 : ("1. Площадь круга и точка в нем", T.two.solve),
        2 : ("2. Работа с алгеброй", T.three.solve),
        3 : ("3. Получение киношек", T.four.solve),
        4 : ("4. Измерение роста семьи", T.five.solve),
        5 : ("5. Переселение зоопарка", T.six.solve),
        6 : ("6. Песенки", T.seven.solve),
        7 : ("7. Секрет", T.eight.solve),
        8 : ("8. Garden", T.nine.solve),
        9 : ("9. Шопинг", T.ten.solve),
        10 : ("10. Магазин", T.eleven.solve),
    }

def main():
    while True:

        for key in menu:
            description, func = menu[key]
            print(f'{description}')

        choice = int(input("\nВыберите задание для выполнения: "))
        if 0 <= choice < len(menu):
            description, func = menu[choice]
            func()
        elif choice == 11:
             break;
        else:
            print("Такого номера нет =(")


if __name__ == "__main__":
        main()