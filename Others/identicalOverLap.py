n = "aabbaa"
n2 = "abbat"
n3 = "abbaattagggaaaatt"
n4 = "aabbaaa"
n5 = "abba"

def solution(s):
    inputLength=len(s)
    ans=[]
    #base case
    if inputLength == 0 :
        return []
    #loop through each char of the param s
    for i in range(1,inputLength):
        
        #substring each char from 0 to i
        sub = s[0:i]
        #reverse the substring
        reverse = sub[::-1]
        
        #cut original string by 1 char each time for comparing with the reversed substring
        newString = s[i:inputLength] 
        
        #print("newS: "+newString)
        #print("Reverse: "+reverse)
        #loop counter for newString
        k=0
        #IS no dissimilar overlap
        isTheSame = False;
        
        #loop through the reversed substring
        for j in range(0,len(reverse)):
            #if overlap with no dissimilar
            if reverse[j]==newString[k]:
                
                isTheSame=True
                
                #print("k: "+str(k)) 
                #prevent index out of range by breaking out of the loop
                if len(newString) <=1:
                    break
                k+=1
            else:
                #if not overlap with no dissimilar
                isTheSame =False
                k=0
                break
        
        #append the folding index to answer list
        if isTheSame == True:
           ans.append(i)
                    
    return ans
               
print(n)
print(solution(n))
print(n2)
print(solution(n2))
print(n3)
print(solution(n3))
print(n4)
print(solution(n4))
        
        