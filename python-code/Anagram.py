
def isAnagram(word1, word2):
    
    found = False
    
    word1 = word1.replace(" ","")   #removes spaces
    word2 = word2.replace(" ","")

    word1 = word1.lower()   #makes all letters lower case
    word2 = word2.lower()
    
    if(len(word1) == len(word2)):   #checks letter length
        
        word1 = list(word1)     #converst word to list
        word2 = list(word2)

        for i in range (0, len(word1), 1):  #loops through all of the first word
            
            for j in range (0, len(word2), 1):  #loops through second word until letter is found
                
                if (word1[i] == word2[j]):  #compares letters
                    del word2[j]    #removes letter from second word if matched
                                    #prevents one letter being used more than once
                    found = True
                    break
                
                else:
                    found = False
                    continue
                
            if (found == True):
                continue
    
    #prints if anagram or not
    if (found == False) :
        print("Not an anagram")
    else:
        print("an anagram")
                    

isAnagram("Nick Draper", "Dark Prince")
 
