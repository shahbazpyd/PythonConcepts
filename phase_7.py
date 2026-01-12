"""
Phase 7: Functional Programming & Intermediate Concepts
This script demonstrates writing cleaner, more efficient code using functional paradigms.
"""

"""🧠 The Mental Model: Phase 7
Functional programming is about treating data like water flowing through pipes. You don't change the pipes; you just transform the water as it flows.

Iterables vs. Iterators (The Playlist vs. The "Next" Button):

Iterable: A music playlist. It contains a list of songs. You can look at the whole list.
Iterator: The internal pointer that tracks "Now Playing". It only knows what the next song is. You can't rewind an iterator; once you press next(), the previous moment is gone.
Generators (The Water Tap):

List: Buying a 24-pack of water bottles. It's heavy (uses lots of RAM) and takes up space, even if you only want one sip right now.
Generator: A water tap. It gives you water one cup at a time (yield) when you ask for it. It takes up almost no space (memory) because it doesn't store the water; it just knows how to produce it flow by flow.
Closures (The Backpack):

Imagine a function is a person leaving their house (scope). Usually, when they leave, the house disappears.
A Closure is like a backpack. Before the person leaves, they pack specific items (variables) from the house into the backpack. Even after the house is gone, they still have access to those specific items in their backpack wherever they go.
Decorators (The Picture Frame):

You have a photo (function). You want to make it look better without drawing on the photo itself.
You put it in a frame (decorator). The frame surrounds the photo. It can add things before the photo (glass) or after (backing), but the photo inside remains untouched.
Higher-Order Functions (The Assembly Line Robots):

map: A robot that spray-paints every car on the line red. (Transforms every item).
filter: A quality control robot that kicks defective cars off the line. (Selects items).
reduce: A trash compactor that crushes all the cars into one single cube. (Combines items into one result)."""
import functools

def main():
    # ==========================================
    # 1. ITERABLES & ITERATORS (The Playlist & The Next Button)
    # ==========================================
    print("--- 1. Iterables & Iterators ---")
    # Iterable: Something you can loop over (like a list).
    # Iterator: The object that actually fetches the items one by one.
    
    colors = ["red", "green", "blue"] # Iterable
    color_iterator = iter(colors)     # Create an iterator
    
    print(f"1st: {next(color_iterator)}") # red
    print(f"2nd: {next(color_iterator)}") # green
    print(f"3rd: {next(color_iterator)}") # blue
    # print(next(color_iterator)) # StopIteration Error if called again

    # ==========================================
    # 2. GENERATORS (The Water Tap)
    # ==========================================
    print("\n--- 2. Generators ---")
    # Unlike lists (which store all data in memory), generators produce items on the fly.
    # Mental Model: A vending machine (list) vs. a manufacturing machine (generator).
    
    def countdown_generator(n):
        print("  (Generator started)")
        while n > 0:
            yield n  # Pauses execution here and returns value
            n -= 1
            
    gen = countdown_generator(3)
    
    print("Calling next...")
    print(f"Got: {next(gen)}") # Runs until first yield
    print("Calling next again...")
    print(f"Got: {next(gen)}") # Resumes and runs until next yield
    
    # Generator Expression (Memory efficient list comprehension)
    # Uses parentheses () instead of brackets []
    squares_gen = (x*x for x in range(1000000)) 
    print(f"Generator object size is small: {squares_gen}")
    # We can take just one item without generating the other 999,999
    print(f"First square: {next(squares_gen)}")

    # ==========================================
    # 3. CLOSURES (The Backpack)
    # ==========================================
    print("\n--- 3. Closures ---")
    # A nested function that remembers variables from its enclosing scope.
    
    def multiplier_factory(factor):
        # 'factor' is local to multiplier_factory...
        def multiply(number):
            # ...but 'multiply' packs 'factor' into its backpack (closure)
            return number * factor
        return multiply
        
    times_two = multiplier_factory(2) # Creates a function that multiplies by 2
    times_three = multiplier_factory(3) # Creates a function that multiplies by 3
    
    print(f"5 * 2 = {times_two(5)}")
    print(f"5 * 3 = {times_three(5)}")

    # ==========================================
    # 4. DECORATORS (The Picture Frame)
    # ==========================================
    print("\n--- 4. Decorators ---")
    # A way to modify a function's behavior without changing its code.
    
    def my_logger(func):
        def wrapper():
            print("LOG: Before function execution")
            func()
            print("LOG: After function execution")
        return wrapper

    @my_logger
    def say_hello():
        print("  Hello World!")

    # Calling say_hello actually calls wrapper()
    say_hello()

    # ==========================================
    # 5. BUILT-IN HIGHER-ORDER FUNCTIONS (The Assembly Line)
    # ==========================================
    print("\n--- 5. Built-in Higher-Order Functions ---")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Map: Apply a function to every item
    # Mental Model: Spray painting every item.
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"Map (doubled): {doubled}")
    
    # Filter: Keep items that match a condition
    # Mental Model: Security guard checking IDs.
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Filter (evens): {evens}")
    
    # Reduce: Combine all items into one single value
    # Mental Model: A snowball rolling down a hill.
    # (1+2=3, 3+3=6, 6+4=10, 10+5=15)
    total = functools.reduce(lambda a, b: a + b, numbers)
    print(f"Reduce (sum): {total}")
    
    # Zip: Combine two lists into pairs
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 95]
    zipped = list(zip(names, scores))
    print(f"Zip: {zipped}")

if __name__ == "__main__":
    main()