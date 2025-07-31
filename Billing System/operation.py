import datetime

def pur(lap_dict):
    '''
    This function takes input from user about which laptop user would like to buy. Then user is asked to input the quantity. Then it is checked if input user given is available or not then all the discount and shipping prices are done and invoice is printed.
    '''

    nam=input("Please enter your name to generate invoice :")
    user_input={}
    laptop_dictionary=lap_dict
    loop=True
  
    while loop==True:
        #Printing the details of laptop from text file. 
        print("--------------------------------------------------------------------------------")
        print("Welcome to purchasing portal, Here are our Laptop options :")
        print("--------------------------------------------------------------------------------")
        print("S.N. \tLaptop Name \tCompany Name \tPrice \tQuantity   Graphic \tRam")
        print("--------------------------------------------------------------------------------")
        for i in range(1,len(laptop_dictionary)+1,1):
            if i==1:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+"   "+laptop_dictionary[i][5])
            elif i==2:  
                print(str(i)+"\t"+laptop_dictionary[i][0]+"     "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+"   "+laptop_dictionary[i][5])
            elif i==3:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"     "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+"   "+laptop_dictionary[i][5])
            elif i==4:
                print(str(i)+"\t "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+"   "+laptop_dictionary[i][5])
            elif i==5:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+"   "+laptop_dictionary[i][5])
            print("--------------------------------------------------------------------------------")
      
        #using try except block.
        try:
            inp=int(input("Please input the S.N. of Laptop would you like to buy:"))
        except:
            print("\n")
            print("You've entered error value.Please enter a integer/numeric value.")
            print("\n")
            inp= int(input("Which Laptop would you like to buy :"))
        print("--------------------------------------------------------------------------------")
     
        while inp<=0 or inp> len(laptop_dictionary):
            print("Please provide a valid Laptop Id!!")
            try:
                inp= int(input("Which Laptop would you like to buy :"))
            except:
                print("\n")
                print("You've entered error value.Please enter a integer/numeric value.")
                print("\n")
                inp= int(input("Which Laptop would you like to buy :"))
            print("--------------------------------------------------------------------------------")
  
        try:
            quant= int(input("Please provide quantity of laptop you want to buy:"))
        except:
            print("\n")
            print("You've entered error value.Please enter a integer/numeric value.")
            print("\n")
            quant= int(input("Please provide quantity of laptop you want to buy:"))
        print("--------------------------------------------------------------------------------")
     
        lap_quantity=laptop_dictionary[inp][3]
        while quant <= 0 or quant > int(lap_quantity):
            print("Sorry we don't currently have "+str(quant)+" "+laptop_dictionary[inp][0]+" laptop right now. Please re-enter the quantity.")
            print("--------------------------------------------------------------------------------")
            try:
                quant= int(input("Please provide quantity of laptop you want to buy:"))
            except:
                print("\n")
                print("You've entered error value.Please enter a integer/numeric value.")
                print("\n")
                quant= int(input("Please provide quantity of laptop you want to buy:"))
            print("--------------------------------------------------------------------------------")
        #entering the data in dictionary.
        user_input[inp]=quant
        
        laptop_dictionary[inp][3]=int(laptop_dictionary[inp][3])-int(quant)
     
        cont=input("Do you want to continue buying (Y/N) :").upper()
        if cont=="N":
            loop=False
        elif cont=="Y":
            loop=True
        else:
            print("\n")
            cont=input("You've entered invalid input. If you want to continue enter Y, if you want to proceed to invoice enter N? :").upper()
            if cont=="N":
                loop=False
    shipping=0
    
    print("--------------------------------------------------------------------------------")
    ship=input("If you want your laptop to be shipped enter Y :").upper()
    if ship=="Y":
        print("--------------------------------------------------------------------------------")
        try:
            print("These are our option for shipping the laptop :")
            deli=int(input("Enter your option\n"
                       "1)Inside Kathmandu Valley\n"
                       "2)Outside Kathmandu Valley ?"))
        except:
            print("\n")
            print("Invalid Input. Please enter integer/numeric value.")
            print("\n")
            print("These are our option for shipping the laptop :")
            deli=int(input("Enter your option: \n"
                       "1)Inside Kathmandu Valley\n"
                       "2)Outside Kathmandu Valley?"))
        if deli==1:
            shipping=500
        elif deli==2:
            shipping=1500
    print("--------------------------------------------------------------------------------")
    #Calculating total.    
    total_amount=0
    for keys in user_input.keys():
        if keys==1:
            razer_unit_price= int(laptop_dictionary[1][2].replace("$",""))
            razer_qty=int(user_input[keys])
            razer_amount=razer_unit_price*razer_qty
            total_amount+=razer_amount
        elif keys==2:
            xps_unit_price= int(laptop_dictionary[2][2].replace("$",""))
            xps_qty=int(user_input[keys])
            xps_amount=xps_unit_price*xps_qty
            total_amount+=xps_amount
        elif keys==3:
            alien_unit_price= int(laptop_dictionary[3][2].replace("$",""))
            alien_qty=int(user_input[keys])
            alien_amount=alien_unit_price*alien_qty
            total_amount+=alien_amount
        elif keys==4:
            swift_unit_price= int(laptop_dictionary[4][2].replace("$",""))
            swift_qty=int(user_input[keys])
            swift_amount=swift_unit_price*swift_qty
            total_amount+=swift_amount
        elif keys==5:
            mac_unit_price= int(laptop_dictionary[5][2].replace("$",""))
            mac_qty=int(user_input[keys])
            mac_amount=mac_unit_price*mac_qty
            total_amount+=mac_amount

    #Applying discount.
    discount=0
    grand_total=0
    disc=0.0
    if total_amount>0 and total_amount<=5000:
        grand_total=total_amount+shipping
    elif total_amount>5000 and total_amount<=10000:
        disc=5.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount+shipping
    elif total_amount>10000 and total_amount<=20000:
        disc=10.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount+shipping
    elif total_amount>20000 and total_amount<=50000:
        disc=15.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount+shipping
    else:
        disc=18.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount+shipping
        
    datim=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    uniq=str(datim)   
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) 
    d=str(t)      

   
    file=open(uniq+"-purchase"+nam+".txt","w")      
    file.write("=====================================================================")
    file.write("\nPRABAL ELECTRONICS \t\t\t\tBill")
    file.write("\nName of Customer: "+str(nam)+"\t\t\t\tTime:"+d)
    file.write("\n=====================================================================")
    file.write("\nLAPTOP            QUANTITY            UNIT PRICE           TOTAL")                     
    file.write("\n---------------------------------------------------------------------")      
    for input_value in user_input.keys():           
        if input_value==1:
            file.write(str("\n"+laptop_dictionary[1][0]+"         "+str(user_input[1])+"                "+laptop_dictionary[1][2]+"               "+str(int(razer_amount))))
        elif input_value==2:
            file.write(str("\n"+laptop_dictionary[2][0]+"                 "+str(user_input[2])+"                 "+laptop_dictionary[2][2]+"                "+str(int(xps_amount))))
        elif input_value==3:
            file.write(str("\n"+laptop_dictionary[3][0]+"           "+str(user_input[3])+"                 "+laptop_dictionary[3][2]+"                "+str(int(alien_amount))))
        elif input_value==4:
            file.write(str("\n"+laptop_dictionary[4][0]+"             "+str(user_input[4])+"                "+laptop_dictionary[4][2]+"                "+str(int(swift_amount))))
        elif input_value==5:
            file.write(str("\n"+laptop_dictionary[5][0]+"       "+str(user_input[5])+"                 "+laptop_dictionary[5][2]+"                "+str(int(mac_amount))))
       
    file.write("\n\n---------------------------------------------------------------------")
    file.write("\n\t\t\t    Total Amount : "+str(int(total_amount)))
    file.write("\n---------------------------------------------------------------------")
    file.write("\n\t\t           "+str(disc)+"% Discounted Amount: "+str(int(discount)))
    file.write("\n---------------------------------------------------------------------")
    file.write("\n\t\t\t            Shipping Total : "+str(shipping))
    file.write("\n---------------------------------------------------------------------")
    file.write("\n\t\t\t            Grand Total : "+str(int(grand_total)))
    file.write("\n=====================================================================")
    file.close()
    #Printing the invoice.
    print("\n")
    print("--------------------------------------------------------------------------------")
    print("Print of INVOICE:")
    file=open(uniq+"-purchase"+nam+".txt","r")
    print(file.read())
    file.close()
    
    return laptop_dictionary

