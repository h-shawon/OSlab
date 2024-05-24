def optimal_page_replacement(pages, capacity):
    # Initialize variables
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                # Determine the page to replace
                future_uses = [None] * len(memory)
                for j in range(len(memory)):
                    if memory[j] in pages[i+1:]:
                        future_uses[j] = pages[i+1:].index(memory[j])
                    else:
                        future_uses[j] = float('inf')
                
                page_to_replace = future_uses.index(max(future_uses))
                memory[page_to_replace] = pages[i]
            page_faults += 1

    return page_faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4

page_faults = optimal_page_replacement(pages, capacity)
print(f"Optimal Page Replacement: {page_faults} page faults")
