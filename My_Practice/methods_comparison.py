"""
methods_comparison.py
This script demonstrates the difference between Normal Methods (Actions)
and Getters/Setters (State Control).
"""

class VideoGameCharacter:
    def __init__(self, name):
        self.name = name
        self._health = 100  # Internal state (protected)

    # ==========================================
    # 1. NORMAL METHOD (The Action)
    # ==========================================
    def attack(self):
        """
        This is a normal method. It performs an action (behavior).
        It doesn't just set a value; it executes logic representing 'doing' something.
        """
        print(f"{self.name} swings their sword!")

    # ==========================================
    # 2. GETTER & SETTER (The Gatekeepers)
    # ==========================================
    # We want to control 'health'. We don't want it to go below 0 or above 100.
    
    @property
    def health(self):
        """Getter: Allows reading the value."""
        return self._health

    @health.setter
    def health(self, value):
        """Setter: Allows writing the value, BUT with rules (Validation)."""
        if value < 0:
            print("  -> Health cannot be negative! Setting to 0.")
            self._health = 0
        elif value > 100:
            print("  -> Health cannot exceed 100! Setting to 100.")
            self._health = 100
        else:
            self._health = value

def main():
    player = VideoGameCharacter("Hero")

    # 1. Using a Normal Method (Action)
    # We use parentheses () because we are commanding an action.
    player.attack() 

    # 2. Using Getter/Setter (State Access)
    # We look like we are just using a variable (no parentheses), but logic runs.
    player.health = 150  # Triggers the Setter (Validation logic runs)
    print(f"Current Health: {player.health}") # Triggers the Getter

if __name__ == "__main__":
    main()