def collatzu(num):
    if num % 2 ==0:
        return num // 2
    elif num % 2 ==1:
        return num * 3 + 1

while True:
    try:
        result = int(input("Please enter integer: "))
        while result !=1:
            num = result
            if result > 0:
                result = collatzu(num)
                print(result)
            else:
                print("Please enter a positive integer: ")
                break

    except ValueError:
        print("Please input integer. Dont simbols")