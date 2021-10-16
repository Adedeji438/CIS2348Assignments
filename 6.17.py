#Adedeji Akingbola
#psid:1793979

inp = input()
password = ""

for alpha in inp:
    if alpha == 'i':
        password += "!"
    elif alpha == 'a':
        password += "@"
    elif alpha == 'm':
        password += 'M'
    elif alpha == 'B':
        password += '8'
    elif alpha == 'o':
        password += '.'
    else:
        password += alpha

password += "q*s"

print(password)