string1 = "abc"
string2 = "abc"

sub1 = ""
sub2 = ""

for i in range (len(string1)):
	sub1 = string1[i:i+2]
	sub2 = string2[i:i+2]

	if sub1 == sub2 and len(sub1) > 1 and len(sub2) > 1:
		print "STRING 1",string1[i:i+2]
		print "YE"