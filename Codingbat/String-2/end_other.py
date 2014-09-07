a = "Hiabc"
b = "abc"

if len(a) > len(b):
    for i in range(len(a)):
    	if a[i:i+len(b)] == b:
    		return true

else:
    for i in range(len(b)):
    	if b[i:i+len(a)] == a:
    		return true
return false