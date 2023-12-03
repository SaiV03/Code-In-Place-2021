def main():
    mass = float(input('Enter kilos of mass: '))
    C = 299792458
    energy_in_joules = mass * (C ** 2)
    print('e = m * C^2')
    print(f" m = {mass}")
    print("C = 299792458 m/s")
    print(f"{energy_in_joules} joules of energy!")


if __name__ == "__main__":
    main()
