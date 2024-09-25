def is_balanced(expression: str) -> str:
    # Визначаємо пари відкритих і закритих дужок
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in expression:
        if char in '({[':  # Якщо це відкрита дужка
            stack.append(char)
        elif char in ')}]':  # Якщо це закрита дужка
            if not stack or stack.pop() != matching_brackets[char]:
                return "Несиметрично"

    if stack:
        return "Несиметрично"
    
    return "Симетрично"

# Приклади використання
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in expressions:
    print(f"{expr}: {is_balanced(expr)}")