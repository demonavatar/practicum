def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result

# Первое тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из целых и дробных чисел.


mixed_numbers = [3, 7, 9, 10, 5.3]  # Список из int и float
result_numbers = '379105.3'  # Ожидаемый результат, который должна вернуть series_sum()

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() не работает со списком чисел')

# Второе тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из чисел и строк.

mixed_numbers_strings = [4, 10, 'chovel']  # Cписок из чисел и строк
result_numbers_strings = '410chovel'  # Ожидаемый результат, который должна вернуть series_sum()

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() не работает со смешанным списком')

# Третье тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать пустой список.
empty = []  # Пустой список
result_empty = ''  # Ожидаемый результат, который должна вернуть series_sum()

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(empty) == result_empty, (
    'Функция series_sum() не работает с пустым списком')
