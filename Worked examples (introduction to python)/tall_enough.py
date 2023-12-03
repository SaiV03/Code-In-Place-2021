

MIN_HEIGHT = 50

def main():
    height = int(input('How tall are you? '))
    if height<MIN_HEIGHT:
        print('You\'re not tall enough to ride!')
    else:
        print("You're tall enough to ride!")
        

if __name__ == "__main__":
    main()
