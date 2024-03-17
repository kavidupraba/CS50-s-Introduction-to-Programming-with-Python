

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #srip "$" from user input
    d=d.strip("$")

    #convert to float
    d=float(d)

    #return the d value
    return d


def percent_to_float(p):
    #strinp "%" from user input
    p=p.strip("%")

    #convert it to float and divid it by 100 at the same time
    p=float(p)/100

    #return p value
    return p


main()