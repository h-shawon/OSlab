class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0

def round_robin(processes, quantum):
    ready_queue = processes.copy()
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    while ready_queue:
        current_process = ready_queue.pop(0)
        current_process.start_time = max(current_time, current_process.arrival_time)
        
        if current_process.remaining_burst_time <= quantum:
            current_time += current_process.remaining_burst_time
            current_process.remaining_burst_time = 0
        else:
            current_time += quantum
            current_process.remaining_burst_time -= quantum
            ready_queue.append(current_process)

        if current_process.remaining_burst_time == 0:
            current_process.completion_time = current_time
            total_waiting_time += (current_process.completion_time - current_process.arrival_time - current_process.burst_time)
            total_turnaround_time += (current_process.completion_time - current_process.arrival_time)

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.completion_time - process.arrival_time - process.burst_time}\t\t{process.completion_time - process.arrival_time}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5)
    ]
    quantum = 3
    round_robin(processes, quantum)
