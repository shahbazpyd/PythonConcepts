"""
Phase 1: The Fundamentals (Syntax & State)
This script aggregates all concepts from Phase 1 into a single executable reference.
"""
"""🧠 The Mental Model: Phase 1
Think of Python code as a script for a play.

Syntax (The Grammar):

Indentation: This is the stage direction. It tells the actors (the computer) which lines belong to which scene. If you don't indent correctly, the actors get confused about when to act.
Comments: These are notes for the director (you), ignored by the actors.
Variables (The Name Tags):

In some languages, variables are boxes. In Python, they are sticky notes.
score = 10 means you stick a note written "score" onto the number 10.
Dynamic Typing: You can peel the "score" note off 10 and stick it onto "Ten". The note doesn't care what it's attached to.
Data Types (The Props):

Integers/Floats: Numbers for math.
Strings: Text for dialogue.
Booleans: Light switches (only ON or OFF).
Operators (The Action Verbs):

These are the actions that happen on stage. + combines things, == compares them, and connects conditions."""
def main():
    # ==========================================
    # 1. BASIC SYNTAX
    # ==========================================
    # Indentation: Python uses whitespace to define blocks of code.
    # Comments: Lines starting with '#' are ignored.
    print("--- 1. Basic Syntax ---")
    
    # Docstrings: Triple quotes used for documentation.
    """This is a docstring inside a function scope."""

    # ==========================================
    # 2. VARIABLES & PRIMITIVE TYPES
    # ==========================================
    print("\n--- 2. Variables & Primitives ---")
    # Dynamic Typing: No need to declare type.
    # Naming Convention: snake_case for variables.
    
    my_integer = 10              # int
    my_float = 20.5              # float
    my_complex = 1 + 3j          # complex
    my_boolean = True            # bool
    my_none = None               # NoneType (absence of value)

    print(f"Integer: {my_integer}, Type: {type(my_integer)}")
    print(f"Float: {my_float}, Type: {type(my_float)}")
    print(f"Boolean: {my_boolean}, Type: {type(my_boolean)}")

    # ==========================================
    # 3. STRINGS & FORMATTING
    # ==========================================
    print("\n--- 3. Strings & Formatting ---")
    first_name = "Gemini"
    language = "Python"
    
    # f-strings (Preferred, Python 3.6+)
    print(f"Hello, I am {first_name} and I speak {language}.")
    
    # .format() method
    print("I am {} and I speak {}.".format(first_name, language))
    
    # % operator (Legacy)
    print("I am %s and I speak %s." % (first_name, language))

    # ==========================================
    # 4. TYPE CASTING
    # ==========================================
    print("\n--- 4. Type Casting ---")
    # Implicit: Python automatically converts smaller types to larger types (int -> float)
    result = my_integer + my_float 
    print(f"Implicit (int + float): {result} is {type(result)}")

    # Explicit: Manually converting types
    str_num = "100"
    converted_int = int(str_num)
    print(f"Explicit (str -> int): '{str_num}' becomes {converted_int}")

    # ==========================================
    # 5. OPERATORS
    # ==========================================
    print("\n--- 5. Operators ---")
    a, b = 10, 3

    # Arithmetic
    print(f"Division ({a}/{b}): {a/b}")       # 3.333...
    print(f"Floor Div ({a}//{b}): {a//b}")    # 3
    print(f"Modulus ({a}%{b}): {a%b}")        # 1
    print(f"Power ({a}**{b}): {a**b}")        # 1000

    # Comparison & Logical
    print(f"Is {a} > {b}? {a > b}")
    print(f"Logic: {True and False}")

    # Identity (is) vs Equality (==)
    list_1 = [1, 2, 3]
    list_2 = [1, 2, 3]
    print(f"Values equal? (==): {list_1 == list_2}") # True
    print(f"Same object? (is): {list_1 is list_2}")  # False (different memory locations)

if __name__ == "__main__":
    main()