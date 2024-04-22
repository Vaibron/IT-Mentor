def main(input: str):
    try:
        inp = input.split()       
        
        if len(inp) != 3:
            raise Exception("Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
        
        a = int(inp[0])
        b = int(inp[2])
        c = inp[1]
        
        if a < 1 or a > 10 or b < 1 or b > 10:
            raise Exception("Числа должны быть в диапазоне от 1 до 10.")
    
        if c == '+':
            result = a + b
        elif c == '-':
            result = a - b
        elif c == '*':
            result = a * b
        elif c == '/':
            result = a // b
        else:
            raise Exception("Недопустимая арифметическая операция. Используйте +, -, *, либо /.")
            
        return str(result)
    
    except Exception as e:
        print(e)
        return None

input_str = input()
result = main(input_str)
if result != None:
    print(result)


#тест