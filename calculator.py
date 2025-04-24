def main(input: str) -> str:
    parts = input.split()
    if len(parts) != 3:
        return "Введите 'число оператор число'"
    
    a, operator, b = parts
    
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Только целые числа"
    
    if not (1 <= a <= 10) or not (1 <= b <= 10):
        return "Числа от 1 до 10"
    
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b if b != 0 else "Делить на 0 нельзя"
    else:
        return "Неизвестный оператор"
    
    return f"Ответ: {result}"

if __name__ == "__main__":
    print(main(input("Ввод: ")))
