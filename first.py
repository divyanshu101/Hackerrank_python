line=input ( "Enter a line:") 
lowercount = uppercount = 0 
digitcount = alphacount = 0 
for b in line: 
   if b.islower(): 
       lowercount += 1 
   elif b.isupper(): 
           uppercount += 1 
   elif b.isdigit (): 
               digitcount +=1 
   if b.isalpha () : 
                   alphacount += 1 
print ("Number of uppercase letters:", uppercount) 
print ("Number of lowercase letters: ", lowercount) 
print ("Number of  alphabets: ", alphacount) 
print ("Number of digits: ", digitcount)
