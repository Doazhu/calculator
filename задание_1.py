def main():
    # Бесконечный цикл, который можно прервать командой выхода
    while True:
        # Ввод данных пользователем
        first_number = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /, **): ")
        second_number = float(input("Введите второе число: "))

        # Словарь с операциями
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '**': lambda x, y: x ** y,
        }

        # Проверка на существование операции
        if operation in operations:
            result = operations[operation](first_number, second_number)
            print("Результат: ", result)
        else:
            print("Неизвестная операция")

        # Спрашиваем у пользователя, хочет ли он продолжить
        exit_program = input("Хотите ли вы продолжить? (да/нет): ")
        if exit_program.lower() != 'да':
            break

if __name__ == '__main__':
    main()
