import threading
import time
import random

class BoundedBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.in_index = 0
        self.out_index = 0
        self.mutex = threading.Semaphore(1)
        self.empty = threading.Semaphore(size)
        self.full = threading.Semaphore(0)

    def produce(self, item):
        self.empty.acquire()    # Wait for an empty slot
        self.mutex.acquire()    # Enter critical section

        # Add the item to the buffer
        self.buffer[self.in_index] = item
        self.in_index = (self.in_index + 1) % self.size
        print(f"Produced: {item}")

        self.mutex.release()    # Exit critical section
        self.full.release()     # Signal that buffer is no longer empty

    def consume(self):
        self.full.acquire()     # Wait for a full slot
        self.mutex.acquire()    # Enter critical section

        # Remove the item from the buffer
        item = self.buffer[self.out_index]
        self.out_index = (self.out_index + 1) % self.size
        print(f"Consumed: {item}")

        self.mutex.release()    # Exit critical section
        self.empty.release()    # Signal that buffer has an empty slot

        return item

def producer(buffer, id):
    while True:
        item = random.randint(1, 100)
        buffer.produce(item)
        time.sleep(random.random())

def consumer(buffer, id):
    while True:
        item = buffer.consume()
        time.sleep(random.random())

if __name__ == "__main__":
    buffer_size = 10
    buffer = BoundedBuffer(buffer_size)

    producer_threads = [threading.Thread(target=producer, args=(buffer, i)) for i in range(3)]
    consumer_threads = [threading.Thread(target=consumer, args=(buffer, i)) for i in range(3)]

    for t in producer_threads:
        t.start()

    for t in consumer_threads:
        t.start()

    for t in producer_threads:
        t.join()

    for t in consumer_threads:
        t.join()
