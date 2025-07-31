import operation
import read
import write

print("\n")
print("\t\t\tPrabal Electronics")
print("\tAddress : Kamalpokhari,Kathmandu || Phone : 01-223344")

print("--------------------------------------------------------------------------------")
print("\t You have successfully entered in our system.");
print("--------------------------------------------------------------------------------")


conti=True
while conti==True:
    print("These are the options for you to carry out :")
    print("  1) Sell to customer")
    print("  2) Purchase from manufacturer")
    print("  3) Exit the system")
    print("--------------------------------------------------------------------------------")
    try:
        do=int(input("What would you like to do :"))
    except:
        print("\n")
        print("You've entered invalid input. Please enter integer/numeric value.")
        do=int(input("What would you like to do :"))
    print("--------------------------------------------------------------------------------")

    a=read.read_()
    if do==1:
        b=operation.pur(a)
        write.write_(b)
        inp_=input("Enter Y to continue in our system :").upper()
        if inp_!="Y":
            conti=False
    elif do==2:
        b=operation.sell_(a)
        write.write_(b)
        inp_=input("Enter Y to continue in our system :").upper()
        if inp_!="Y":
            conti=False
    elif do==3:
        print("Thanks for your visiting.")
        break
    elif do==0:
        print("Please enter valid input.")
        print("--------------------------------------------------------------------------------")
    elif do>3:
        print("Please enter valid input.")
        print("--------------------------------------------------------------------------------")

    

        
