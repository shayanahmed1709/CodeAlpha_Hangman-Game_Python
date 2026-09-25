import random

def play_hangman():
    # 1. Predefined list of 5 words
    words = ["python", "hangman", "coding", "developer", "computer"]
    word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("================================")
    print("   Welcome to Text Hangman!     ")
    print("================================")
    print(f"You are allowed up to {max_incorrect} incorrect guesses.")
    
    while incorrect_guesses < max_incorrect:
        # Build the current word display (e.g., p _ t h _ n)
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Check for win condition
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You successfully guessed the word: {word}")
            return
            
        # Get console input
        guess = input("Guess a letter: ").lower().strip()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input. Please enter a single alphabetical letter.")
            continue
            
        if guess in guessed_letters:
            print("⚠️ You already tried that letter. Pick a different one.")
            continue
            
        # Add to guessed list
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Incorrect! '{guess}' is not in the word.")
            
    # Lose condition
    print(f"\n💀 Game Over! You ran out of guesses. The correct word was: {word}")

if __name__ == "__main__":
    play_hangman()
