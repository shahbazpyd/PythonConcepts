"""
Phase 4: Functions & Modularity
This script demonstrates how to create reusable code blocks, manage scope,
and organize code into modules.
"""
"""🧠 The Mental Model: Phase 4
Think of your code as a professional kitchen.

Functions (def, return) - A Specialized Appliance:

A function is like a blender. You don't want to manually mash ingredients every time. Instead, you package that logic into a reusable appliance. You put ingredients in (parameters), it does its job, and it gives you a result (returns a smoothie).
Parameters (Positional, Keyword, Default) - The Appliance's Settings:

Positional: The order matters. blend(fruit, liquid).
Keyword: You label the settings, so order doesn't matter. blend(liquid="milk", fruit="banana").
Default: The appliance has a factory setting. blend(fruit, liquid="water"). If you don't specify a liquid, it defaults to water.
*args, **kwargs - The "And More..." Bins:

*args: A "catch-all" bin for extra ingredients. "Blend a banana, and also these strawberries, blueberries, and raspberries." It collects them all into a tuple.
**kwargs: A "catch-all" for extra settings. "Blend with speed='high', pulse=True." It collects them into a dictionary.
Scope (Local, Global, Nonlocal) - Where Your Ingredients Are:

Local: Ingredients on your personal cutting board. They are used for one recipe and then discarded.
Global: Ingredients in the main pantry, available to anyone in the kitchen.
Nonlocal: Ingredients in a container on the counter, used by a series of related steps (like in a nested recipe).
Lambda Functions - A Disposable Gadget:

This is a single-use tool, like a plastic lemon squeezer. You use it for one quick task (e.g., sorting a list by a specific rule) and then toss it. You don't give it a formal name or store it.
Recursion - Russian Nesting Dolls:

To open the whole set, you open the outer doll, which reveals another doll. You apply the exact same process (open it) to the new, smaller doll, and so on, until you reach the smallest one (the "base case").
Modules & Packages - The Kitchen's Organization:

Module (.py file): A drawer for a specific type of tool (e.g., baking_tools.py).
Package (directory): The entire cabinet or section of the kitchen (e.g., a baking cabinet that contains drawers for tools, pans, etc.)."""
# ==========================================
# 8. MODULES & PACKAGES
# ==========================================
# A module is a Python file with code you can import. 'math' is a built-in module.
import math

# You can import a specific function and give it an alias.
from math import factorial as fact

# A package is a directory of modules. It must contain an __init__.py file.
# Example structure you would create on your file system:
# my_package/
# ├── __init__.py
# └── string_utils.py
#
# You would then use it like this:
# from my_package import string_utils


def main():
    # ==========================================
    # 1. & 2. DEFINING FUNCTIONS & PARAMETERS
    # ==========================================
    print("--- 1. & 2. Functions & Parameters ---")
    # Mental Model: A specialized appliance with settings.
    def make_greeting(name, greeting="Hello", punctuation="!"):
        """Creates a greeting string. Demonstrates all parameter types."""
        return f"{greeting}, {name}{punctuation}"

    # Calling with positional arguments
    print(f"Positional: {make_greeting('World')}")

    # Calling with keyword arguments (order doesn't matter)
    print(f"Keyword: {make_greeting(punctuation='!!', name='Python')}")

    # Calling with a mix (positional must come before keyword)
    print(f"Mixed: {make_greeting('Developer', greeting='Hi')}")

    # ==========================================
    # 3. VARIABLE LENGTH ARGUMENTS (*args, **kwargs)
    # ==========================================
    print("\n--- 3. Variable Length Arguments ---")
    # Mental Model: A "catch-all" bin for extra ingredients/settings.
    def kitchen_sink_blender(main_ingredient, *extra_ingredients, **settings):
        """Blends ingredients with various settings."""
        print(f"Main ingredient: {main_ingredient}")

        if extra_ingredients:
            # *args is a tuple of extra positional arguments
            print(f"Extra ingredients (*args): {extra_ingredients}")

        if settings:
            # **kwargs is a dictionary of extra keyword arguments
            print("Settings (**kwargs):")
            for key, value in settings.items():
                print(f"  - {key}: {value}")

    kitchen_sink_blender("Banana", "Strawberry", "Spinach", speed="High", pulse=True)

    # ==========================================
    # 4. SCOPE (Local, Global, Nonlocal)
    # ==========================================
    print("\n--- 4. Scope ---")
    pantry_item = "Sugar"  # Global scope

    def outer_function():
        counter_item = "Flour"  # Enclosing scope

        def inner_function():
            local_item = "Eggs"  # Local scope

            global pantry_item
            pantry_item = "Brown Sugar"  # Modify the global variable

            nonlocal counter_item
            counter_item = "Whole Wheat Flour"  # Modify the enclosing variable

            print(f"  Inner sees: {local_item}, {counter_item}, and {pantry_item}")

        print(f"Before inner call, outer sees: {counter_item}")
        inner_function()
        print(f"After inner call, outer sees: {counter_item} (modified by inner)")

    print(f"Before outer call, global pantry has: '{pantry_item}'")
    outer_function()
    print(f"After outer call, global pantry has: '{pantry_item}'")

    # ==========================================
    # 5. LAMBDA FUNCTIONS
    # ==========================================
    print("\n--- 5. Lambda Functions ---")
    # Mental Model: A disposable, single-use gadget.
    # lambda arguments: expression
    add_lambda = lambda x, y: x + y
    print(f"Lambda function: 5 + 3 = {add_lambda(5, 3)}")

    # Often used for short operations, like sorting
    points = [(1, 5), (9, 2), (4, 7)]
    # Sort by the second element (y-value) using a lambda as the key
    points.sort(key=lambda point: point[1])
    print(f"Sorted points by y-value: {points}")

    # ==========================================
    # 6. RECURSION
    # ==========================================
    print("\n--- 6. Recursion ---")
    # Mental Model: Russian nesting dolls.
    def countdown(n):
        if n <= 0:
            print("Blastoff!")  # Base case: The condition to stop.
            return
        print(n)
        countdown(n - 1)  # Recursive step: Call self with a smaller problem.

    countdown(3)

    # ==========================================
    # 7. USING AN IMPORTED FUNCTION (from top of file)
    # ==========================================
    print("\n--- 7. Using an Imported Function ---")
    num = 5
    print(f"Factorial of {num} (using 'math.factorial'): {math.factorial(num)}")
    print(f"Factorial of {num} (using alias 'fact'): {fact(num)}")


if __name__ == "__main__":
    main()