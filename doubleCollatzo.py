def clz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return  num * 3 +1

while True:
    try:
        res = int(input("Введите целое положительное число: "))
        while res !=1:
            num = res
            if num > 0:
                res = clz(num)
                print(res)

            else:
                print("Число не целое положительное, повторите ввод: ")

    except ValueError:
        print("Пожалуйста повторите ввод! Вы ввели не цисло: ")