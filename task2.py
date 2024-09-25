from collections import deque

def is_palindrome(s: str) -> bool:
    # Приведення рядка до нижнього регістру та видалення пробілів
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Створення двосторонньої черги
    char_deque = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклад використання
input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Цей рядок є паліндромом.")
else:
    print("Цей рядок не є паліндромом.")