import random

from hangman_words import word_list

chosen_word= random.choice(word_list)
lenght_of_word=len(chosen_word)

end_of_game=False
lives=6

from hangman_art import logo
print(logo)

list=[]
for letter in range(0,lenght_of_word):
    list+="_"

while not end_of_game:
    guess = input("Guess a letter : ").lower()

    if guess in list:
        print(f"You've already guesssed {guess}")

    for i in range(0,lenght_of_word):
        if guess == chosen_word[i]:
            list[i]=guess

    if guess not in chosen_word:
        print(f"You guessed {guess},thats not in the word, You lose a life.")
        lives-=1
        if lives==0:
            end_of_game1=True
            print("You Lose.")

    print(f"{' '.join(list)}")

    if "_" not in list:
        end_of_game = True
        print("You win.") 

    from hangman_art import stages
    print(stages[lives])
                      


       
        






   
