from random import randint
num1 = randint(1,100)
print("Я загадаю число 1-100 спробуй вгадати")
num2 = -1
while num1 != num2:
    num2 = int(input("Вгадай число"))
    if num2 > num1:
        print("спробуй менше")
    if num2 < num1:
        print("спробуй більше")
print("Вітаю! ти вгадав, відповіть була " + str(num1))