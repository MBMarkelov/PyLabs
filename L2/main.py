# main.py
from restaurant_package.dish import Dish
from restaurant_package.order import Order
from restaurant_package.table import Table
from restaurant_package.report import save_to_doc

def display_menu():
    print("\nДобро пожаловать в систему управления рестораном!")
    print("1. Добавить блюдо")
    print("2. Просмотреть заказ")
    print("3. Установить 11скидку")
    print("4. Занять столик")
    print("5. Показать столик")
    print("6. Сохранить отчет в .docx")
    print("0. Выход")

def main():
    order = Order()  # Создаем заказ
    table = Table(1, 4)  # Создаем столик с 4 местами

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            # Добавление блюда
            name = input("Введите название блюда: ")
            price = float(input("Введите цену блюда: "))
            dish = Dish(name, price)
            order.add_dish(dish)
            print(f"Добавлено: {dish}")

        elif choice == "2":
            # Просмотр заказа
            print(f"\nВаш заказ:\n{order}")

        elif choice == "3":
            # Установка скидки
            discount = float(input("Введите размер скидки (в процентах): "))
            order.discount = discount
            print(f"Скидка {discount}% установлена.")

        elif choice == "4":
            # Занять столик
            table.occupy()
            print("Столик занят.")

        elif choice == "5":
            # Показать статус столика
            print(table)

        elif choice == "6":
            # Сохранение отчета в формате .docx
            file_name = input("Введите имя файла для сохранения отчета (без расширения): ")
            save_to_doc(order, table, file_name + ".docx")
            print(f"Отчет сохранен как {file_name}.docx")

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
