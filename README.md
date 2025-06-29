# codeAlpha_HangmanShowdown
# 🎯 Hangman Game in Python

A beginner-friendly **text-based Hangman game** built with Python. This version includes:

- Difficulty levels: Easy, Medium, Hard
- Visual hangman graphics (console-based)
- Hint system (reveals a letter)
- Input validation and feedback
- Replay support
- Clean and readable code, perfect for learning

---

## 🕹️ How to Play

1. Choose a difficulty level when prompted.
2. Guess one letter at a time.
3. You have **6 wrong guesses** before the game ends.
4. Type `hint` to reveal a random letter (limited to 2 hints per game).
5. Replay the game after winning or losing.

---

## ✅ Features

- 📚 Word lists by difficulty
- 🧠 Hint system with limited uses
- 🎨 ASCII art hangman stages
- 🧼 Clear console between turns
- 🔁 Option to play again without restarting

---

## 🚀 Getting Started

### Requirements
- Python 3.x

### Run the Game

```bash
python hangman.py

🛠️ Code Structure

hangman_pics — ASCII art stages of the hangman

word_list — dictionary with words categorized by difficulty

play_game() — main function handling the game loop and logic

clear_screen() — clears terminal screen between guesses

display_intro() — shows welcome message and instructions

🧑‍💻 Author
Developed with ❤️ by Malik Kamran Ali
