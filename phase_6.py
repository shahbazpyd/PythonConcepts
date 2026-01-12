"""
Phase 6: File Handling & Exception Handling
This script demonstrates how to interact with files and manage errors gracefully.
"""

"""🧠 The Mental Model: Phase 6
Phase 6 is about interacting with the outside world (files) and handling the chaos of reality (errors).

Exceptions (try, except, else, finally) - The Trapeze Act:

try: This is the trapeze artist attempting a dangerous stunt.
except: This is the safety net. If the artist falls (ZeroDivisionError), the net catches them so the show doesn't end abruptly with a crash.
else: This is the applause. It only happens if the stunt was successful (no fall).
finally: This is the janitor. Whether the artist landed the stunt or fell into the net, the janitor always comes out to sweep the stage (close connections, clean memory).
Raising Exceptions (raise) - The Fire Alarm:

Sometimes, you detect a problem that you can't fix right there. You pull the fire alarm (raise ValueError) to alert the system that something is wrong, forcing the program to stop or a higher-level "safety net" to handle it.
File I/O (open) - The Library Book:

Opening a file is like checking a book out of a library. You have exclusive access to read or write in it.
Modes:
'r' (Read): Reading the book.
'w' (Write): Erasing the book and writing a new story.
'a' (Append): Writing a post-it note on the last page.
Context Managers (with) - The Automatic Librarian:

If you manually open() a file, you might forget to close() it (return the book). If you crash while reading, the book stays checked out forever (resource leak).
The with statement is an automatic librarian. It hands you the book, and the moment you step away from the desk (exit the code block)—even if you faint (error)—the librarian immediately snatches the book back and checks it in (close())."""

import os

def main():
    # ==========================================
    # 1. EXCEPTIONS (The Safety Net)
    # ==========================================
    print("--- 1. Exceptions (try, except, else, finally) ---")
    
    # Mental Model: A trapeze act.
    # try: Attempt the dangerous stunt.
    # except: The safety net catches you if you fall.
    # else: You take a bow if you succeed.
    # finally: You clean up the stage no matter what.

    user_input = "0" 
    print(f"Attempting to divide 10 by '{user_input}'...")

    try:
        number = int(user_input)
        result = 10 / number
    except ValueError:
        print("  Error: That's not a valid number!")
    except ZeroDivisionError:
        print("  Error: You cannot divide by zero!")
    else:
        print(f"  Success! Result is {result}")
    finally:
        print("  (Cleanup: Execution complete)")

    # ==========================================
    # 2. RAISING & CUSTOM EXCEPTIONS (The Fire Alarm)
    # ==========================================
    print("\n--- 2. Raising & Custom Exceptions ---")

    # Custom Exception: Creating a specific label for a specific problem.
    # Inheriting from Exception class
    class CoffeeTooHotError(Exception):
        """Raised when the coffee temperature is too high."""
        pass

    def drink_coffee(temp):
        if temp > 85:
            # Raising: Pulling the alarm manually.
            raise CoffeeTooHotError(f"Ouch! {temp}C is too hot!")
        print(f"Drinking coffee at {temp}C. Delicious.")

    try:
        drink_coffee(90)
    except CoffeeTooHotError as e:
        print(f"  Caught custom error: {e}")

    # ==========================================
    # 3. FILE I/O & CONTEXT MANAGERS (The Librarian)
    # ==========================================
    print("\n--- 3. File I/O & Context Managers ---")
    
    filename = "example_phase_6.txt"

    # Writing to a file using 'with' (Context Manager)
    # Mental Model: The 'with' keyword is an automatic librarian.
    # It hands you the file, and automatically closes it when you leave the block.
    print(f"Writing to '{filename}'...")
    
    # Mode 'w': Write (Overwrites existing content)
    with open(filename, "w") as file:
        file.write("Hello, File World!\n")
        file.write("This file was created by Python.")

    # Reading from a file
    # Mode 'r': Read (Default)
    print(f"Reading from '{filename}':")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"---\n{content}\n---")
    except FileNotFoundError:
        print("  Error: File not found!")

    # Appending to a file
    # Mode 'a': Append (Adds to the end)
    print("Appending a new line...")
    with open(filename, "a") as file:
        file.write("\nThis line was appended.")

    # Cleanup (deleting the file to keep your folder clean)
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Cleanup: '{filename}' deleted.")

if __name__ == "__main__":
    main()