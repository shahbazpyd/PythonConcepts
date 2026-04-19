"""
javastyle_getset_demo.py
This script demonstrates using normal methods as "Java-style" getters and setters,
as an alternative to the @property decorator.
"""

class VideoGameCharacter:
    def __init__(self, name):
        self.name = name
        self._health = 100  # Internal state (protected)

    def attack(self):
        """A normal action method."""
        print(f"{self.name} swings their sword!")

    # ==========================================
    # "Java-style" Getter and Setter Methods
    # ==========================================

    def get_health(self):
        """
        Getter Method: A normal method that returns the internal state.
        """
        return self._health

    def set_health(self, value):
        """
        Setter Method: A normal method that validates and sets the internal state.
        """
        if not isinstance(value, int):
            print("  -> Health must be an integer.")
            return # Stop execution

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

    # Using the normal methods requires parentheses ()
    player.set_health(150)
    
    current_hp = player.get_health()
    print(f"Current Health: {current_hp}")

if __name__ == "__main__":
    main()