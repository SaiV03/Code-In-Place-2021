"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

def main():
    num = int(input('Type a number: '))
    total=0
    while num!=-1:
        total+=num
        num = int(input('Type a number: '))
        
        if num==-1:
            break
    print(f'total is {total}')



if __name__ == '__main__':
    main()
