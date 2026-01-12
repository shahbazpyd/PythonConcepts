"""
Phase 8: Advanced Python
This script covers internals, metaprogramming, concurrency, and optimization.
"""

"""🧠 The Mental Model: Phase 8
Phase 8 is about looking "under the hood" of the car and modifying the engine itself.

Memory Management (The Warehouse Manager):

Reference Counting: Think of every object (like a balloon) having a counter attached to it. Every time someone holds the string, the counter goes up. When they let go, it goes down. If the counter hits zero, the balloon flies away (is deleted).
Garbage Collection (GC): The janitor. Sometimes two people hold each other's balloons, but nobody else is watching them (circular reference). The reference count never hits zero, but they are useless. The GC finds these isolated groups and sweeps them away.
id(): The exact shelf number in the warehouse where the object lives.
Metaprogramming (The Factory Factory):

Classes are blueprints for creating Objects (Houses).
Metaclasses are blueprints for creating Classes (Architects).
type: The default architect.
__new__ vs __init__: __new__ is buying the raw materials (creating the empty object). __init__ is decorating the interior (setting values). You rarely need __new__ unless you are messing with immutable types or metaclasses.
Descriptors (The Gatekeepers):

Standard attributes are like open doors. You can walk in and throw furniture around.
Descriptors (__get__, __set__) are security guards stationed at specific doors. If you try to bring in a negative number, the guard stops you.
Concurrency & Parallelism (The Kitchen Staff):

Threading (I/O Bound): One chef (CPU) with multiple pots on the stove. While water boils (waiting for I/O, network), the chef chops onions. The GIL (Global Interpreter Lock) prevents the chef from chopping two things at exactly the same time, but they switch tasks so fast it looks simultaneous.
Multiprocessing (CPU Bound): Two chefs in two completely different kitchens. They can chop onions simultaneously. This bypasses the GIL but requires more overhead to coordinate.
Asyncio (The Waiter): One waiter handling 10 tables. They take an order, send it to the kitchen, and immediately go to the next table. They don't wait for the food to cook before talking to the next customer.
Slots (The Fixed Menu):

Normal objects use a dictionary (__dict__) to store attributes. It's flexible (you can order anything off-menu) but uses a lot of memory (RAM).
__slots__ is a fixed menu. You can only have exactly what is listed. It saves massive amounts of memory if you have millions of objects."""
import sys
import time
import threading
import multiprocessing
import asyncio
from typing import List, Dict, Optional

# ==========================================
# HELPER FUNCTIONS FOR CONCURRENCY
# ==========================================
def cpu_bound_task(n):
    """A task that requires heavy calculation (for Multiprocessing)."""
    count = 0
    for i in range(n):
        count += i
    return count

def io_bound_task(name, duration):
    """A task that waits (for Threading)."""
    print(f"  Thread {name}: starting sleep...")
    time.sleep(duration)
    print(f"  Thread {name}: woke up!")

async def async_task(name, duration):
    """An asynchronous task (for Asyncio)."""
    print(f"  Async {name}: starting...")
    await asyncio.sleep(duration) # Non-blocking sleep
    print(f"  Async {name}: finished!")


def main():
    # ==========================================
    # 1. MEMORY MANAGEMENT
    # ==========================================
    print("--- 1. Memory Management ---")
    
    # id(): The memory address
    x = [1, 2, 3]
    y = x
    print(f"ID of x: {id(x)}")
    print(f"ID of y: {id(y)} (Same as x)")
    
    # Reference Counting
    # Note: getrefcount returns 1 higher than expected because passing it to the function adds a ref.
    print(f"Ref count of x: {sys.getrefcount(x)}") 
    del y
    print(f"Ref count after deleting y: {sys.getrefcount(x)}")

    # ==========================================
    # 2. METAPROGRAMMING (Metaclasses)
    # ==========================================
    print("\n--- 2. Metaprogramming ---")
    
    # A metaclass that forces all class attribute names to be uppercase.
    class UpperCaseMeta(type):
        def __new__(cls, name, bases, attrs):
            uppercase_attrs = {}
            for key, value in attrs.items():
                if not key.startswith("__"):
                    uppercase_attrs[key.upper()] = value
                else:
                    uppercase_attrs[key] = value
            return super().__new__(cls, name, bases, uppercase_attrs)

    class MyClass(metaclass=UpperCaseMeta):
        hello = "world"

    # print(MyClass.hello) # This would fail!
    print(f"Modified attribute: MyClass.HELLO = {MyClass.HELLO}")

    # ==========================================
    # 3. DESCRIPTORS
    # ==========================================
    print("\n--- 3. Descriptors ---")
    
    class PositiveNumber:
        """A descriptor that enforces positive values."""
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, owner):
            return instance.__dict__.get(self.name)

        def __set__(self, instance, value):
            if value < 0:
                raise ValueError(f"{self.name} cannot be negative!")
            instance.__dict__[self.name] = value
            print(f"  Set {self.name} to {value}")

    class BankAccount:
        balance = PositiveNumber("balance")

        def __init__(self, init_balance):
            self.balance = init_balance

    acc = BankAccount(100)
    try:
        acc.balance = -50
    except ValueError as e:
        print(f"  Caught error: {e}")

    # ==========================================
    # 4. CONCURRENCY & PARALLELISM
    # ==========================================
    print("\n--- 4. Concurrency ---")

    # A. Threading (I/O Bound)
    print("A. Threading:")
    t1 = threading.Thread(target=io_bound_task, args=("A", 1))
    t2 = threading.Thread(target=io_bound_task, args=("B", 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # B. Multiprocessing (CPU Bound)
    # Note: In a real script, this often needs 'if __name__ == "__main__":' protection
    print("B. Multiprocessing:")
    p1 = multiprocessing.Process(target=cpu_bound_task, args=(1000000,))
    p1.start()
    p1.join()
    print("  Process finished.")

    # C. Asyncio (Asynchronous)
    print("C. Asyncio:")
    async def run_async():
        await asyncio.gather(
            async_task("X", 1),
            async_task("Y", 1)
        )
    asyncio.run(run_async())

    # ==========================================
    # 5. TYPE HINTING
    # ==========================================
    print("\n--- 5. Type Hinting ---")
    
    def process_data(items: List[int]) -> Dict[str, int]:
        total: int = sum(items)
        return {"total": total, "count": len(items)}

    result: Dict[str, int] = process_data([10, 20, 30])
    print(f"Typed result: {result}")

    # ==========================================
    # 6. SLOTS (Memory Optimization)
    # ==========================================
    print("\n--- 6. Slots ---")
    
    class RegularPoint:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class SlottedPoint:
        __slots__ = ['x', 'y'] # Fixed attributes, no __dict__
        def __init__(self, x, y):
            self.x = x
            self.y = y

    reg = RegularPoint(1, 2)
    slot = SlottedPoint(1, 2)
    print(f"Regular has __dict__: {hasattr(reg, '__dict__')}")
    print(f"Slotted has __dict__: {hasattr(slot, '__dict__')}")

if __name__ == "__main__":
    main()