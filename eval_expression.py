
def eval_expression(a, b, action):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль")
        return a / b
    else:
        raise ValueError("Ошибка: неизвестное действие")
    