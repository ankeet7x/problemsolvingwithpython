import random

guess = [
    "rock", "paper", "scissor"
]




x = "rock"
y = "paper"
z = "scissor"


game_over = False



while(game_over is False):
    c_guess = random.choice(guess)
    click = input("A: rock\n B: paper\n C: scissor\n")    
    if(click == 'a'):
        humanguess = x
    elif(click=='b'):
        humanguess = y
    elif(click =='c'):
        humanguess = z
    else:
        print("Input a, b or c")
        continue
    
    #comparison with pcguess
    
    if(humanguess== c_guess):
        continue
    if(humanguess == x and c_guess == y):
        print("Your choice is: " + humanguess)
        print("Pc's choice is: "+ c_guess)
        print("Pc won")
        game_over = True
    elif(humanguess== x and c_guess == z):
        print("Your choice is: " + humanguess)
        print("Pc's choice is: " + c_guess)
        print("You won")
        game_over = True
    elif(humanguess == y and c_guess == x):
        print("Your choice is: " + humanguess)
        print("Pc's choice is: " + c_guess)
        print('You won')
        game_over = True
    elif(humanguess == y and c_guess == z):
        print("Your choice is: " + humanguess)
        print("Pc's choice is: " + c_guess)
        print('Pc won')
        game_over = True
    elif(humanguess == z and c_guess == x):
        print("Your choice is: " + humanguess)
        print("Pc's choice is: " + c_guess)
        print('Pc won')
        game_over = True
    elif(humanguess == z and c_guess == y):
        print("Your choice is: " + humanguess)
        print("Pc's choice is: " + c_guess)
        print('You won')
        game_over = True
    
