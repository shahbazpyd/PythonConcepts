"""
Phase 9: Ecosystem & Best Practices
This script demonstrates professional standards: Logging, Testing, Documentation, and Style.
"""

"""🧠 The Mental Model: Phase 9
Phase 9 is about moving from "coding in your garage" to "building a skyscraper". It's about standards, safety, and collaboration.

Virtual Environments (venv) - The Fenced-Off Construction Site:

Imagine building a house. You don't dump your bricks on the public highway; you fence off a specific area.
A Virtual Environment is that fence. It ensures that the tools (libraries) you use for Project A don't accidentally mess up Project B.
Package Management (pip, requirements.txt) - The Supply Manifest:

You need specific materials (bricks, cement). You don't just guess.
requirements.txt is your shopping list. If you hand this list to another builder (pip install -r), they can build an exact replica of your house with the exact same materials.
Testing (unittest, pytest) - The Safety Inspector:

Before you let people live in the house, an inspector comes in. They check: "If I flush the toilet, does the roof leak?"
Tests are automated inspectors. They run every time you change the code to ensure you didn't accidentally break the plumbing while painting the walls.
Documentation (Docstrings) - The User Manual:

You built a complex thermostat. If you don't leave a manual, the homeowner will freeze.
Docstrings are the manual written directly on the device, explaining what inputs it needs and what it does.
PEP 8 - The Building Code:

There are rules: "Wiring must be blue, pipes must be red."
PEP 8 is the style guide. It ensures that any electrician (developer) who walks onto the site later understands the wiring immediately, because it follows the standard code.
Logging - The Security Camera:

print() is like shouting "Hey!" in the hallway. It's ephemeral and annoying.
Logging is a security camera recording. It timestamps exactly what happened ("Door opened at 10:00 PM"), how severe it was ("Warning: Window cracked"), and saves it to a tape (file) for review after a crash."""
import logging
import unittest

# ==========================================
# 1. LOGGING (The Security Camera)
# ==========================================
# Mental Model: print() is ephemeral shouting. Logging is a permanent record.
# We configure the logger to write to the console (or file) with timestamps and severity.

# Configure logging (usually done at the very start of the app)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger(__name__)

# ==========================================
# 2. DOCUMENTATION & PEP 8 (The Manual & Building Code)
# ==========================================

def complex_calculation(a: int, b: int) -> float:
    """
    Performs a division to demonstrate logging and documentation.
    
    This function follows PEP 8 (snake_case, spacing) and includes a docstring.
    
    Args:
        a (int): The numerator.
        b (int): The denominator.
        
    Returns:
        float: The result of the division.
        
    Raises:
        ValueError: If b is zero.
    """
    logger.info(f"Starting calculation with a={a}, b={b}")
    
    if b == 0:
        # Log the error before raising it, so we have a record
        logger.error("Attempted division by zero!")
        raise ValueError("Cannot divide by zero")
        
    result = a / b
    logger.debug(f"Calculation result: {result}")
    return result

# ==========================================
# 3. TESTING (The Inspector)
# ==========================================
# Mental Model: An automated inspector that checks if the code works as expected.
# We use 'unittest' (built-in) here. 'pytest' is also very popular.

class TestCalculation(unittest.TestCase):
    def test_success(self):
        """Test that valid input returns correct result."""
        self.assertEqual(complex_calculation(10, 2), 5.0)
        
    def test_failure(self):
        """Test that invalid input raises the correct error."""
        with self.assertRaises(ValueError):
            complex_calculation(10, 0)

def main():
    print("--- 1. Ecosystem Concepts (Mental Models) ---")
    print("Virtual Environments (venv): A fenced-off construction site.")
    print("  Command: python -m venv my_env")
    print("Package Management (pip): The supply manifest.")
    print("  Command: pip install -r requirements.txt")
    print("PEP 8: The building code (style guide).")
    
    print("\n--- 2. Logging Demo ---")
    # Notice how the logs appear with timestamps
    try:
        val = complex_calculation(10, 2)
        print(f"  (Print Output) Result: {val}")
        
        # This will trigger the error log
        complex_calculation(10, 0)
    except ValueError:
        print("  (Print Output) Caught expected error.")

    print("\n--- 3. Running Tests ---")
    # Running unittest programmatically
    # exit=False is crucial here, otherwise the script stops immediately!
    # argv=['first-arg-is-ignored'] prevents unittest from trying to parse our script's CLI args
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == "__main__":
    main()