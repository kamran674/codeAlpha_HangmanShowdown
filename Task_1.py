import random
import os
from time import sleep

# Hangman stages (from 0 to 6 wrong guesses)
hangman_pics = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

# Expanded word list with difficulty levels
word_list = {
    "easy": ["apple", "chair", "house", "water", "pizza", "happy", "sunny", "music"],
    "medium": ["elephant", "guitar", "diamond", "jungle", "bicycle", "library"],
    "hard": ["xylophone", "quasar", "jazz", "awkward", "pneumonia", "rhythm"]
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():
    print("""
    🎯 WELCOME TO HANGMAN! 🎯
    --------------------------
    Guess the word one letter at a time.
    You get 6 wrong guesses before you lose.
    Type 'hint' for help (but it reveals a letter!).
    """)

def get_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in word_list:
            return difficulty
        print("⚠️ Please choose easy, medium, or hard.")

def play_game():
    clear_screen()
    display_intro()
    difficulty = get_difficulty()
    secret_word = random.choice(word_list[difficulty]).lower()
    
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 6
    display_word = ["_" for _ in secret_word]
    hints_remaining = 2

    while wrong_guesses < max_guesses and "_" in display_word:
        clear_screen()
        print(hangman_pics[wrong_guesses])
        print("\nWord: ", " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Wrong guesses left: {max_guesses - wrong_guesses}")
        print(f"Hints remaining: {hints_remaining}")
        
        guess = input("\nEnter a letter or 'hint': ").strip().lower()
        
        # Handle hint request
        if guess == "hint":
            if hints_remaining > 0:
                hidden_indices = [i for i, letter in enumerate(secret_word) if display_word[i] == "_"]
                if hidden_indices:
                    hint_pos = random.choice(hidden_indices)
                    display_word[hint_pos] = secret_word[hint_pos]
                    guessed_letters.append(secret_word[hint_pos])
                    hints_remaining -= 1
                    print(f"\n💡 Hint revealed: '{secret_word[hint_pos]}'")
                else:
                    print("\nNo more letters to reveal!")
            else:
                print("\nYou've used all your hints!")
            sleep(2)
            continue
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️ Please enter a single letter.")
            sleep(1)
            continue
        
        if guess in guessed_letters:
            print("\n❗ You already guessed that letter.")
            sleep(1)
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("\n✅ Correct!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print("\n❌ Wrong guess!")
        
        sleep(1)
    
    # Game over screen
    clear_screen()
    print(hangman_pics[wrong_guesses])
    print("\nWord: ", " ".join(display_word))
    
    if "_" not in display_word:
        print(f"\n🎉 YOU WIN! The word was: {secret_word.upper()}")
    else:
        print(f"\n💀 GAME OVER! The word was: {secret_word.upper()}")
    
    # Play again?
    if input("\nPlay again? (y/n): ").lower() == 'y':
        play_game()
    else:
        print("\nThanks for playing Hangman! 👋")

# Start the game
if __name__ == "__main__":
    play_game()