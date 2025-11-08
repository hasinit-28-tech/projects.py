import random
word_bank = ['rizz', 'ohio','hasinee','sarahh','hansika','dhatru']
word = random.choice(word_bank)
guessed_word = ['_']* len(word)
attempts = 10
while attempts > 0:
    print("\n current word:" +' '.join(guessed_word))
    guess = input("guess a letter ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
                print ("great  guess" )
    else:
         
        attempts -= 1
        print("wrong guess ! attempts left: " + str(attempts))
        if '_' not in guessed_word :
         print("congratulations !, you guessed all the letters correctly" + word)
         break
else:
    print("sorry u ran out of moves, the word was : " + word)
                   
           
          
                   
