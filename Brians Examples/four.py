#Given that the word ends with b return "buzz"
#Given that the word starts with f return "fizz"
#Given that the word starts with f AND ends with b return "fizzbuzz"
#Else return the orginal word unchanged

#Run with: python test.py four

def fizzbuzz(word):
    #Your code goes here
	f = word.find("f")
	b = word.rfind("b")
	if f == 0 and b == len(word)-1:
		return "fizzbuzz"
	if f == 0:
		return "fizz"
	if b == len(word)-1:
		return "buzz"
	else:
		return word