def write_(lap):
    laptop_dictionary=lap
    file = open("laptop.txt","w")
    for values in laptop_dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()
    
