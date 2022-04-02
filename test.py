import math
import numpy
import re
#TODO сделать проверку того что если у меня все содержимое списка только списки длиной 1 то нужно просто печатать по порядку

def GetCol(size, n):
    return math.ceil(size / n)


def getStroks(list, n):
    answer = []
    v = []
    index = 0
    while len(answer) != n:
        try:
            v.append(list[index])
            index = index + 1
            if len(v) == GetCol(len(list), n):
                answer.append(v)
                v = []
        except:
            answer.append(v)
    return answer


def TranspMatr(list):
    v = []
    for i in range(len(list)-1):
        v.append(list[i])
    matr = numpy.array(v)
    matr = matr.transpose()
    print(list)
    stroka = ""
    for i in matr:
        stroka = stroka + str(i) + "\n"
    stroka = stroka.replace("[","")
    stroka = stroka.replace("[ ", "")
    stroka = stroka.replace("]", "")
    file = open("answer.txt", "w")
    file.write(stroka)
    file.close()
    mass = stroka.split("\n")
    mass = mass[:-1]
    for i in range(len(list[-1])):
        mass[i] = mass[i] + " " + str(list[-1][i])
    print(mass)
    stroka = ""
    for i in mass:
        stroka = stroka + i + "\n"
    stroka = stroka.replace("  ", " ")
    if len(list[0]) == len(list[-1]) and stroka[0] == " ":
        stroka = stroka[1:]
    file = open("answer.txt", "w")
    file.write(stroka)
    file.close()



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    number = a
    spisoc = []
    while number <= b:
        spisoc.append(number)
        number = number + 1
    TranspMatr(getStroks(spisoc, 4))
