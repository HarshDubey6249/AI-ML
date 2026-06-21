
secret_number=9



while True:
    guess=int(input("enter your name"));
   
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct! You guessed the number!")
        break