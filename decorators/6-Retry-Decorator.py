# Retry a function if it fails.


import random

def retry(times):
    def decorator(func):

        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
            raise Exception(f"Failed after {times} attempts")
        return wrapper
    return decorator

@retry(3)
def flaky_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

print(flaky_function())


"""


Let’s walk through **what happens behind the scenes** — line by line and call by call — when you run this code.

---

### ✅ Step-by-step Execution Flow

#### 🔹 **Step 1: Decorator Definition**

```python
def retry(times):
    ...
```

This defines the **outer decorator factory**. It takes a number (`times`) and returns the actual `decorator`.

---

#### 🔹 **Step 2: Function Definition with Decorator**

```python
@retry(3)
def flaky_function():
```

This is equivalent to:

```python
flaky_function = retry(3)(flaky_function)
```

Now let’s see what each part of this does behind the scenes:

---

### ⚙️ Under the Hood:

#### 🔹 1. `retry(3)` is called.

```python
@retry(3)
```

➡️ This calls the **outer function `retry`** with `times = 3`.
It returns the **`decorator` function**.

```python
# now we have:
decorator = retry(3)
```

---

#### 🔹 2. `decorator(flaky_function)` is called.

The `decorator` takes your original function `flaky_function` as `func`.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        for attempt in range(times):  # uses 'times' from closure (3)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {e}")
        raise Exception(f"Failed after {times} attempts")
    return wrapper
```

✅ This returns the `wrapper` function and **replaces** the original `flaky_function`.

So now, behind the scenes:

```python
flaky_function = wrapper
```

But `wrapper` **remembers** the original function (`func`) via closure.

---

### ✅ Final Function Call

```python
print(flaky_function())
```

Now calling `flaky_function()` is actually calling `wrapper()`.

---

### 🔁 Inside the `wrapper`

```python
def wrapper(*args, **kwargs):
    for attempt in range(times):  # tries 3 times
        try:
            return func(*args, **kwargs)  # original flaky_function
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
    raise Exception(f"Failed after {times} attempts")
```

---

### 🎲 Random Outcome Example

```python
def flaky_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"
```

* `random.random()` returns a float between 0.0 and 1.0
* If it's less than 0.7 (70% chance), an exception is raised
* If not, it returns "Success!"

So on each retry:

* If it fails, it prints the error and retries
* If all 3 fail, it raises a final error

---

### 🧠 Closure Magic (Very Important)

* The `wrapper` function **remembers** both `func` (original function) and `times` (number of retries), **even after `retry` has finished executing**.
* This is because of **Python closures** — inner functions remember variables from their enclosing scope.

---

### 👇 Visualization:

```text
retry(3) → returns decorator

decorator(flaky_function) → returns wrapper

flaky_function = wrapper  ← replaces original function
           |
           +-- remembers original flaky_function
           +-- remembers times = 3

Calling flaky_function() → actually runs wrapper() → runs original function up to 3 times
```

---

### ✅ Output Examples

Run 1:

```
Attempt 1 failed: Random failure!
Attempt 2 failed: Random failure!
Success!
```

Run 2:

```
Attempt 1 failed: Random failure!
Attempt 2 failed: Random failure!
Attempt 3 failed: Random failure!
Traceback (most recent call last):
Exception: Failed after 3 attempts
```

---

Let me know if you'd like a **visual call stack diagram** or a version that shows how closures retain state!


Great! Let’s dive deep into what happens **behind the scenes** for this line:

```python
@retry(3)
def flaky_function():
    pass
```

---

### 🧠 Step-by-step “Behind the Scenes”:

This line:

```python
@retry(3)
def flaky_function():
    pass
```

is **syntactic sugar** for:

```python
def flaky_function():
    pass

flaky_function = retry(3)(flaky_function)
```

---

### ✅ What exactly happens:

Let’s break it into phases:

---

#### 🔹 Step 1: `retry(3)` is called

```python
def retry(times):         # times = 3
    def decorator(func):
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator
```

* `retry(3)` returns the `decorator` function.
* So now we have:

  ```python
  decorator = retry(3)
  ```

---

#### 🔹 Step 2: `decorator(flaky_function)` is called

Now:

```python
flaky_function = decorator(flaky_function)
```

This means:

* `decorator` takes `flaky_function` as input (`func`)
* Returns a new `wrapper` function
* So `flaky_function` is now actually pointing to `wrapper`

✅ The original `flaky_function()` is **wrapped**, and the original function is now "hidden" inside the wrapper via **closure**.

---

### 🧠 Final outcome (simplified):

```python
def flaky_function():
    pass

# Behind the scenes:
decorator = retry(3)
flaky_function = decorator(flaky_function)

# flaky_function is now the wrapper
```

---

### 📦 Internally Now:

```python
flaky_function = wrapper  # with closure variables:
# - func → original flaky_function
# - times → 3
```

When you later call `flaky_function()`, Python executes `wrapper()` and not your original function directly.

But the `wrapper()` has access to:

* the original `flaky_function` as `func`
* the `times` value (3 in this case)

---

### 🧠 Closure Summary

Closure is what enables the `wrapper` function to **remember**:

* `func` (the original function it’s wrapping)
* `times` (the argument passed to the decorator)

Even though `retry()` and `decorator()` have already returned!

---

### 👀 Visual Timeline:

```text
@retry(3)
↓
retry(3) → returns decorator

def flaky_function(): ...  ← declared

↓
decorator(flaky_function) → returns wrapper

↓
flaky_function = wrapper
```

---

### 🎉 Final Result:

You now have a function called `flaky_function`, but what’s really running is:

```python
def wrapper(*args, **kwargs):
    for attempt in range(3):
        try:
            return func(*args, **kwargs)
        except Exception:
            ...
```

And `func` is still the original `flaky_function` — kept alive via closure.

---

Let me know if you want me to visualize this as code flow or a call stack!


"""