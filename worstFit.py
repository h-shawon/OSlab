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

allocation = worst_fit(memory_blocks.copy(), process_sizes)
print(f"Worst Fit Allocation: {allocation}")
