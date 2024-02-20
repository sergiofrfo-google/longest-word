import random
class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.grid = random.choices(letters, k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        word_letters = list(word.upper())
        grid_copy = self.grid.copy()

        # Check if all letters of the word are present in the grid
        for letter in word_letters:
            if letter in grid_copy:
                grid_copy.remove(letter)
            else:
                return False

        return True
