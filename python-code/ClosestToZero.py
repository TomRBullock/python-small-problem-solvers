

def closestToZero(numArray):

    #checks for empty array
    if (len(numArray) >= 1):

        #initalise variable names
        negNew = False
        current = 0
        lowest = convertPos(numArray[0])[0]
        neg = convertPos(numArray[0])[1]

        
        for i in range (1, len(numArray), 1):     #traverse through array

            current = convertPos(numArray[i])[0]
            negNew = convertPos(numArray[i])[1]
            
            #checks current value to lowest value so far
            if (current < lowest):
                
                
                neg = negNew        #sets neg to true/false depending on if it was a negative number
                lowest = current    #chages lowest to highest,

            #makes sure the possitive value is prefered 
            elif ((current == lowest) and (negNew == False)):
                
                lowest = current    #chages lowest to highest,
                neg = negNew        #sets neg to true/false depending on if it was a negative number


        #if the lowest value was a negative number then converts back to negative        
        if (neg == True):
            lowest = lowest * -1

        print(lowest, " Is closest to 0")
    #empty array passed
    else:
        print("Empty array passed")


        
def convertPos(num):
    #declare array
    returnArr = [None]*2
    
    #checks for negative numbers
    if(num < 0):
        #converts to positive
        current = num * -1
        negNew = True
        
    else:
        #assigns when possitive
        current = num
        negNew = False
        
    #assign values to be sent back
    returnArr[0] = current
    returnArr[1] = negNew
    
    return returnArr


temp = [-1.7, 1.7, 7]
closestToZero(temp)
