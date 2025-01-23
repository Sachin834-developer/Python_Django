"""
Multiprocessing is a programming paradigm that allows the execution of multiple processes simultaneously. Each process has its own memory space and resources, which makes it more isolated than threads. This isolation helps avoid issues like race conditions but requires more overhead for inter-process communication.

### Key Features of Multiprocessing:
- **Independent Processes**: Each process runs in its own memory space, allowing for true parallelism.
- **Resource Allocation**: Since processes don’t share memory, they require more resources than threads but avoid many synchronization issues.
- **Use of Multiple CPUs**: It is well-suited for CPU-bound tasks, where tasks can be distributed across multiple CPU cores.

### Example of Multiprocessing in Python:

Here’s a simple example using the `multiprocessing` module to calculate the square of numbers in parallel:

"""

import multiprocessing
import time


# Function to calculate square of a number
def calculate_square(n):
    time.sleep(1)  # Simulating a time-consuming operation
    print(f"Square of {n}: {n * n}")


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Creating a list of processes
    processes = []
    for number in numbers:
        process = multiprocessing.Process(target=calculate_square, args=(number,))
        processes.append(process)
        process.start()  # Start the process

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
"""

### Explanation:
- **Importing Modules**: The `multiprocessing` and `time` modules are imported.
- **Defining a Function**: The `calculate_square` function calculates the square of a number and simulates a delay.
- **Creating Processes**: A list of processes is created, each targeting the `calculate_square` function with a different number.
- **Starting Processes**: Each process is started using `start()`.
- **Joining Processes**: The main program waits for all processes to finish using `join()`.

### Advantages of Multiprocessing:
- It can fully utilize multiple CPU cores, leading to better performance for CPU-intensive tasks.
- Avoids issues related to memory sharing, making it safer for certain types of applications.

Multiprocessing is particularly useful for tasks that require a lot of CPU power and can be executed independently.
"""
