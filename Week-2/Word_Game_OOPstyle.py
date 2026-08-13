import random
import string

class WordGame:


    def __init__(self, max_lives=6):
        self.word = self.get_random_word()
        self.blanks = self.make_blanks()
        self.used_letters = set()
        self.lives = max_lives

    def get_random_word(self):
        words = [
            "python",
            "variable",
            "function",
            "iterator",
            "notebook",
            "pipeline",
            "dataset",
            "computer",
            "research",
            "analytics"
        ]

        return random.choice(words)

    def make_blanks(self):
        return ["_" for _ in self.word]

    def prompt_for_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        found_any = False

        for i, ch in enumerate(self.word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

    def all_blanks_filled(self):
        return "_" not in self.blanks

    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.word)} letters.")
        print(" ".join(self.blanks))

        while True:
            # Ask the user to guess a letter
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check whether the letter is in the word
            if self.reveal_letters(guess):
                print("\nWell done! Nice job! You found a letter.")
                print(" ".join(self.blanks))

                # Check whether the whole word has been guessed
                if self.all_blanks_filled():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.word}")
                    print("GAME OVER")
                    break

            else:
                # The guessed letter was not in the word
                self.lives -= 1

                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))

                # Check whether the player has run out of lives
                if self.lives <= 0:
                    print("\nOut of lives! Better luck next time!")
                    print(f"The word was: {self.word}")
                    print("GAME OVER")
                    break


if __name__ == "__main__":
    game = WordGame()
    game.play()
