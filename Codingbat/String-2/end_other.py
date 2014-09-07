def end_other(a, b):
  
    a = a.lower()
    b = b.lower()  
    theLen = 0

    if len(a) > len(b):
        theLen = len(a) - len(b)

        for i in range(len(a)):
    	    if a[i:i+len(b)] == b and i >= theLen:
    		return True

    else:
        theLen = len(b) - len(a)

        for i in range(len(b)):
    	    if b[i:i+len(a)] == a and i >= theLen:
    		return True
    return False