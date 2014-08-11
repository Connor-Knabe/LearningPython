#Given that the word ends with b return "buzz"
#Given that the word starts with f return "fizz"
#Given that the word starts with f AND ends with b return "fizzbuzz"
#Else return the orginal word unchanged

#Run with: python test.py four

def fizzbuzz(word):
    #Your code goes here
	if word[-1] == "b" and word[0] == "f":
		return "fizzbuzz"
	if word[-1] == "b":
		return "buzz"
	if word[0] == "f":
		return "fizz"
	return word
