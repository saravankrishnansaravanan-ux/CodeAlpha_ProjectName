import random
# ── Predefined word list ──────────────────────────────────────────────────────
WORDS = ["python", "hangman", "keyboard", "science", "puzzle"]
# ── ASCII art stages (0 = fresh gallows → 6 = full hangman) ──────────────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]
MAX_WRONG = 6
def display_state(secret: str, guessed: set, wrong: int) -> None:
    """Print the current gallows, masked word, and game stats."""
    print(HANGMAN_STAGES[wrong])
    # Show guessed letters or blanks
    masked = " ".join(ch if ch in guessed else "_" for ch in secret)
    print(f"  Word  : {masked}")
    print(f"  Wrong guesses left : {MAX_WRONG - wrong}")
    wrong_letters = sorted(ch for ch in guessed if ch not in secret)
    if wrong_letters:
        print(f"  Incorrect letters  : {', '.join(wrong_letters)}")
    print()
def get_valid_guess(guessed: set) -> str:
    """Prompt the player until they enter a fresh, single alphabetical letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("  ⚠  Please enter exactly one letter.\n")
        elif not guess.isalpha():
            print("  ⚠  Letters only, no numbers or symbols.\n")
        elif guess in guessed:
            print(f"  ⚠  You already guessed '{guess}'. Try another one.\n")
        else:
            return guess
def play_game(secret: str) -> bool:
    """Run one round of Hangman. Returns True if the player wins."""
    guessed: set = set()
    wrong = 0
    print("\n" + "=" * 40)
    print("        ✦  HANGMAN  ✦")
    print("=" * 40)
    print(f"  The secret word has {len(secret)} letter(s). Good luck!\n")
    while wrong < MAX_WRONG:
        display_state(secret, guessed, wrong)
        guess = get_valid_guess(guessed)
        guessed.add(guess)
        if guess in secret:
            print(f"  ✓  Nice! '{guess}' is in the word.\n")
            # Check win condition
            if all(ch in guessed for ch in secret):
                display_state(secret, guessed, wrong)
                print("  🎉  You won! The word was:", secret.upper())
                return True
        else:
            wrong += 1
            print(f"  ✗  '{guess}' is not in the word. ({wrong}/{MAX_WRONG} wrong)\n")
    # Player ran out of guesses
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"  💀  Game over! The word was: {secret.upper()}")
    return False
def main() -> None:
    print("\nWelcome to Hangman!")
    print("Guess the hidden word letter by letter.")
    print("You have 6 chances before the hangman is complete.\n")
    while True:
        secret_word = random.choice(WORDS)
        play_game(secret_word)
        print()
        # Require full-word answers: only accept 'yes' or 'no'
        while True:
            try:
                again = input("  Play again? (yes / no): ").strip().lower()
            except KeyboardInterrupt:
                print("\n\n  Thanks for playing! Goodbye. 👋\n")
                return
            if again in ("yes", "no"):
                break
            print("  Please answer 'yes' or 'no'.\n")

        if again == "no":
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break
if __name__ == "__main__":
    main()
