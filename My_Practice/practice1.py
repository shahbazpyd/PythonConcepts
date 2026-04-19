# text = "Hello World"
# if (n := len(text)) > 5:
#     print(f"String is long! It has {n} charactors.")


# text = "Hello World"
# if (len(text)) > 5:
#     print(f"String is long! It has {n} charactors.")


# digit = int(input("enter number 1 to 3:"))
# match digit:
#     case 1:
#         print("One")
#     case 2:
#         print("Tow")
#     case 3:
#         print("Three")
#     case _:
#         print("please write number between 1 to 3")


# def kitchen_sink_blender(main_ingredient, *extra_ingredients, **settings):
#         """Blends ingredients with various settings."""
#         print(f"Main ingredient: {main_ingredient}")

#         if extra_ingredients:
#             # *args is a tuple of extra positional arguments
#             print(f"Extra ingredients (*args): {extra_ingredients}")

#         if settings:
#             # **kwargs is a dictionary of extra keyword arguments
#             print("Settings (**kwargs):")
#             for key, value in settings.items():
#                 print(f"  - {key}: {value}")

# kitchen_sink_blender("Banana", "Strawberry", "Spinach", "Apples", speed="High", pulse=True)




# print("\n--- 4. Scope ---")
# pantry_item = "Sugar"  # Global scope

# def outer_function():
#     counter_item = "Flour"  # Enclosing scope

#     def inner_function():
#         local_item = "Eggs"  # Local scope

#         global pantry_item
#         pantry_item = "Brown Sugar"  # Modify the global variable

#         nonlocal counter_item
#         counter_item = "Whole Wheat Flour"  # Modify the enclosing variable

#         print(f"  Inner sees: {local_item}, {counter_item}, and {pantry_item}")

#     print(f"Before inner call, outer sees: {counter_item}")
#     inner_function()
#     print(f"After inner call, outer sees: {counter_item} (modified by inner)")

# print(f"Before outer call, global pantry has: '{pantry_item}'")
# outer_function()
# print(f"After outer call, global pantry has: '{pantry_item}'")



# print("\n--- 5. Lambda Functions ---")
# # Mental Model: A disposable, single-use gadget.
# # lambda arguments: expression
# add_lambda = lambda x, y: x + y
# print(f"Lambda function: 5 + 3 = {add_lambda(5, 3)}")

# # Often used for short operations, like sorting
# points = [(1, 5), (9, 2), (4, 7)]
# # Sort by the second element (y-value) using a lambda as the key
# points.sort(key=lambda point: point[1])
# print(f"Sorted points by y-value: {points}")


# print("\n--- 6. Recursion ---")
# # Mental Model: Russian nesting dolls.
# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")  # Base case: The condition to stop.
#         return
#     print(n)
#     countdown(n - 1)  # Recursive step: Call self with a smaller problem.

# countdown(3)


# ==========================================
# 5. DECORATORS (@classmethod, @staticmethod, @property)
# ==========================================
print("\n--- 5. Method Decorators & Properties ---")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    # @property: Access a method like an attribute (getter)
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    # Setter for the property
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

    # @classmethod: Works with the class, not the instance (Factory method)
    @classmethod
    def from_kelvin(cls, kelvin):
        return cls(kelvin - 273.15)

    # @staticmethod: Utility function, doesn't need self or cls
    @staticmethod
    def is_hot(celsius):
        return celsius > 30

temp = Temperature(25)
print(f"25C is {temp.fahrenheit}F (Calculated via property)")

hot_day = Temperature.is_hot(35) # Static method call
print(f"Is 35C hot? {hot_day}")