#Please make a list of 5 "lastName_firstName.pdf" values
""" Display data type of unique variables, file extension, first name,
    last name, first name last name, (last name, first name), length of file name """
#Check if all file names contain an "_"
    
    # >>> fnp = file name pure (without extension)

def myfunc():
    list_of_files = ["Anderson_Kevin.pdf", "Williams_Samantha.pdf", "Matthews_Jane.pdf", "Dean_Andrew.pdf", "Laris_Cody.pdf"]
    kander, swilli, jmatth, adean, claris = list_of_files
    
    underSymbol = "_"
    dotSymbol = "."
    commaSymbol = ","
    space = " "
    
    print(type(list_of_files))
    print(type(list_of_files[0]))
    print(list_of_files[0][-4:])
    print()
    
    #finding length of file name
    for x in list_of_files:
        fn_length = len(x)
        
        print(x)
        print("Length of name, excluding extension:",(fn_length - 4))
        print()
    
    #checking format if _ is present
    for x in list_of_files:
        print(x)
        
        if underSymbol in x:
            print("The above file is correct")
            print()
    
    #displaying file name without extension
    print()
    print("File Name Without Extension")
    print("---------------------------------")   
    for x in list_of_files:
    
        dotPosition = x.find(".")
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        print(fnp)
        
        #fn_name = x[:-4]
        #print(fn_name)
    
    #displaying last name, first name
    print()
    print("Last Name, First Name")
    print("--------------------------")           
    for x in list_of_files:
        
        dotPosition = x.find(".")
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        if underSymbol in fnp:
            lastFirstName = fnp.replace(underSymbol, commaSymbol + space)
            print(lastFirstName)
    
        #y = x[:-4]
        #if "_" in y:
            #z = y.replace("_", ", ")
            #print(z)
    
    #displaying last name only
    print()
    print("Last Name")
    print("------------")
    for x in list_of_files:
    
        dotPosition = x.find(".")
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        underPosition = fnp.find("_")     
        lastName = fnp[:underPosition]
        
        print(lastName)
        
        #y = x[:-4]
        #z = y.find("_")
        
        #print(y[:z])
    
    #displaying first name only
    print()
    print("First Name")
    print("------------")
    for x in list_of_files:
        
        dotPosition = x.find(".")
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        underPosition = fnp.find("_")
        firstName = fnp[underPosition + 1:]
        
        print(firstName)
        
        #y = x[:-4]
        #z = y.find("_") + 1
        
        #print(y[z:])
    
    #displaying first name last name
    print()
    print("Full Name")
    print("------------")
    for x in list_of_files:
        
        dotPosition = x.find(".")
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        underPosition = fnp.find("_")     
        lastName = fnp[:underPosition]
        
        underPosition = fnp.find("_")
        firstName = fnp[underPosition + 1:]
        
        fullName = firstName + space + lastName
        print(fullName)
        
        
        #y = x[:-4]
        #z = y.find("_")
        #w = z + 1
        
        #print(y[w:], y[:z])
     
myfunc()
