# program to get anagrams of a palindrome

def reverse_strings_list(string_list):
    result = list(filter(lambda x: (x == "".join(reversed(x))), string_list))
    return result


original_list = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
print(original_list)
print(reverse_strings_list(original_list))

