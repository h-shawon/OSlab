class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0

def FCFS(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.completion_time = current_time + process.burst_time

        total_waiting_time += (current_time - process.arrival_time)
        total_turnaround_time += (process.completion_time - process.arrival_time)

        current_time = process.completion_time

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print("PID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.start_time - process.arrival_time}\t\t{process.completion_time - process.arrival_time}\t\t{process.completion_time}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")



processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8)
    ]

FCFS(processes)
