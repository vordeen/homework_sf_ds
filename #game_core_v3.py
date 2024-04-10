#game_core_v3
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
    tmp_number = number
    predict_number = random.randint(1, 101)
    while True:
        count += 1
        #if number == predict_number: break
        if predict_number > number:
            predict_number //= 2
        elif  predict_number < number:
            predict_number //= 2
        else:
              break

            
    # Ваш код заканчивается здесь

    return count
print(f'Run benchmarking for game_core_v3: {game_core_v3()}')

