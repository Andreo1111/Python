

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number +1
while True:
    try:
        number = int(input("Please input integer: "))
        if number > 0:
            res = collatz(number)
            while res != 1:
                number = res
                res = collatz(number)
                print(res)
        else:
            print("Please input positive integer: ")

    except ValueError:
        print("Please repeat your input. Dont integer!!!!")



