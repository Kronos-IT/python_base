#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'daughter', 'son']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['mother', 150],
    ['father', 190],
    ['daugher', 165],
    ['son', 160]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ' f'{my_family_height[1][1]}' ' см')

my_family_height_all = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]

print('Общий рост моей семьи ' + str(my_family_height_all) + ' см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
