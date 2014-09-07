a = "AbC"
b = "HiaBc"

a = a.lower()
b = b.lower()
print a

if len(a) > len(b):
    for i in range(len(a)):
    	if a[i:i+len(b)] == b and i < len(a):
    		print "true"

else:
    for i in range(len(b)):
    	if b[i:i+len(a)] == a and i < len(b):
    		print "true"
print "false"