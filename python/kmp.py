# не работает для случаев, если префикс не с начала строки
# это типо ограничение использования?

# всегда ли префикс должен захватывать начало?
def list_p(my_str):
    list_p = [0 for i in range(len(my_str))]

    j = 0
    i = 1
    while j < len(my_str) and i < len(my_str):
        if my_str[j] == my_str[i]:
            list_p[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                list_p[i] = 0
                i += 1
            else:
                j = list_p[j - 1]

    return list_p


def main(main_str, sub_str):
    p = list_p(sub_str)

    len_sub_str = len(sub_str)
    len_main_str = len(main_str)
    j = 0
    i = 0
    while not(j == len_sub_str or i >= len_main_str):
        if main_str[i] == sub_str[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if j == len(sub_str):
        print("Подстрока найдена в строке!")
    else:
        print("Подстроки в строке нет!")


# как это работает?
if __name__ == '__main__':
    main("лиаллиил_лииллииб", "лииллиил")
    print(len("   "))