s=input("enter a string:")
print(s)
char=s[0]
s=s.replace(char,'$')
s='$'+s[1:]
print(s)
