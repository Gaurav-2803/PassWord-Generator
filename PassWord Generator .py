import string 
import random 

print("\n\n\t\t\t\tPASSWORD GENRATOR\n\n")
a = string.ascii_uppercase
b = string.ascii_lowercase
c = string.digits
d = string.punctuation 
p = input("\n\nEnter passord Length : ") 

try :
    p = int(p)
except ValueError as n :
    print("Your input is invalid")
s = []
s.extend(list(a))
s.extend(list(b))
s.extend(list(c))
s.extend(list(d))
random.shuffle(s)
x = "".join(s[0:p])
print("\nYour Genrated Password : " , x)
print("\n\n")

