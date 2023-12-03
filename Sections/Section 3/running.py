"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    total()
    
def total():
    # A list is used here to keep in track of the numbers
    lst = []
    total=0
    num = int(input('Enter a value: '))
    while num!=0:
        total+=num
        print(f'Running total is {total}')
        #Appending the numbers entered to the empty list
        lst.append(num)
        #Prining the max and min of the numbers present in the list
        print(f'Maximum so far is {max(lst)}')
        print(f'Minimum so far is {min(lst)}')
        num = int(input('Enter a value: '))

if __name__ == '__main__':
    main()
