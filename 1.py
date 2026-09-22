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


#2
values_2 = [1, 3, 5, 8, 6, 4, 2]
for start in [0, 2, 4, 6]:
    idx, val = hill_climbing(values_2, start)
    print(f"Бастапқы күй: {start}, Соңғы индекс: {idx}, Соңғы мән: {val}")


#3
values_3 = [1, 4, 7, 5, 3, 6, 9, 8]
for start in [0, 4]:
    idx, val = hill_climbing(values_3, start)

#4
attempts = 5
for exp in range(1, 4):
    best_val = -1
    best_idx = -1
    
    for _ in range(attempts):
        start = random.randint(0, len(values_3) - 1)
        idx, val = hill_climbing(values_3, start)
        if val > best_val:
            best_val = val
            best_idx = idx
#5
