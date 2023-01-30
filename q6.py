# program to read csv and convert to dictionary

from csv import DictReader

# open file in read mode
with open("emp.csv", 'r') as f:
    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)
    print(list_of_dict)
