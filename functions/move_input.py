def move_input():
    try:
        value = int(input('Номер для хода (1-9): '))
    except ValueError:
        print('Введите число от 1 до 9.')
        return False

    if value > 9 or value < 1:
        print('Введите число от 1 до 9 включительно')
        return False

    return value