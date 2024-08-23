

numbers_arr = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
numbers_unique1 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
numbers_unique2 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
numbers_unique3 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]


for i in range(0, 1000):
    inNumStr = str(i)
    inNum = int(inNumStr)
    zero = 'ноль'


    if len(inNumStr) == 1:
        if inNum == 0:
            print(zero)
        else:
            for number in numbers_arr:
                if inNum -1 == numbers_arr.index(number):
                    print(number)
    elif len(inNumStr) == 2:
        if inNumStr[0] == '1':
            if inNum == 10:
                print(numbers_unique2[0])
            else:
                for number in numbers_unique1:
                    if inNum - 11 == numbers_unique1.index(number):
                        print(number)    
        else:
            double_number1 = ''
            double_number2 = ''
            for number in range(0, len(numbers_unique2) + 1):
                if int(inNumStr[0]) == number:
                    double_number1 = numbers_unique2[number-1]
                if int(inNumStr[1]) == number and int(inNumStr[1]) != 0:
                    double_number2 = numbers_arr[number-1]
            print(double_number1 + " " + double_number2)       
    elif len(inNumStr) == 3:
        triple_number1 = ''
        triple_number2 = ''
        triple_number3 = ''
        for number in range(0, len(numbers_unique3) + 1):
            if int(inNumStr[0]) == number:
                triple_number1 = numbers_unique3[number-1]
            if int(inNumStr[1]) + int(inNumStr[2]) != 0 and int(inNumStr[1]) == 1:
                if inNumStr[1:3] == '10':
                    triple_number2 = numbers_unique2[0]
                else:
                    if int(inNumStr[2]) == number:
                        triple_number2 = numbers_unique1[number - 1]    
            else:
                if int(inNumStr[1]) == number and int(inNumStr[1]) != 0:
                    triple_number2 = numbers_unique2[number-1]
                
                if int(inNumStr[2]) == number and int(inNumStr[2]) != 0:
                    triple_number3 = numbers_arr[number-1]       
        if int(inNumStr[1]) == 0:
            print(triple_number1 + ' ' + triple_number3)
        elif int(inNumStr[2]) == 0:
            print(triple_number1 + ' ' + triple_number2)
        else:
            print(triple_number1, triple_number2, triple_number3)


