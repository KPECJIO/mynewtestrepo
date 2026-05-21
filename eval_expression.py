from project_debugger import debugger

def eval_expression(a, b, action):
    debugger.log_step("Eval_expression", "Before Eval", {"a": a, "b": b, "action": action})
    
    if action == '+':
        res = a + b
    elif action == '-':
        res = a - b
    elif action == '*':
        res = a * b
    elif action == '/':
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль")
        res = a / b
    else:
        raise ValueError("Ошибка: неизвестное действие")
        
    # Проверяем длину дробной части. Она не должна превышать 10 знаков
    if '.' in str(res):
        fraction_length = len(str(res).split('.')[1])
        if fraction_length > 10:
            print("\n[ВНИМАНИЕ] Обнаружена аномалия точности. Активация отладчика pdb...")
            import pdb; pdb.set_trace() # Программа "замрет" на этой строке

    debugger.log_step("Eval_expression", "After Eval", {"result": res})
    return round(res, 10)