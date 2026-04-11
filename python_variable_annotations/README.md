# Python Variable Annotations

## 📌 Description

This project introduces **type annotations in Python 3**, allowing developers to specify variable types, function parameters, and return values. These annotations improve code readability, maintainability, and enable static type checking using tools like `mypy`.

---

## 🎯 Learning Objectives

At the end of this project, you should be able to explain:

- Type annotations in Python 3
- How to annotate variables and function signatures
- Duck typing in Python
- How to validate code using `mypy`

---

## 🧠 1. Basic Type Annotations

Type annotations allow you to specify the expected type of a variable.

```python
a: int = 1
pi: float = 3.14
name: str = "Alice"
is_valid: bool = True
```

---

## 🔧 2. Function Annotations

You can annotate function parameters and return types.

```python
def add(a: float, b: float) -> float:
    return a + b
```

```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

---

## 📦 3. Complex Types with typing

The `typing` module provides advanced types.

### ➤ List

```python
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

---

### ➤ Union (multiple possible types)

```python
from typing import Union

def square(v: Union[int, float]) -> float:
    return float(v ** 2)
```

---

### ➤ Tuple

```python
from typing import Tuple

def to_kv(k: str, v: float) -> Tuple[str, float]:
    return (k, v)
```

---

### ➤ Callable (functions as arguments or return values)

```python
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
```

---

### ➤ Iterable and Sequence

```python
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

---

## 🦆 4. Duck Typing

Python uses **duck typing**, meaning:

> "If it behaves like a duck, it's a duck."

You don’t check the type explicitly — only the behavior matters.

```python
def get_length(item):
    return len(item)
```

Works for:
- strings
- lists
- tuples

---

## ✅ 5. Static Type Checking with mypy

Install:

```bash
pip install mypy
```

Run:

```bash
mypy filename.py
```

Example:

```python
def add(a: int, b: int) -> int:
    return a + b

add("1", "2")  # mypy will detect an error
```

---

## ⚠️ Important Notes

- Type annotations are **not enforced at runtime**
- They are mainly used for:
  - readability
  - static analysis
  - better tooling support

---

## 🚀 Conclusion

Type annotations help write cleaner, safer, and more maintainable Python code. Combined with tools like `mypy`, they allow early detection of type-related bugs while keeping Python flexible.
