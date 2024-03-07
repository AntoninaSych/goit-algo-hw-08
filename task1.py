import heapq

def min_cost_to_connect_cables(cable_lengths):
    """
    Функція, що обчислює мінімальні витрати на об'єднання кабелів.

    Параметри:
    - cable_lengths: список, що містить довжини всіх кабелів.

    Повертає:
    - total_cost: мінімальні витрати на об'єднання кабелів.
    """
    heapq.heapify(cable_lengths)  # перетворення списку в купу
    total_cost = 0
    
    while len(cable_lengths) > 1:
        # отримання двох найменших кабелів
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        # обчислення витрат на їх з'єднання
        connection_cost = shortest1 + shortest2
        total_cost += connection_cost
        
        # додавання нового кабелю до купи
        heapq.heappush(cable_lengths, connection_cost)
    
    return total_cost

# Приклад використання:
cable_lengths = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
