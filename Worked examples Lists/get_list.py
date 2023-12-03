def main():
    lst = []
    value = input('Enter a value: ')
    while value!='':
        lst.append(value)
        value = input('Enter a value: ')
    print(f'Here\'s the list: \n{lst}')
        

if __name__ == "__main__":
    main()
