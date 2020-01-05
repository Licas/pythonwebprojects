
secret_number = 9
i = 0
while i < 3:
    i+=1
    guess_number = input("Guess a number (1 to 10): ")
    if int(guess_number) == secret_number:
        print("You Win!")
        break
else:
    print("You loose!")