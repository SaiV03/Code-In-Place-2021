def main():
    #Creating a list of names
    names = ['Anton','Beth','Chen','Drew','Ethan']
    # Computing ages 

    age_a,age_b,age_c=21,6,20
    age_d = age_c+age_a
    age_e = age_c

    #A list of ages 
    ages = [age_a,age_b,age_c,age_d,age_e]

    for name,age in zip(names,ages):
         print(name,age)


if __name__ == '__main__':
    main()
