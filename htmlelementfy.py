def htmlelementfy(shorthand):
    #function to convert the given data into a html element
    def elementfy(element, innervalue, attributes):
        x = '<' + str(element)
        
        if attributes[0] == "":
            has_attributes = False
        else:
            has_attributes = True
            x = x + " "
        for c in attributes:
            x = x + str(c)
            if has_attributes and c != attributes[len(attributes)-1]:
                x = x + " "
                
        x = x + ">" + innervalue + "</" + element + ">"
        return x
    
    #split the given string into variables to convert it into a html element
    x = shorthand
    y = x.split("(")
    z = y[-1][:-1]
    y[-1] = z
    data = z.split(" #", 1)   
    element = y[0]
    innervalue = data[0]
    attributes = data[1]
    attributes = attributes.split(" #")

    #return the html element
    return elementfy(element, innervalue, attributes)

#paste above code in your project
