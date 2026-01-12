"""
Phase 2: Control Flow
This script demonstrates how to direct the execution of code using conditionals, loops, and matching.
"""
"""🧠 The Mental Model: Phase 2
If Phase 1 was about the actors (variables) and props (data types), Phase 2 is the script's direction. It tells the actors where to go and when to stop.

Conditionals (if/elif/else) - The Fork in the Road:

Imagine driving. You see a sign.
If the light is green, go.
Else if (elif) the light is yellow, slow down.
Else (red), stop.
The code only takes one of these paths.
Loops - The Assembly Line:

for loop: You have a checklist of 5 items. You do the exact same task for item 1, then item 2, until the list is done.
while loop: You are filling a bucket with water. You don't know exactly how many seconds it will take, but you keep the tap open while the bucket is not full.
Control Keywords - The Traffic Signs:

break: Emergency Exit. Stop the assembly line immediately and leave the factory.
continue: Skip this item. "This apple is rotten, throw it out and grab the next one immediately."
pass: "Under Construction." A placeholder sign that says "I will build a bridge here later, but for now, just drive through."
The Walrus Operator (:=) - The "Look and Grab":

Usually, you look at a price tag (check condition) and then write it down (assignment) in two steps.
The Walrus lets you look at the price and write it down in a single glance.
Pattern Matching (match/case) - The Shape Sorter:

Imagine a toy box with holes for shapes. You hold an object (variable).
Does it fit in the square hole? No.
The triangle hole? Yes -> Drop it in (execute code).
It's cleaner than checking 10 different if statements."""
def main():
    # ==========================================
    # 1. CONDITIONAL STATEMENTS (The Fork in the Road)
    # ==========================================
    print("--- 1. Conditional Statements ---")
    # Mental Model: A security checkpoint. You only pass if you have the right ID.
    age = 20
    
    if age >= 21:
        print("Access Granted: VIP Section")
    elif age >= 18:
        print("Access Granted: General Admission")
    else:
        print("Access Denied")

    # ==========================================
    # 2. LOOPS (The Cycle)
    # ==========================================
    print("\n--- 2. Loops ---")
    
    # A. FOR LOOP (Iterating over a sequence)
    # Mental Model: Processing items on a conveyor belt.
    print("For Loop (Fruits):")
    fruits = ["Apple", "Banana", "Cherry"]
    for fruit in fruits:
        print(f"  Eating {fruit}")

    # B. RANGE FUNCTION
    # range(start, stop, step) - stop is exclusive
    print("For Loop (Range):")
    for i in range(1, 10, 2): # 1, 3, 5, 7, 9
        print(f"  Step {i}")

    # C. WHILE LOOP
    # Mental Model: Keep running until a condition changes (like a battery draining).
    print("While Loop:")
    battery = 3
    while battery > 0:
        print(f"  Battery: {battery}%")
        battery -= 1
    print("  System Shutdown")

    # ==========================================
    # 3. CONTROL KEYWORDS
    # ==========================================
    print("\n--- 3. Control Keywords ---")
    
    for number in range(10):
        if number == 3:
            print(f"  Skipping {number} (continue)")
            continue  # Skip the rest of this iteration
        
        if number == 5:
            pass      # Placeholder: Do nothing, just pass through
            # print("  (Passed 5)") 
        
        if number == 7:
            print(f"  Stopping at {number} (break)")
            break     # Exit the loop completely
            
        print(f"  Processing {number}")

    # ==========================================
    # 4. THE WALRUS OPERATOR (:=)
    # ==========================================
    print("\n--- 4. The Walrus Operator ---")
    # Assigns a value to a variable as part of a larger expression.
    # Useful for checking a value and using it immediately.
    
    text = "Hello Python"
    # We assign length to 'n' AND check if 'n > 5' in one line.
    if (n := len(text)) > 5:
        print(f"String is long! It has {n} characters.")

    # ==========================================
    # 5. PATTERN MATCHING (Python 3.10+)
    # ==========================================
    print("\n--- 5. Pattern Matching ---")
    # Mental Model: A coin sorting machine.
    
    status_code = 404
    
    match status_code:
        case 200:
            print("Success (200)")
        case 400 | 404:  # Matches 400 OR 404
            print("Client Error (400 or 404)")
        case 500:
            print("Server Error (500)")
        case _:          # Wildcard (matches anything else)
            print("Unknown Status")

if __name__ == "__main__":
    main()