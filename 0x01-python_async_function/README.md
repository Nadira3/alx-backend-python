# Async Project

## Overview
This project demonstrates the use of asynchronous programming in Python, utilizing `asyncio` to handle concurrent tasks efficiently. The project includes functions that leverage asynchronous comprehensions, allowing for cleaner and more readable code when dealing with asynchronous operations.

## Features
- **Asynchronous Functions**: Implements asynchronous functions to simulate delays and handle multiple tasks concurrently.
- **Asynchronous Comprehensions**: Utilizes `async for` to gather results from asynchronous iterators.
- **Performance Measurement**: Measures execution time for asynchronous tasks, allowing for performance optimization.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- `asyncio` module (included in Python standard library)

### Installation
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/async-project.git
cd async-project
```

### Usage

1. Run the main script: Execute the main script to see the asynchronous functions in action.
```
python 2-main.py
```

2. Modify parameters: You can change the parameters such as n and max_delay in 2-main.py to test different scenarios.



#### Example Functions
```
wait_random(max_delay=10):
```
A coroutine that waits for a random delay between 0 and max_delay seconds and returns the delay.

```
wait_n(n, max_delay):
```
A coroutine that spawns wait_random n times with the specified max_delay and returns a list of delays in ascending order.

```
measure_time(n, max_delay):
```

A function that measures the total execution time of wait_n(n, max_delay) and returns the average time per call.



##   Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request.

Acknowledgements

Asyncio Documentation

Python Official Documentation

