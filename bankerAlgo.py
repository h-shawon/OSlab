from queue import PriorityQueue

def is_safe_state(available, allocation, max_need):
    n = len(allocation) 
    m = len(allocation[0]) 

    work = available.copy() 
    finish = [False] * n 
    safe_seq = [] 
    process_queue = PriorityQueue()
    for i in range(n):
        need = [max_need[i][j] - allocation[i][j] for j in range(m)]
        process_queue.put((sum(need), i))

    while not process_queue.empty():
        process_i = process_queue.get()[1] 
        if not finish[process_i] and all(work[j] >= allocation[process_i][j] for j in range(m)):
            for j in range(m):
                work[j] += allocation[process_i][j]
            finish[process_i] = True
            safe_seq.append(process_i)

    if not all(finish[i] for i in range(n)):
        return False

    return safe_seq


# Example usage
available = [3, 2, 1]
allocation = [
    [0, 1, 0],  # Process 0
    [2, 0, 0],  # Process 1
    [1, 1, 2],  # Process 2
]
max_need = [
    [7, 5, 3],  # Process 0
    [3, 2, 2],  # Process 1
    [8, 0, 6],  # Process 2
]

safe_seq = is_safe_state(available, allocation, max_need)
if safe_seq:
    print("System is in safe state. Safe sequence:", safe_seq)
else:
    print("System is not in a safe state.")