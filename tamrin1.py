import random


words_bank = ["tree","book", "blue", "train", "fish", "woman", "life", "freedom", "iran", "sky"]
user_mistakes = 0

good_chars= []
bad_chars = []

word=random.choice(words_bank)

while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
        else:
            print("-", end=" ")
    if len(good_chars) == len(word):
        print("congratuate man you win")
    
        break
    user_char = str.lower(input(("please write your guess: ")))
  
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            bad_chars.append(user_char)
            user_mistakes += 1 
            print("❌")
    else:
        print("mesle adam vared kon")

if user_mistakes == 6:
    print("❌Game Over❌")