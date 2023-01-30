# program to handles the ValueError exception raised when trying to convert a string to an integer

string = "3"
try:
    string_int = int(string)
    print(string_int)
except ValueError:
    print('Please enter an integer')
