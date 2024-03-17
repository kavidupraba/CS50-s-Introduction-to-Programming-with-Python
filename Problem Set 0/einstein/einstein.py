

#Creating main function
def main():
    #using try and catch to handle user input
    try:
       up1=input("Please input your Mass value: ")#assign user input to new variable

       if "Kg" in up1:#check if user add "Kg" or "KG" on input
           up1=up1.strip("Kg")
       elif "KG" in up1:
           up1=up1.strip("KG")
       else:
           pass#if there is no any kg simply passing

       up1=int(up1)#converting usser input
       calculate(up1)

    except Exception as er:
        #hadling exception
        print("Ivalide input",str(er))
    finally:

        #just try to give a hint to the user
        if "kg"==up1 or "KG"==up1:
            print("you miss the mass value! ex: 5kg")
        else:
            print("try again!")

#creating function to calculate E=mc^2

def calculate(M):
    C = 300000000
    E = M * pow(C, 2)  # using pow() to get c^2
    print(E)


#calling the main function
main()