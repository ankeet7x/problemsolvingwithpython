import random

name = input("What's your name nigga ?")

print("Hey " + name + " Let's play")

a = [ 
    "locker", "mobile", "cinema", "duster", "guitar",
]

guessed_word = "******"
word = random.choice(a)

mistake_count = 10
wrongguess = ''
guess = ''
disp = ''

while(mistake_count > 0):
    guess = input("Input your guess\n")
    
    if(guess in word):
        if(guess in disp):
            
            print("You have already given " + guess + " as input")
        else:
            print("You guessed " + guess + " which is correct")
            pos = word.index(guess)
            
            guessed_word = guessed_word[:pos] + guess + guessed_word[pos+1:]
            print(guessed_word)
            

            disp = disp + guess                                   
            if(len(disp)== len(word)):
                print("You won")
                break
    else:
        wrongguess = wrongguess + guess
        if(len(wrongguess) == 1):
            print("Previous wrong guess is " + wrongguess)
        else:
            print("Previous wrong guesses were " +" "+ wrongguess)

        mistake_count = mistake_count-1
        if(mistake_count>0):
            print("You have " + str(mistake_count) + " guesses")
        else:
            print("You're hanged lol")
