"""
decorator_deep_dive.py
This script explains decorators from the ground up and demonstrates how to build custom ones.
"""
import time
import functools

# ==========================================
# 1. THE CONCEPT: Functions wrapping Functions
# ==========================================
# A decorator is just a function that takes another function, 
# adds some functionality to it, and returns it.

def my_simple_decorator(func):
    """
    A simple decorator that prints before and after the function runs.
    """
    # The 'wrapper' is the actual function that will replace the original 'func'.
    # It usually accepts *args and **kwargs so it can handle any function signature.
    # @functools.wraps(func) is good practice: It copies the name/docstring of 'func' to 'wrapper'.
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        print(">>> LOG: Before the function runs")
        
        # This is where the actual function executes
        result = func(*args, **kwargs) 
        
        print("<<< LOG: After the function runs")
        return result
    
    return wrapper

# Applying the decorator using the @ syntax
@my_simple_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# ==========================================
# 2. PRACTICAL EXAMPLE: Timing Decorator
# ==========================================

def timer_decorator(func):
    """Calculates how long a function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs) # Run the function
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def slow_function():
    print("  (Doing some heavy work...)")
    time.sleep(1)
    print("  (Work complete.)")

# ==========================================
# 3. ADVANCED: Decorators with Arguments
# ==========================================
# If you want to pass arguments to the decorator itself (like @repeat(3)),
# you need THREE layers of functions.

def repeat(num_times):
    """
    A decorator factory. It returns the actual decorator.
    """
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"--- Repeating {num_times} times ---")
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hi, {name}!")

if __name__ == "__main__":
    # 1. Simple
    say_hello("Alice")
    print("-" * 20)
    
    # 2. Timer
    slow_function()
    print("-" * 20)
    
    # 3. Arguments
    greet("Bob")