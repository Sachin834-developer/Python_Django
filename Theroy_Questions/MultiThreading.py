"""
Multithreading is a programming concept that allows a single process to create multiple threads of execution. Each thread can run independently and concurrently, sharing the same resources of the process, such as memory. 

### Key Points:
- **Concurrency**: Multiple threads can be executed in overlapping time periods, improving the efficiency of CPU usage.
- **Resource Sharing**: Threads within the same process share memory and resources, which makes communication between them easier compared to separate processes.
- **Responsiveness**: Multithreading can enhance the responsiveness of applications, allowing background tasks to run without freezing the main application (e.g., in GUI applications).
- **Efficiency**: It helps utilize CPU resources better, especially on multi-core processors, by allowing threads to run in parallel.

### Common Use Cases:
- Performing background tasks (e.g., downloading files while the user interacts with the interface).
- Managing multiple connections (e.g., handling multiple clients in a server application).
- Executing tasks that are I/O-bound, like reading from or writing to files or databases.

Overall, multithreading can improve performance and responsiveness, but it also introduces complexity, such as the need for synchronization to avoid race conditions.    



WHAT is GIL in python ?

Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) is a mutex (mutual exclusion) that protects access to Python objects and prevents multiple native threads from executing Python bytecode at once. This lock is necessary because CPython (the most widely used implementation of Python) is not thread-safe. The GIL ensures that only one thread can execute Python code at a time, even if multiple threads are active in a process.

The GIL makes Python's multithreading suboptimal for CPU-bound tasks. Even if you create multiple threads to utilize multiple CPU cores, the GIL restricts execution to a single core at any time. This limits the performance benefits of multithreading for CPU-bound tasks (e.g., heavy computations) because the threads can't run in true parallelism due to the GIL.
"""

import threading
import time


# Function to print numbers
def print_even_numbers(name, delay):
    for i in range(0, 10, 2):
        time.sleep(delay)
        print(f"{name}: {i}")


def print_odd_numbers(name, delay):
    for i in range(1, 10, 2):
        time.sleep(delay)
        print(f"{name}: {i}")


# Create threads
thread1 = threading.Thread(target=print_even_numbers, args=("Thread 1", 0.5))
thread2 = threading.Thread(target=print_odd_numbers, args=("Thread 2", 0.5))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
