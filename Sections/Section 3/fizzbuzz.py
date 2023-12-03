"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    fizzed=0
    buzzed=0
    fizzbuzzed=0
    num = int(input('Number to count to: '))
    for x in range(1,num+1):

        if (x%5==0 and x%3==0):
            fizzbuzz()
            fizzbuzzed+=1
            
        elif x%3==0:
            say_fizz()
            fizzed+=1

        elif x%5==0:
            say_buzz()
            buzzed+=1
        
        else:
            print(x)
    print(f'Num fizzed: {fizzed}')
    print(f'Num buzzed: {buzzed}')
    print(f'Num fizzbuzzed: {fizzbuzzed}')


    
def say_fizz():
     print('Fizz')
def say_buzz():
     print('Buzz')  
def fizzbuzz():
     print('Fizzbuzz')
if __name__ == '__main__':
    main()
