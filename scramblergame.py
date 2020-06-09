import random

def function():
    words = ['khwopa', 'bhaktapur', 'kathmandu', 'creator', 'apple', 'orange', 'mango', 'grapes', 'watermelon', 'lemon']

    word = random.choice(words)
    # print(word)
    answer = word
    # print(answer)

    word = list(word)
    scramble = ""
    # print(word)

    for letter in range(0, len(word)):
        scramble += word.pop(random.randint(0, len(word) - 1))

    print("\nGuess a word from:", scramble)

    guess = input("\nGuess that word: ")

    while guess.lower() != answer and guess != "":
        print("\n\nSorry! that's wrong :( it was: ", answer)
        print("\n")
        break 

    if guess.lower() == answer :
        print("\n\nYou are correct :) \n")

function()



for i in range(1000):
    redo = input("Want to play again (Y/N): ")
    if redo.upper() == "Y" :
        function()
    if redo.upper() == "N" :
        print("Thanks! for playing")
        print("\n")
        break


