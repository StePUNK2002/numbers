import math
import numpy
from tkinter import *
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
def Action():
    number = int(a.get())
    spisoc = []
    while number <= int(b.get()):
        spisoc.append(number)
        number = number + 1
    TranspMatr(getStroks(spisoc, int(numberstolb.get())))




if __name__ == '__main__':
    root = Tk()
    root.geometry("300x180")
    numberstolb = Entry(root, width=30)
    text1 = Label(root, text="Введите кол-во столбцов")
    text2 = Label(root, text="Введите нижнию границу")
    text3 = Label(root, text="Введите верхнюю границу")
    a = Entry(root, width=30)
    b = Entry(root, width=30)
    button = Button(root, text="Заполнить файл", command=Action)
    text1.pack()
    numberstolb.pack()
    text2.pack()
    a.pack()
    text3.pack()
    b.pack()
    button.pack()
    root.resizable(width=False, height=False)
    root.mainloop()