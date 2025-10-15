s=input("enter the string:")
vowels='aeiouAEIOU'
vowel_list=[]
for i in range(len(s)):
    if(s[i] in vowels):
    
       vowel_list.append(s[i])
print(vowel_list)       
