#Write a python function which accepts a sentence and returns a list in which first value
#is the count of upper case letters and second value is the count of lower case letters in the sentence. 
#Ignore spaces, numbers and other special characters if any.

#lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    #start writing your code here
    count1 = 0 
    count2 = 0 
    for i in sentence:
        if(i.islower()):
            count1+=1 
        elif(i.isupper()):
            count2+=1 
       
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))
