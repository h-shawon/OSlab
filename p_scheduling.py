class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0

def priority_scheduling(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    remaining_processes = processes.copy()

    # Sort processes based on arrival time
    remaining_processes.sort(key=lambda x: x.arrival_time)

    while remaining_processes:
        # Select process with highest priority
        selected_process = min(remaining_processes, key=lambda x: x.priority)

        if current_time < selected_process.arrival_time:
            current_time = selected_process.arrival_time

        selected_process.start_time = current_time
        selected_process.completion_time = current_time + selected_process.burst_time

        total_waiting_time += (current_time - selected_process.arrival_time)
        total_turnaround_time += (selected_process.completion_time - selected_process.arrival_time)

        current_time = selected_process.completion_time
        remaining_processes.remove(selected_process)

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print("PID\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.start_time - process.arrival_time}\t\t{process.completion_time - process.arrival_time}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5, 2),
        Process(2, 1, 3, 1),
        Process(3, 2, 8, 3)
    ]
    priority_scheduling(processes)
