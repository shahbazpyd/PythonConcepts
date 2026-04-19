"""
property_rules_demo.py
This script demonstrates the strict rules of using @property, 
specifically focusing on naming, storage, and recursion avoidance.
"""

class StrictRules:
    def __init__(self, value):
        # We assign to 'self.data', which triggers the setter immediately.
        self.data = value

    # RULE 1: The Getter comes first and defines the property name.
    # The method name 'data' becomes the attribute name 'obj.data'.
    @property
    def data(self):
        print("  (Getter called)")
        # RULE 2: Return a "backing" variable (usually starts with _).
        # If you return 'self.data', you call the getter again -> Infinite Recursion.
        return self._data

    # RULE 3: The Setter uses @<property_name>.setter
    # The method name MUST be the same as the property ('data').
    @data.setter
    def data(self, value):
        print(f"  (Setter called with {value})")
        # RULE 4: Validation logic goes here.
        if value < 0:
            raise ValueError("Data cannot be negative!")
        
        # RULE 5: Assign to the "backing" variable.
        # If you assign 'self.data = value', you call the setter again -> Infinite Recursion.
        self._data = value

def main():
    print("--- Initializing Object ---")
    # This calls __init__, which calls the setter
    obj = StrictRules(10)
    
    print("\n--- Accessing Property ---")
    # This calls the getter
    print(f"Value is: {obj.data}")
    
    print("\n--- Setting Property ---")
    # This calls the setter
    obj.data = 20
    
    print("\n--- Triggering Validation ---")
    try:
        obj.data = -5
    except ValueError as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    main()