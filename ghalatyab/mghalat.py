def ghalat(s):
    v = "aeiouy"
    l = "!#$%^&*<>,.?:;"
    #stringOfFile =f.read()
    #listOfFile = stringOfFile.split()
    for i in s :
        x=0
        
            
            
        for j in i :
            if j == j.capitalize() and j not in l :
                x=0    
            
            
            if j in v :
                
                x=0
            
            
            x=x+1
        if  x>=5:
            print(f"{i} \n ")
                
 