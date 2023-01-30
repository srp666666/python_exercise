# program to get sorted list of strings

def sort_numeric_strings(list_strings):
    result = sorted(list_strings, key=lambda el: str(el))
    return result


original_list = ["python", "java", "c++"]
print(original_list)
print(sort_numeric_strings(original_list))
