import pandas as pd

# Make a menu function for the CSV,JSON,TXT and XLS files

def menu():
    print("Press 1 for CSV File")
    print("Press 2 for JSON File")
    print("Press 3 for TXT File")
    print("Press 4 for XLS File")

    return int(input("Enter the number according to the file you want to upload : "))


