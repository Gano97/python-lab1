strng= input("Inserire stringa:")
str2=""
if len(strng)<2:
    strng=""
else:
    i=0
    for car in strng:
        if(i==0 or i==1 or i==len(strng)-2 or i==len(strng)-1):
            str2+= car
        i+=1

print("Stringa risultato:" + str2)