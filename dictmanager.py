class CountryMannager():
    def __init__(self, **items):
        self.items = items

    def add_item(self, **added_items):
        for key, value in added_items.items():
            self.items[key] = value

    def del_item(self, item_to_del):
        self.items.pop(item_to_del, 'Такого элемента нет') 

    def is_item_exits(self, item_to_check):
        try:
            return self.items[item_to_check]
        except:
            return 'Такой страны нет' 
        
    def update_item(self, **items_to_update):
        for key, value in items_to_update.items():
            self.items[key] = value


countries = CountryMannager(Russian = 'Moscow', Germany = 'Berlin', France='Paris')




print(countries.items)

def show_menu():
    print("\n--- Меню ---")
    print("0. список")
    print("1. Поиск")
    print("2. добавить")
    print("3. удалить")
    print("4. изменить")
    print("5. распокавать")
    print("6. упаковать")
    print("7. Выход")
    print("8. Получить код доступа")
    print("------------")

def main():
    while True:
        show_menu()
        choice = input("Выберите опцию (0-8): ")
        if choice == '0':
            print("список", countries.items)
            # Здесь код для Опции 1
        if choice == '1':
            el=input()
            print("поиск", countries.is_item_exits(el))
            # Здесь код для Опции 1
        elif choice == '2':
            el=input()
            print("добавить", countries.add_item(el))
            # Здесь код для Опции 2
        elif choice == '3':
            el=input()
            print("удалить", countries.del_item(el))
            break
        elif choice == '4':
            el=input()
            print("изменить", countries.update_item(el))
            # Здесь код для Опции 2
        elif choice == '5':
            print("бета-распоковать")
            break
        elif choice == '6':
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print("бета-упаковать")
            
        elif choice == '7':
            print("Выход из программы.")
            break
        elif choice == '8':
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print("зарикролено")
            # Здесь код для Опции 2
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 0 до 8.")

if __name__ == "__main__":
    main()