#Please make a list of 5 "lastName_firstName.pdf" values
""" Display data type of unique variables, file extension, first name,
    last name, first name last name, (last name, first name), length of file name """
#Check if all file names contain an "_"
    
    # >>> fnp = file name pure (without extension)

list_of_files = ["Anderson_Kevin.pdf", "Williams_Samantha.pdf", "Matthews_Jane.pdf", "Dean_Andrew.pdf", "Laris_Cody.pdf"]
kander, swilli, jmatth, adean, claris = list_of_files
    
underSymbol = "_"
dotSymbol = "."
commaSymbol = ","
space = " "


#finding length of file name
def findLength(x):
    fn_length = len(x)
    dotPosition = x.find(dotSymbol)
    fnp_length = len(x[:dotPosition])  
    fnp = x[:fnp_length]

    print(x)
    print("Length of name, excluding extension:",fnp_length)
    print()

#checking format if _ is present   
def checkFormat(x):
    print(x)
        
    if underSymbol in x:
        print("The above file is correct")
        print()
        
#cleaning file name to exclude extension    
def makePure(x):
        dotPosition = x.find(dotSymbol)
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        print(fnp) 

#giving lastName, firstName
def giveLastFirstName(x):
        dotPosition = x.find(dotSymbol)
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        if underSymbol in fnp:
            lastFirstName = fnp.replace(underSymbol, commaSymbol + space)
            print(lastFirstName)

#giving last name from file name
def giveLastName(x):
        dotPosition = x.find(dotSymbol)
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        underPosition = fnp.find(underSymbol)     
        lastName = fnp[:underPosition]
        
        print(lastName)

#giving first name from file name        
def giveFirstName(x):
        dotPosition = x.find(dotSymbol)
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        underPosition = fnp.find(underSymbol)
        firstName = fnp[underPosition + 1:]
        
        print(firstName)
        
def giveFullName(x):
        dotPosition = x.find(dotSymbol)
        fnp_length = len(x[:dotPosition])  
        fnp = x[:fnp_length]
        
        underPosition = fnp.find(underSymbol)     
        lastName = fnp[:underPosition]
        
        underPosition = fnp.find(underSymbol)
        firstName = fnp[underPosition + 1:]
        
        fullName = firstName + space + lastName
        print(fullName)
        
def myfunc():
    
    print(type(list_of_files))
    print(type(list_of_files[0]))
    
    dotPosition = list_of_files[0].find(dotSymbol)
    print(list_of_files[0][dotPosition:])
    print()
    
    #displaying length of file name
    for x in list_of_files:
        findLength(x)
    
    #displaying if format is correct
    for x in list_of_files:
        checkFormat(x)
    
    #displaying file name without extension
    print()
    print("File Name Without Extension")
    print("---------------------------------")   
    for x in list_of_files:
        makePure(x)
        
    #displaying last name, first name
    print()
    print("Last Name, First Name")
    print("--------------------------")           
    for x in list_of_files:
        giveLastFirstName(x)
    
    #displaying last name only
    print()
    print("Last Name")
    print("------------")
    for x in list_of_files:
        giveLastName(x)
    
    #displaying first name only
    print()
    print("First Name")
    print("------------")
    for x in list_of_files:
        giveFirstName(x)
    
    #displaying first name last name
    print()
    print("Full Name")
    print("------------")
    for x in list_of_files:
        giveFullName(x)
     
myfunc()
