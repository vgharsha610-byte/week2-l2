
# 📘 Assignment: Games in Python

## 🎯 Objective

Learn game development fundamentals by building the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Implement Game Setup and Word Selection

#### Description
Create the foundation of the Hangman game by setting up word selection and tracking game state.

#### Requirements
Completed program should:

- Define a list of words to choose from (at least 5 words)
- Randomly select one word at the start of the game
- Initialize variables to track incorrect guesses remaining (e.g., 6 attempts)
- Display the word progress in underscore format (e.g., `_ _ _ _`)


### 🛠️ Implement Letter Guessing Logic

#### Description
Build the core game loop that handles player guesses and updates game state.

#### Requirements
Completed program should:

- Accept letter guesses from the user via `input()`
- Check if the guessed letter is in the word
- Update the word display to reveal correctly guessed letters
- Decrement remaining attempts if the guess is incorrect
- Display current progress, remaining guesses, and guessed letters after each turn


### 🛠️ Implement Win/Lose Conditions

#### Description
Add end-game logic to determine and display whether the player won or lost.

#### Requirements
Completed program should:

- Check if the player has guessed the complete word (win condition)
- Check if the player has run out of attempts (lose condition)
- Display appropriate win/lose messages
- Show the final word when game ends
- Offer the player the option to play again
