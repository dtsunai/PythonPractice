#Please make a list of 5 "lastName_firstName.pdf" values
""" Display data type of unique variables, file extension, first name,
    last name, first name last name, (last name, first name), length of file name """
#Check if all file names contain an "_"

def myfunc():
    list_of_files = ["Anderson_Kevin.pdf", "Williams_Samantha.pdf", "Matthews_Jane.pdf", "Dean_Andrew.pdf", "Laris_Cody.pdf"]
    kander, swilli, jmatth, adean, claris = list_of_files
    
    print(type(list_of_files))
    print(type(list_of_files[0]))
    print(list_of_files[0][-4:])
    print()
    
    for x in list_of_files:
        y = len(x)
        
        print(x)
        print("Length of name, excluding extension:",(y - 4))
        print()
    
    for x in list_of_files:
        print(x)
        
        if "_" in x:
            print("The above file is correct")
            print()
    
    print()
    print("File Name Without Extension")
    print("---------------------------------")   
    for x in list_of_files:
        y = x[:-4]
        print(y)
       
    print()
    print("Last Name, First Name")
    print("--------------------------")           
    for x in list_of_files:
        y = x[:-4]
        if "_" in y:
            z = y.replace("_", ", ")
            print(z)

    print()
    print("Last Name")
    print("------------")
    for x in list_of_files:
        y = x[:-4]
        z = y.find("_")
        
        print(y[:z])
        
    print()
    print("First Name")
    print("------------")
    for x in list_of_files:
        y = x[:-4]
        z = y.find("_") + 1
        print(y[z:])
    
    print()
    print("Full Name")
    print("------------")
    for x in list_of_files:
        y = x[:-4]
        z = y.find("_")
        w = z + 1
        
        print(y[w:], y[:z])
     
myfunc()