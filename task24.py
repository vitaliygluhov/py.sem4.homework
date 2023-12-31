
'''
Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''
import random
bushes_quantity = int(input('Количество кустов черники: '))
bushes_values = list()
for i in range(bushes_quantity):
    bushes_values.append(random.randint(0, 100))
print("Кусты с ягодой: ", *bushes_values)

arr_count = list()
for i in range(len(bushes_values)):
       arr_count.append(bushes_values[i-1] + bushes_values[i] + bushes_values[i-2]) # сумма трех кустов для каждого i куста
print("Максимальное значение которое возможно  \nсобрать с трех соседних кустов:\t", max(arr_count)) # выводим максимальное кол-во которое можно собрать за один заход
print(f"Номер куста (от 0 до {bushes_quantity-1}): \t", ((arr_count.index(max(arr_count)) - 1) + bushes_quantity) % bushes_quantity)