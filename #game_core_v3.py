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
        if number == predict_number: break    
        if predict_number < 16: predict_number -=1
        if 15 < predict_number < 31: predict_number -= 15
        if 30 < predict_number < 46: predict_number -= 30
        if 45 < predict_number < 61: predict_number -= 45
        if 60 < predict_number < 76: predict_number -= 60
        if 75 < predict_number < 101: predict_number -= 75

            
    # Ваш код заканчивается здесь

    return count
print(f'Run benchmarking for game_core_v3: {game_core_v3()}')

