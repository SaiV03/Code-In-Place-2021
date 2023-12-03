def main():
    year = int(input('Please input a year: '))

    # checking whether the provided year is evenly divisibly by 4
    if (year % 4 and year%100) == 0:
		
         print("That's a leap year!")
    else:
          print("That's not a leap year.")
        

if __name__ == "__main__":
    main()
