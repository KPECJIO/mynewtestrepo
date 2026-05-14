import re

def input_expression():
    print("Калькулятор ")
    expression = input("Введите выражение: ")#Получение выражения 
    pattern = r'^(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)$'
    match = re.match(pattern, expression.strip()) # Деление выражения на переменные
    if not match:
        raise ValueError("Неверный формат")
    try:
        a = float(match.group(1)) # Первая переменная
        action = match.group(2) # Оператор
        b = float(match.group(3)) # Вторая переменная
    except ValueError:
        raise ValueError("Неверный формат")
    if action not in ['+', '-', '*', '/']:
        raise ValueError("Недопустимое действие. Используйте + - * /")
    return a, b, action # Передача 
