import locale
import os
import math
import itertools

def FindEntropy(SymNFreq):
    # Рассчитаем энтропию
    H = 0.0
    for key in SymNFreq:
        H = H + SymNFreq[key] * math.log(SymNFreq[key], 2)
    H = round(-H, 4)
    optH = math.log(len(SymNFreq), 2)
    # Найдём избыточность
    fi = round(1 - (H / optH), 4)
    return H, optH, fi


def ToString(d):
    for key in d:
        if d[key] != 0:
            print(f"{key}  :  {d[key]}")


def Independent():
    locale.setlocale(locale.LC_ALL, "Italian")
    # print("Введите имя файла: ", end=" ")
    # filename = input()
    filename = "fullalphabet.txt"
    inp = open(filename, "r+")
    FileSize = os.path.getsize(filename)
    print(f"Размер файла в байтах: {FileSize}")
    # Поскольку язык предоставляет возможность использования словарей:
    SymNFreq = {}
    for line in inp:
        for keys in line:
            SymNFreq[keys] = SymNFreq.get(keys, 0) + 1
    for keys in SymNFreq:
        SymNFreq[keys] /= FileSize
        SymNFreq[keys] = round(SymNFreq[keys], 4)
    ToString(SymNFreq)
    M = len(SymNFreq)
    # Рассчитаем энтропию
    H, optH, fi = FindEntropy(SymNFreq)
    print(f"Реальная энтропия при мощности алфавита {len(SymNFreq)}: {H}")
    print(f"Оптимальная энтропия при мощности алфавита {len(SymNFreq)}: {optH}")
    print(f"Избыточность: {fi}")


def Dependent():
    locale.setlocale(locale.LC_ALL, "Italian")
    print("Введите имя файла: ", end=" ")
    filename = input()
    # filename = "fullalphabet.txt"
    inp = open(filename, "r+")
    FileSize = os.path.getsize(filename)
    print(f"Размер файла в байтах: {FileSize}")
    # Поскольку язык предоставляет возможность использования словарей:
    array = []
    SymNFreq = {}
    for line in inp:
        for i in line:
            if i not in array:
                array.append(i)
    # В данном моменте будут как нельзя кстати сочетания с повторениями.
    Combinations = list(itertools.combinations_with_replacement(array, 2))
    inp.seek(0)
    for line in inp:
        for i in range(0, len(line) - 1):
            for index in range(0, len(Combinations)):
                if line[i] in Combinations[index] and line[i + 1] in Combinations[index]:
                    keys = line[i] + line[i + 1]
                    SymNFreq[keys] = SymNFreq.get(keys, 0) + 1
    for keys in SymNFreq:
        if keys[0] == keys[1]:
            SymNFreq[keys] /= 23  # Обработка ошибки
        SymNFreq[keys] /= FileSize
        SymNFreq[keys] = round(SymNFreq[keys], 4)
    # ToString(SymNFreq)
    H, optH, fi = FindEntropy(SymNFreq)
    H = H / 2
    print(f"Реальная энтропия при условии попарной зависимости: {H}")
    print(f"Избыточность: {fi}")


# MAIN
#Independent()
Dependent()
