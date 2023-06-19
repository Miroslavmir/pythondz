# 11.120, 11.132все. 11.145.абв. 11.173
# 11.120. В массиве хранится информация о росте 35 человек. Определить, сколько
# человек имеют самый большой рост.
# stroka = [178, 165, 180, 168, 175, 170, 173, 167,143, 67,78,65,170,170, 181,154,76,156,192,189,
#           135, 245,190,178,123, 162, 123, 176, 128, 189, 132, 145, 135, 126, 145]
# col = len(stroka)
# max = 0
# for i in range(col):
#     if stroka[i] > max:
#         max = stroka[i]
#         print(max)

# 11.132. Дан массив. Определить:
# а) максимальный элемент массива и элемент, являющийся максимальным
# без учета этого элемента;
# б) минимальный элемент массива и элемент, являющийся минимальным
# без учета этого элемента;
# в) номера максимального элемента массива и элемента, являющегося максимальным без учета этого элемента;
# spisok = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(spisok)):
#      if spisok[i] == max(spisok):
#          print(max(spisok))
# for i in range(len(spisok)):
#     if spisok[i] == min(spisok):
#         print(min(spisok))
# for i in range(len(spisok)):
#     if (spisok[i] == max(spisok)) and (spisok[i] != min(spisok)):
#         print(i)
#

#
#11.145. Дан массив из четного числа элементов. Поменять местами:
# а) его половины;
# б) первый элемент со вторым, третий — с четвертым и т. д.;
# в) его половины следующим способом: первый элемент поменять
# с последним, второй — с предпоследним и т. д.
# spisok = [1,2,3,4,5,6]
# m, m2, m3 = (spisok[::] for i in range(3))
# res = m3[len(spisok) // 2:] + m3[:len(spisok) // 2]
# for i in range(0,len(m2),2):
#     m2[i],m2[i + 1] = m2[i + 1],m2[i]
# length = len(m)
# for i in range(len(m) // 2):
#     temp = m[i]
#     m[i] = m[length - 1 - i]
#     m[length - 1 - i] = temp
# print(res)
# print(m2)
# print(m)
# 11.173. Переставить последний элемент массива на место первого.
# При этом первый, второй, ..., предпоследний элементы сдвинуть вправо на 1 позицию.
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(spisok)
def shift(spisok, steps):
    if steps < 0:
        for i in range(abs(steps)):
         spisok.append(spisok.pop(0))
shift(spisok, -8)
print(spisok)
# shift(spisok, 1)
# print(spisok)


