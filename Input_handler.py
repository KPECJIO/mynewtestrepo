def input_expression(): 
    print("Калькулятор ")
    a = float(input('Введите первое значение: '))
    action = input('Введите действие (+, -, *, /): ')
    b = float(input('Введите второе значение: '))
    return a, b, action
