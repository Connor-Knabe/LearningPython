is_birthday = True

speed = 60


if speed <= 60:
	print "not speed"
elif speed > 60 and speed <= 80 and not is_birthday:
	print "speed"


if speed <= 60:
	return 0 
elif speed > 60 and speed <= 80:
	return 1
elif speed > 80:
	return 2


