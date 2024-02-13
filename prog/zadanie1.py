#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def set_operations(set1, set2):
    print("Множество 1:", set1)
    print("Множество 2:", set2)

    # Объединение
    union_set = set1.union(set2)
    print("\nОбъединение множеств 1 и 2:", union_set)

    # Пересечение
    intersection_set = set1.intersection(set2)
    print("Пересечение множеств 1 и 2:", intersection_set)

    # Разность
    difference_set = set1.difference(set2)
    print("Разность множеств 1 и 2:", difference_set)

    # Симметрическая разность
    symmetric_difference_set = set1.symmetric_difference(set2)
    print("Симметрическая разность множеств 1 и 2:", symmetric_difference_set)


# Считываем элементы множества строками
set1 = set(input("Введите элементы множества 1 (через запятую): ").split(","))
set2 = set(input("Введите элементы множества 2 (через запятую): ").split(","))

# Вызываем функцию для выполнения операций над множествами
set_operations(set1, set2)

if __name__ == "__main__":
    main()
