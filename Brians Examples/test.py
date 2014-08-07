import sys
import os

file_name = sys.argv[1]
split_name = os.path.splitext(file_name)
file_name_minus_ext = split_name[0]

try:
    module_to_test = __import__(file_name_minus_ext)
except ImportError:
    print('Dammit Connor, that file doesn\'t exist.')

if file_name == "example":
    sol = "It Worked!"
    answer = module_to_test.example()
    if sol == answer:
        print("Everything worked correctly.")
    else:
        print("Something went amiss.")
elif file_name == "one":
    test_arr = [1, 2, 3, 4, 5]
    sol_arr = [2, 4, 6, 8, 10]
    arr = module_to_test.times2(test_arr)
    if sol_arr == arr:
        print("Correct: \n That was an easy one. Don't get cocky.")
    else:
        print("Wrong: \n You're a fucking idiot.")
elif file_name == "two":
    test_arr = [1, 2, 3, 4, 5]
    sol_arr = [5, 4, 3, 2, 1]
    arr = module_to_test.reverse(test_arr)
    if sol_arr == arr:
        print("Correct: \n A little tougher but I'm still not impressed.")
    else:
        print("Wrong: \n You're a fucking idiot.")
elif file_name == "three":
    test_arr = [3, 2, 5, 4, 1]
    sol_arr = [1, 2, 3, 4, 5]
    arr = module_to_test.sort(test_arr)
    if arr == sol_arr:
        print("Correct: \n Congratulations! You can't sort something! #sarcasm")
    else:
        print("Wrong: \n You're a fucking idiot.")
elif file_name == "four":
    test_str1 = "fib"
    test_str2 = "lab"
    test_str3 = "first"
    test_str4 = "nope"
    arr = []
    sol_arr = ["fizzbuzz", "buzz", "fizz", "nope"]
    arr.append(module_to_test.fizzbuzz(test_str1))
    arr.append(module_to_test.fizzbuzz(test_str2))
    arr.append(module_to_test.fizzbuzz(test_str3))
    arr.append(module_to_test.fizzbuzz(test_str4))
    if arr == sol_arr:
        print("Correct: \n Good job. I had to throw that one in there.")
    else:
        print("Wrong: \n You're a fucking idiot.")
elif file_name == "five":
    file_to_test = open("five.py", 'r')
    contents = file_to_test.read()
    if contents.count("for") > 1 or contents.count("while") > 1:
        print("Wrong: \n What part of 'no loops' didn't you understand?")
        exit()
    test_arr = [1, 2, 3, 4, 5]
    sol_arr = [2, 4, 6, 8, 10]
    arr = module_to_test.times2(test_arr)
    if sol_arr == arr:
        print("Correct: \n Wow. Didn't expect you to get that one.")
    else:
        print(arr)
        print("Wrong: \n You're a fucking idiot.")
