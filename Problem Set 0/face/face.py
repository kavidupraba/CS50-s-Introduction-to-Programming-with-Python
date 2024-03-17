import emoji

#creating the main method
def main():
    #getting user input
    up1=input("Please add happy face or sad face: ")

    #using if elif and else to do procces
    if ":)" in up1 and ":(" in up1:
        print(up1.replace(':)', '🙂').replace(':(','🙁'))
    elif ":)" in up1:
        print(up1.replace(':)','🙂'))
    elif ":(" in up1:
        print(up1.replace(':(','🙁'))

    else:
        print(up1)

#calling main method
main()