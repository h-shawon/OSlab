class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0

def SJN(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    remaining_processes = processes.copy()

    while remaining_processes:
        # Sort the remaining processes by burst time
        remaining_processes.sort(key=lambda x: x.burst_time)

        # Find the process with the shortest burst time
        shortest_process = remaining_processes[0]

        if current_time < shortest_process.arrival_time:
            current_time = shortest_process.arrival_time

        shortest_process.start_time = current_time
        shortest_process.completion_time = current_time + shortest_process.burst_time

        total_waiting_time += (current_time - shortest_process.arrival_time)
        total_turnaround_time += (shortest_process.completion_time - shortest_process.arrival_time)

        current_time = shortest_process.completion_time
        remaining_processes.remove(shortest_process)

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print("PID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.start_time - process.arrival_time}\t\t{process.completion_time - process.arrival_time}\t\t{process.completion_time}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


processes = [
    Process(1, 0, 5),
    Process(2, 1, 8),
    Process(3, 2, 4)
    ]
SJN(processes)
