import random
import math

def hill_climbing(values, start):
    index = start
    
    while True:
        best_index = index

        if index > 0 and values[index - 1] > values[best_index]:
            best_index = index - 1
            
        if index < len(values) - 1 and values[index + 1] > values[best_index]:
            best_index = index + 1
        if best_index == index:
            break
            
        index = best_index
    return index, values[index]
