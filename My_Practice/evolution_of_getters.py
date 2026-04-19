"""
evolution_of_getters.py
This script demonstrates the three stages of attribute access:
1. Direct Access (No Control)
2. Java-Style Getters/Setters (Control, but verbose)
3. Pythonic @property (Control + Readability)
"""

# STAGE 1: Direct Access
# Pros: Simple, Readable.
# Cons: No control. User can set invalid values.
class SimpleBox:
    def __init__(self, width):
        self.width = width

# STAGE 2: Java-Style Getters/Setters
# Pros: Full Control (Validation).
# Cons: Verbose syntax (box.set_width(10)). Breaks code if you switch from Stage 1.
class JavaStyleBox:
    def __init__(self, width):
        self.set_width(width) # Use setter to validate init too

    def get_width(self):
        return self._width

    def set_width(self, value):
        if value <= 0:
            print("  [JavaStyle] Error: Width must be positive. Defaulting to 1.")
            self._width = 1
        else:
            self._width = value

# STAGE 3: Pythonic @property
# Pros: Full Control (Validation) AND Simple Syntax (box.width = 10).
# This is why we say it's "Readability" compared to Stage 2, but "Control" compared to Stage 1.
class PythonicBox:
    def __init__(self, width):
        self.width = width # Looks like direct access, but triggers setter!

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("  [Pythonic] Error: Width must be positive. Defaulting to 1.")
            self._width = 1
        else:
            self._width = value

def main():
    print("--- 1. Simple Box (No Protection) ---")
    b1 = SimpleBox(10)
    b1.width = -5 # Bad data allowed!
    print(f"SimpleBox width: {b1.width}")

    print("\n--- 2. Java Style (Protected but Verbose) ---")
    b2 = JavaStyleBox(10)
    b2.set_width(-5) # Validation works
    print(f"JavaStyleBox width: {b2.get_width()}")

    print("\n--- 3. Pythonic Style (Protected & Readable) ---")
    b3 = PythonicBox(10)
    b3.width = -5 # Validation works, using clean syntax
    print(f"PythonicBox width: {b3.width}")

if __name__ == "__main__":
    main()