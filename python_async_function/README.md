# Python Async Project – Concepts & Explanations

## 📌 Overview

This project introduces asynchronous programming in Python using:
- async / await
- asyncio
- coroutines
- tasks
- concurrency

The goal is to understand how to run multiple operations efficiently without blocking execution.

---

# 🧠 1. Synchronous vs Asynchronous

## 🔴 Synchronous execution

```python
import time

print("Start")
time.sleep(3)
print("End")
```

### ⏱️ Behavior

```
Time →
[==== 3s ====]

Total = 3 seconds (blocking)
```

👉 The program waits and does nothing during execution.

---

## 🟢 Asynchronous execution

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(3)
    print("End")

asyncio.run(main())
```

### ⏱️ Behavior

```
Time →
[==== waiting ====] → but program can do other things
```

👉 The program can switch to other tasks instead of blocking.

---

# ⚡ 2. async / await

## 🔹 async

Defines a coroutine:

```python
async def my_function():
    pass
```

👉 This function does NOT execute immediately.

---

## 🔹 await

Used to pause execution without blocking:

```python
await asyncio.sleep(2)
```

👉 Allows other tasks to run during the wait.

---

# 🔄 3. asyncio (Event Loop)

The asyncio module manages execution of async code.

It acts like a scheduler:

```
[ Event Loop ]
     ↓
 ┌───────────────┐
 │ Task A        │
 │ Task B        │
 │ Task C        │
 └───────────────┘
```

👉 It switches between tasks when they are waiting.

---

# 🎯 Task 0 – wait_random

## 📌 Goal

Create a coroutine that:
- waits for a random delay
- returns that delay

## ✅ Code

```python
import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
```

---

## 🧠 Logic

```
1. Generate random delay
2. Wait (non-blocking)
3. Return delay
```

---

## ⏱️ Visualization

```
wait_random(5)

→ random = 2.3
→ sleep 2.3s
→ return 2.3
```

---

# 🎯 Task 1 – wait_n

## 📌 Goal

Run multiple coroutines concurrently and return results in ascending order WITHOUT sorting.

---

## ✅ Code

```python
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
```

---

## 🧠 Key Concept: Concurrency = Natural Sorting

```
Tasks start at the same time
Shortest delay finishes first
```

---

## ⏱️ Visualization

```
Time →

A: [====== 4s ======]
B: [== 1s ==]
C: [==== 3s ====]
D: [= 0.5s =]

Order of completion:

D → 0.5
B → 1
C → 3
A → 4

Result:
[0.5, 1, 3, 4]
```

---

## ⚠️ Important

- asyncio.gather() → keeps order of calls ❌
- asyncio.as_completed() → order of completion ✅

---

# 🎯 Task 2 – measure_time

## 📌 Goal

Measure execution time of wait_n and return average time per task.

---

## ✅ Code

```python
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - start) / n
```

---

## 🧠 Logic

```
total_time ≈ max delay (NOT sum)

average_time = total_time / n
```

---

## ⏱️ Visualization

```
Delays = [2, 5, 1, 7, 3]

Time →
[======= 7s =======]

Result:
7 / 5 = 1.4
```

---

# 🎯 Task 3 – task_wait_random

## 📌 Goal

Return a Task instead of a coroutine.

---

## ✅ Code

```python
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
```

---

## 🧠 Concept: Coroutine vs Task

| Type | Description |
|------|------------|
| Coroutine | Not executed yet |
| Task | Scheduled & running |

---

## 🎬 Visualization

```
wait_random() → coroutine (idle)

create_task(wait_random())
→ Task created
→ Scheduled in event loop
→ Starts running
```

---

# 🎯 Task 4 – task_wait_n

## 📌 Goal

Same as wait_n but using Tasks instead of coroutines.

---

## ✅ Code

```python
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
```

---

## 🧠 Key Difference

```
wait_n → creates coroutines
task_wait_n → creates running tasks
```

---

## ⏱️ Visualization

```
Time →

T1: [------ 3s ------]
T2: [-- 1s --]
T3: [---- 2s ----]

Order of completion:

T2 → 1
T3 → 2
T1 → 3

Result:
[1, 2, 3]
```

---

# 🧠 Final Summary

```
async → defines async function
await → pauses without blocking
asyncio.run → starts event loop

coroutine → not running yet
task → running coroutine

gather → keeps order
as_completed → completion order

concurrency → tasks overlap
```

---

# 🚀 Key Takeaway

```
Async programming = doing useful work while waiting
```

---

# ✅ You now understand

- async / await
- asyncio event loop
- coroutines
- tasks
- concurrency
- execution timing
