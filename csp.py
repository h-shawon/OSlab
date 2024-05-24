import threading

class SharedResource:
    def __init__(self):
        self.mutex = threading.Semaphore(1)  # Semaphore to ensure mutual exclusion
        self.counter = 0

    def increment_counter(self):
        self.mutex.acquire()  # Wait operation (P operation)
        self.counter += 1
        print(f"Incremented counter: {self.counter}")
        self.mutex.release()  # Signal operation (V operation)

    def decrement_counter(self):
        self.mutex.acquire()  # Wait operation (P operation)
        self.counter -= 1
        print(f"Decremented counter: {self.counter}")
        self.mutex.release()  # Signal operation (V operation)

def worker(shared_resource):
    for _ in range(5):
        shared_resource.increment_counter()
        shared_resource.decrement_counter()

if __name__ == "__main__":
    shared_resource = SharedResource()
    
    # Create multiple threads to simulate concurrent access
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker, args=(shared_resource,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads have completed.")
