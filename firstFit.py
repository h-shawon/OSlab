def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break

    return allocation

# Example usage
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

allocation = first_fit(memory_blocks.copy(), process_sizes)
print(f"First Fit Allocation: {allocation}")
