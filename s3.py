def is_palindrome(text):
    # Приводим к нижнему регистру и убираем пробелы
    text = text.lower().replace(" ", "")
    # Проверяем, совпадает ли строка с перевернутой
    return text == text[::-1]

# Тестируем несколько строк
test_strings = ["радар", "hello", "А роза упала на лапу Азора", "python"]
for s in test_strings:
    if is_palindrome(s):
        print(f"'{s}' - это палиндром")
    else:
        print(f"'{s}' - не палиндром")