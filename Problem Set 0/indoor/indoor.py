
#create main function
def main():
    #assign the user input to a variable
    up1=input("Please enter your Yelling: ")

    #assign handled userinput to new variable
    hup=handle(up1)

    #finally give output
    print(hup)

#create handling function
def handle(hv1):
    #strip any sapse (LEFT AND RIGHT) that user may have input
    hv1=hv1.strip()

    #turn Yelling into a indoor voice (using of lower() inbuild function)
    hv1=hv1.lower()

    #return Output
    return hv1

#mention of main() function  calling main() function
main()

