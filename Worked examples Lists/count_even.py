SAMPLE_LIST = [1,2,3,4,5,6]

def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    counter=0
    for x in lst:
        if x%2==0:
            counter+=1
    print(counter)

def main():
    count_even(SAMPLE_LIST)

if __name__ == "__main__":
    main()
