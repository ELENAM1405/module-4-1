def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second


if __name__ == '__main__':
    print(divide(69, 3))
    print(divide(3, 0))
