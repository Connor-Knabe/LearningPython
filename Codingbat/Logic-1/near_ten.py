#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod 

num = 17

mod = num % 10

return (mod <= 2 or mod >= 8)

print num % 10 