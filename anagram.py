def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    return sorted(str1)==sorted(str2)


s1=input("Enter th first word ")
s2=input("Enter th second word ")

if is_anagram(s1,s2):
    print("this is anagram")
else:
    print("The strings are not anagrams")