#break
def sell_(lap_dict):
    '''
    This function takes input  about which laptop user would like to buy from distrubutor. Then user is asked to input the quantity.  Discount are applied and invoice is printed.
    '''
    print("\n")
 
    nam=input("Please enter your name to generate invoice :")
    user_quan={}
    laptop_dictionary=lap_dict
    #Loop will be run till user says No
    loop=True
    while loop==True:
      
        print("--------------------------------------------------------------------------------")
        print("Welcome to Distributer's screen, Laptop available are shown below :")
        print("--------------------------------------------------------------------------------")
        print("S.N. \tLaptop Name \tCompany Name \tMarket Price")
        print("--------------------------------------------------------------------------------")
        for i in range(1,len(laptop_dictionary)+1,1):
            if i==1:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            elif i==2:  
                print(str(i)+"\t   "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            elif i==3:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"     "+laptop_dictionary[i][2]+"\t   ")
            elif i==4:
                print(str(i)+"\t "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            elif i==5:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            print("--------------------------------------------------------------------------------")
        try:
           
            inp=int(input("Please input the S.N. of Laptop would you like to buy:"))
            print("\n")
        except:
            print("You've entered error value.Please enter a integer/numeric value.")
            print("\n")
            inp= int(input("Which Laptop would you like to buy :"))
            print("\n")
       
        while inp<=0 or inp> len(laptop_dictionary):
            print("Please provide a valid Laptop Id!!")
            print("\n")
            try:
                inp= int(input("Please input the S.N. of Laptop would you like to buy :"))
                print("\n")
            except:
                print("You've entered error value.Please enter a integer/numeric value.")
                inp= int(input("Please input the S.N. of  Laptop would you like to buy:"))
                print("\n")
        try:
            quant= int(input("How many laptop would you like to buy :"))
            print("\n")
        except:
            print("You've entered error value.Please enter a integer/numeric value.")
            print("\n")
            quant= int(input("How many laptop would you like to buy :"))
            print("\n")
        #entering the data in dictionary.
        user_quan[inp]=quant
        
        laptop_dictionary[inp][3]=int(laptop_dictionary[inp][3])+int(quant)
        
        more=input("Enter Y if you want to buy more laptops :").upper()
        print("\n")
        if more!="Y":
            loop=False
    #calculating total.
    total_amount=0
    for keys in user_quan.keys():
        if keys==1:
            razer_unit_price= int(laptop_dictionary[1][2].replace("$",""))
            razer_qty=int(user_quan[keys])
            razer_amount=razer_unit_price*razer_qty
            total_amount+=razer_amount
        elif keys==2:
            xps_unit_price= int(laptop_dictionary[2][2].replace("$",""))
            xps_quantity=int(user_quan[keys])
            xps_amount=xps_unit_price*xps_quantity
            total_amount+=xps_amount
        elif keys==3:
            alien_unit_price= int(laptop_dictionary[3][2].replace("$",""))
            alien_qty=int(user_quan[keys])
            alien_amount=alien_unit_price*alien_qty
            total_amount+=alien_amount
        elif keys==4:
            swift_unit_price= int(laptop_dictionary[4][2].replace("$",""))
            swift_qty=int(user_quan[keys])
            swift_amount=swift_unit_price*swift_qty
            total_amount+=swift_amount
        elif keys==5:
            mac_unit_price= int(laptop_dictionary[5][2].replace("$",""))
            mac_qty=int(user_quan[keys])
            mac_amount=mac_unit_price*mac_qty
            total_amount+=mac_amount
    #Applying discount.
    discount=0        
    vat=13.0
    total_amount=total_amount+(vat*total_amount)/100        
    grand_total=0
    disc=0.0
    if total_amount>0 and total_amount<=25000:
        grand_total=total_amount
    elif total_amount>25000 and total_amount<=50000:
        disc=10.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
    elif total_amount>50000 and total_amount<=80000:
        disc=15.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
    elif total_amount>80000 and total_amount<=100000:
        disc=18.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
    else:
        disc=25.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount

    datim=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    uniq=str(datim)   
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) 
    d=str(t)      

    #Creating the invoice.
    file=open(uniq+"-sell"+nam+".txt","w")      
    file.write("=====================================================================")
    file.write("\nPRABAL ELECTRONICS \t\t\t\tBill")
    file.write("\nName of Customer: "+str(nam)+"\t\t\t\tTime:"+d)
    file.write("\n=====================================================================")
    file.write("\nLAPTOP            QUANTITY            UNIT PRICE           TOTAL")                     
    file.write("\n---------------------------------------------------------------------")

    #Printing invoice.      
    for input_value in user_quan.keys():           
        if input_value==1:
            file.write(str("\n" +laptop_dictionary[1][0]+"            "+str(int(user_quan[1]))+"               "+laptop_dictionary[1][2]+"                "+str(razer_amount)))
        elif input_value==2:
            file.write(str("\n" +laptop_dictionary[2][0]+"                 "+str(int(user_quan[2]))+"                   "+laptop_dictionary[2][2]+"                 "+str(xps_amount)))
        elif input_value==3:
            file.write(str("\n" +laptop_dictionary[3][0]+"              "+str(int(user_quan[3]))+"                "+laptop_dictionary[3][2]+"               "+str(alien_amount)))
        elif input_value==4:
            file.write(str("\n" +laptop_dictionary[4][0]+"              "+str(int(user_quan[4]))+"                    "+laptop_dictionary[4][2]+"               "+str(swift_amount)))
        elif input_value==5:
            file.write(str("\n" +laptop_dictionary[5][0]+"        "+str(int(user_quan[5]))+"                 "+laptop_dictionary[5][2]+"                 "+str(mac_amount)))
    file.write("\n\n---------------------------------------------------------------------")
    file.write("\n\t\t\t    Final Amount with 13% VAT : "+str(int(total_amount)))   
    file.write("\n\n---------------------------------------------------------------------")
    file.write("\n\t\t            "+str(disc)+"% Discounted Amount : "+str(int(discount)))
    file.write("\n---------------------------------------------------------------------")
    file.write("\n\t\t\t             Grand Total : $"+str(int(grand_total)))
    file.write("\n=====================================================================")
    file.close()

    print("\n")
    print("--------------------------------------------------------------------------------")
    print("Print INVOICE:")
    file=open(uniq+"-sell"+nam+".txt","r")
    print(file.read())
    file.close()
    return laptop_dictionary
