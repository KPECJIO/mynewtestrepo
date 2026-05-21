import re
from project_debugger import debugger  # Импортируем наш отладчик

def input_expression():
    print("Калькулятор")
    expression = input("Введите выражение: ")
    
    # Отладка: фиксируем сырой ввод пользователя
    debugger.log_step("Input_handler", "Raw Input", {"expression": repr(expression)})
    
    pattern = r'^(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)$'
    match = re.match(pattern, expression.strip())
    
    if not match:
        raise ValueError("Неверный формат")
        
    try:
        a = float(match.group(1))
        action = match.group(2)
        b = float(match.group(3))
    except ValueError:
        raise ValueError("Неверный формат")
        
    if action not in ['+', '-', '*', '/']:
        raise ValueError("Недопустимое действие. Используйте + - * /")
        
    # Отладка: показываем успешно распарсенные токены
    debugger.log_step("Input_handler", "Parsed Tokens", {"a": a, "action": action, "b": b})
    
    return a, b, action