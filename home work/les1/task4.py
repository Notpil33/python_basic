number = input("Введите случайное целое число:\n")
number = int(number)
number1= number%10
number2 = number//10
while number > 0:
    if number%10 > number1:
        number1 = number%10
    number = number//10
print(number1)