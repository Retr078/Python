guess_count = 1 
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print("Done, moving on to next game")
print("----------------------------")
#-----------------------------------------------------------------

secrete_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess the number im thinking, you have three chances: '))
    guess_count += 1
    if secrete_number == guess:
        print("You won")
        break
else:
    print("You failed!")
    

