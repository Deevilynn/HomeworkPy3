#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# a = int(input('Введите количество элементов списка: '))
# a_entered = input("Введите через пробел элементы списка: ").split()
# list_a = list(map(int, a_entered))
# if len(list_a) != a:
#     print('Количество указанных элементов не соответствует количеству введенных. Повторите еще раз.')
# else:
#     b = int(input('Введите число, встречаемость которого необходимо найти в списке: '))
#     count = 0
#     for i in range(a):
#         if list_a[i] == b:
#             count += 1
#     print('Число ',b,' встречается в списке ',count,'раз') 


#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# a = int(input('Введите количество элементов списка: '))
# a_entered = input("Введите через пробел элементы списка: ").split()
# list_a = list(map(int, a_entered))
# if len(list_a) != a:
#     print('Количество указанных элементов не соответствует количеству введенных. Повторите еще раз.')
# else:
#     b = int(input('Введите число, с которым необходимо сравнивать элементы списка: '))
#     min = abs(b - list_a[0])
#     for i in range(a):
#         new_min = abs(b - list_a[i])
#         if new_min < min:
#             min = new_min
#             index = i
# print('Искомый индекс числа: ', index,)
# print('Число равно: ',list_a[index])


#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

sob = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JZШЭЮ',
      	10:'QZФЩЪ'}

word = input('Введите слово: ').upper()
a=0
for i in word:
    for y in sob.keys():
        if i in sob[y]:
            a +=y
print('Сумма очков: ',a)





