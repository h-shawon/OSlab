def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break

    return allocation


def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        best_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if best_idx == -1 or memory_blocks[j] < memory_blocks[best_idx]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            memory_blocks[best_idx] -= process_sizes[i]

    return allocation

def worst_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        worst_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if worst_idx == -1 or memory_blocks[j] > memory_blocks[worst_idx]:
                    worst_idx = j

        if worst_idx != -1:
            allocation[i] = worst_idx
            memory_blocks[worst_idx] -= process_sizes[i]

    return allocation



# Example usage
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

allocation1 = first_fit(memory_blocks.copy(), process_sizes)
print(f"First Fit Allocation: {allocation1}")

allocation2 = best_fit(memory_blocks.copy(), process_sizes)
print(f"Best Fit Allocation: {allocation2}")

allocation3 = worst_fit(memory_blocks.copy(), process_sizes)
print(f"Worst Fit Allocation: {allocation3}")