__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    x = 0
    y = 0
    z = 0

    for i in arr:
        if i % 2 == 0:
            x += i
        else:
            y += i
    if x != 0 and y != 0:
        z = x / y
    return z
