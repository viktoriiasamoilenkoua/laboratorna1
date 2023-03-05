# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:51:03 2023

@author: vikas
"""

def fibonacci(n):
    """Повертає n-те число Фібоначчі."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Приклад використання
n = 10
for i in range(n):
    print(fibonacci(i))
