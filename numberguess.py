#guess number

def main():

    secret_number = 6

    while True:

        guess = int(input("Guess the number "))

        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("You guessed it!")
            break   

main()