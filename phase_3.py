"""
Phase 3: Data Structures (Collections)
This script demonstrates how to store and manage groups of data.
"""
"""🧠 The Mental Model: Phase 3
Think of your program's memory as a kitchen. Phase 1 gave you individual ingredients (numbers, strings). Phase 3 gives you the containers to organize them.

Lists - A Shopping List:

It's a piece of paper where you write down items in order. You can add new items to the bottom (append), cross items off (pop), change an item, or reorder the entire list (sort). It's your all-purpose, flexible container.
Tuples - A Published Recipe:

These are the ingredients and steps for a recipe that has been finalized and published. The steps are ordered, but you cannot change them. This immutability guarantees that the recipe won't be accidentally altered while you're cooking.
Dictionaries - A Spice Rack:

Each jar has a unique label (the key) and contains a specific spice (the value). You don't care about the order of the jars on the rack; you just want to grab "Cinnamon" instantly by its label. It's incredibly fast for lookups.
Sets - A Bowl of Unique Fruits:

This is a fruit bowl where you can only have one of each type of fruit. You can't have two identical apples. The main questions you ask are: "Is there an apple in the bowl?" (in) or "What fruits do I get if I combine my bowl with a friend's?" (union). The arrangement doesn't matter.
Mutability vs. Immutability - The Original vs. The Photocopy:

Immutable (Tuples, Strings): When you pass an immutable variable, you're giving someone a photocopy. They can write on their copy all they want, but the original is safe.
Mutable (Lists, Dictionaries): When you pass a mutable variable, you're giving someone a link to a shared document. Any change they make is a change to the one and only original document.
Comprehensions - The Magical Assembler:

Instead of building a shopping list one item at a time (for loop), you give a single, concise command: "Give me a list of all the even numbers from 1 to 100." It's a powerful and "Pythonic" way to build collections instantly."""
def main():
    # ==========================================
    # 1. LISTS (The Shopping List - Mutable)
    # ==========================================
    print("--- 1. Lists ---")
    # An ordered, changeable collection.
    
    shopping_list = ["milk", "eggs", "bread"]
    print(f"Original list: {shopping_list}")
    
    # Indexing and Slicing
    print(f"First item: {shopping_list[0]}")
    print(f"Last two items: {shopping_list[1:]}")
    
    # Methods
    shopping_list.append("apples")  # Add an item
    shopping_list[1] = "butter"     # Change an item
    removed_item = shopping_list.pop() # Remove the last item
    shopping_list.sort()            # Sorts the list in-place
    
    print(f"Modified list: {shopping_list}")
    print(f"Removed item: {removed_item}")

    # ==========================================
    # 2. TUPLES (The Published Recipe - Immutable)
    # ==========================================
    print("\n--- 2. Tuples ---")
    # An ordered, unchangeable collection.
    
    coordinates = (10.0, 20.5)
    print(f"Coordinates: {coordinates}")
    
    # Unpacking
    x, y = coordinates
    print(f"Unpacked: x={x}, y={y}")
    
    # Trying to change a tuple will raise a TypeError
    try:
        coordinates[0] = 5.0
    except TypeError as e:
        print(f"Error when changing a tuple: {e}")

    # ==========================================
    # 3. DICTIONARIES (The Spice Rack - Key-Value)
    # ==========================================
    print("\n--- 3. Dictionaries ---")
    # Unordered (in older Python), key-value pairs. Fast lookups.
    
    spice_rack = {"cinnamon": "sweet", "cayenne": "spicy", "oregano": "savory"}
    print(f"Spice rack: {spice_rack}")
    
    # Accessing values
    print(f"Cinnamon is {spice_rack['cinnamon']}")
    
    # Safe access with .get() (avoids errors for missing keys)
    paprika_taste = spice_rack.get("paprika", "not found")
    print(f"Taste of paprika: {paprika_taste}")
    
    # Iterating
    print("Spices and their tastes:")
    for spice, taste in spice_rack.items():
        print(f"  - {spice}: {taste}")

    # ==========================================
    # 4. SETS (The Bowl of Unique Fruits)
    # ==========================================
    print("\n--- 4. Sets ---")
    # Unordered collection of unique items.
    
    my_fruits = {"apple", "banana", "cherry"}
    friend_fruits = {"banana", "orange", "mango"}
    
    # Set Operations
    all_fruits = my_fruits.union(friend_fruits)
    common_fruits = my_fruits.intersection(friend_fruits)
    
    print(f"My fruits: {my_fruits}")
    print(f"Combined fruits (union): {all_fruits}")
    print(f"Common fruits (intersection): {common_fruits}")

    # ==========================================
    # 5. MUTABILITY vs. IMMUTABILITY
    # ==========================================
    print("\n--- 5. Mutability vs. Immutability ---")
    
    # Immutable example (like a photocopy)
    a = 5
    b = a
    a = 10 # 'a' gets a new value, 'b' is unaffected
    print(f"Immutable: a={a}, b={b}")
    
    # Mutable example (like a shared document link)
    list_a = [1, 2]
    list_b = list_a
    list_a.append(3) # We modify the list via 'list_a'
    print(f"Mutable: list_a={list_a}, list_b={list_b}") # 'list_b' sees the change!

    # ==========================================
    # 6. COMPREHENSIONS (The Magical Assembler)
    # ==========================================
    print("\n--- 6. Comprehensions ---")
    
    # List comprehension: [expression for item in iterable if condition]
    squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Squares of even numbers: {squares}")
    
    # Dictionary comprehension
    square_dict = {x: x**2 for x in range(5)}
    print(f"Dictionary of squares: {square_dict}")

if __name__ == "__main__":
    main()