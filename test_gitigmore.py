from numpy import random
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict_number = random.randint(1, 101)
    while number != predict_number:
        count += 1
        if number > predict_number:
            predict_number += 2
        elif  number < predict_number:
            predict_number //= 2

    return count
    