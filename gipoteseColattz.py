def collatz(number):
    if number % 2 == 0:
        return number //2
    elif number % 2 == 1:
        return number * 3 +1
while True:
    try:
        number = int(input("Пожалуйста введите целое положительное цисло: "))
        if number > 0:
            result = collatz(number)
            while result !=1:
                number = result
                result = collatz(number)
                print(result)

        else:
            print("повторите ввод, число не положительное")
    except ValueError:
        print("Вы ввели не число !!! Повторите ввод !!!")