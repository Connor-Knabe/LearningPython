def missing_char(str, n):
  
    firstStr = ""
    lastStr = ""

    if (n==0):
        return str[n+1:]
    elif (n==len(str)-1):
        return str[0:len(str)-1]
    else:
		firstStr = str[0:n]
		lastStr = str[n+1:len(str)]
	return firstStr + lastStr



