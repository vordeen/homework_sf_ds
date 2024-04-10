from numpy import random
from numpy import mean


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0      # счетчик попыток
    min_lim = 0    # нижняя граница 
    max_lim = 101  # верхняя граница
    # Запускаем бесконечный цикл поиска загаданного числа
    while True:
        
        # Вычисляем предполагаемое число и сравниваем с загаданным
        count += 1                                   # увеличиваем на 1 число попыток
        predict_number = (max_lim + min_lim) // 2  # предполагаемое число
        result = number - predict_number             # результат сравнения 
        
        # Выходим из цикла, если число угадано
        if result == 0: break
        # Изменяем границы интервала поиска, если число не угадано
        
        if result < 0:                                # если результат сравнения отрицательный
            max_lim = predict_number                # то правую границу смещаем в предполагаемое число
        else:                                         # если результат сравнения положительный
            min_lim = predict_number                # левую границу смещаем в предполагаемое число
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")



print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)