# 0x00. Python - Variable Annotations

This project is part of the **ALX Backend Python** curriculum and focuses on using **type annotations** in Python. Type annotations help make code more readable and easier to debug by clearly specifying the expected data types of variables and function return types.

## Learning Objectives

By completing this project, you will learn:

- The concept of type annotations in Python.
- How to use type hints to annotate variables and function arguments.
- The differences between static and dynamic typing.
- Common built-in types used in type annotations (e.g., `List`, `Tuple`, `Dict`, etc.).
- How to use type annotations with third-party libraries.

## Project Files

This project contains the following Python scripts that demonstrate the use of type annotations:

### 1. Basic Annotations
- **0-add.py**: Function that adds two floating point numbers.
- **1-concat.py**: Function that concatenates two strings.
- **2-floor.py**: Function that returns the floor of a floating-point number.
- **3-to_str.py**: Function that converts a floating-point number to a string.

### 2. More Complex Annotations
- **4-define_variables.py**: Defines variables with specified types.
- **5-sum_list.py**: Function that takes a list of floats and returns their sum.
- **6-sum_mixed_list.py**: Function that sums a list of integers and floats.
- **7-to_kv.py**: Function that converts a string and an integer/float to a tuple.
- **8-make_multiplier.py**: Function that returns a function that multiplies a float by a given number.
- **9-element_length.py**: Function that returns a list of tuples with elements and their lengths.

### 3. Advanced Concepts
- **100-safe_first_element.py**: Function that safely retrieves the first element from a list using type annotations and `Any`.
- **101-safely_get_value.py**: Function that safely retrieves a value from a dictionary using type hints and `TypeVar`.
- **102-type_checking.py**: Example of using type hints for third-party libraries and understanding `mypy`'s behavior.

## Requirements

- **Python 3.x** is required for these scripts.
- Use **mypy** to check type hints.
  
## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/alx-backend-python.git
   cd alx-backend-python/0x00-python_variable_annotations
   ```

2. Ensure that you have Python 3.x installed. You can check your Python version by running:
```
python3 --version
```

3. Optionally, you can install mypy to validate type annotations:
```
pip install mypy
```


Usage

Run any of the Python scripts using the command line:
```
python3 0-add.py
```
To check type annotations using mypy, run:
```
mypy 0-add.py
```
For example, to check the file 5-sum_list.py, you would run:
```
mypy 5-sum_list.py
```
Example

For 5-sum_list.py, the function sums a list of floating point numbers:
```
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```
To run the function, call it like this:
```
floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum)  # Output: 6.470000000000001
```
Resources

PEP 484 – Type Hints

Python Typing Documentation

Python Type Checking (Guide)

