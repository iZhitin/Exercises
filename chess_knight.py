# Задача: написать скрипт, который будет выдавать количество доступных ходов у коня в зависимости от
# его положения на шахматной доске. Считать, что данный конь - единственная на фигура на доске

import string

letter = input("Введите координату по Х (от a до h): ")
letter_position = string.ascii_lowercase.index(letter)
x = letter_position + 1

y = int(input("Введите координату по Y (от 1 до 8): "))

count = 0

if (x + 2 >= 3) and (y + 1 >= 2) and (x + 2 <= 8) and (y + 1 <= 8):
    count += 1
if (x + 1 >= 2) and (y + 2 >= 3) and (x + 1 <= 8) and (y + 2 <= 8):
    count += 1
if (x - 1 >= 1) and (y - 2 >= 1):
    count += 1
if (x - 2 >= 1) and (y - 1 >= 1):
    count += 1
if (x + 1 >= 2) and (y - 2 >= 1) and (x + 1 <= 8):
    count += 1
if (x + 2 >= 3) and (y - 1 >= 1) and (x + 2 <= 8):
    count += 1
if (x - 1 >= 1) and (y + 2 >= 3) and (y + 2 <= 8):
    count += 1
if (x - 2 >= 1) and (y + 1 >= 2) and (y + 1 <= 8):
    count += 1
    
knight_position = letter + str(y)

print(f"Количество доступных ходов из положения {knight_position} сотавляет: {count}")
