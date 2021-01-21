string1 = str(input("Enter A String:"))
string2 = string1

print("String One Is "+string1)
print("String Two Is "+string2)

a = list(string2)
b = len(string2)
z = a[b-1]
a[b-1] = a[0]
a[0]  = z
stra = ""
print("Exchanged String Is: "+stra.join(a))