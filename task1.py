#Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
n = int(input("Введите число членов последовательности: "))
data = list(fibonacci(n))
print(data)
