

#create main function
def main():
    #assign user input to new veriable
    up1=input("Please enter your Quick speech: ")
    handle(up1)

#creating handle() function for handling the user input
def handle(hv1):
    #slowing down (riplace space with ...)
    print(hv1.replace(' ','...'))


# calling main() function
main()