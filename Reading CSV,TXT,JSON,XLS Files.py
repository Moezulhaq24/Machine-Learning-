import pandas as pd
import json

# Make a menu function for the CSV,JSON,TXT and XLS files

def menu():
    print("Press 1 for CSV File")
    print("Press 2 for JSON File")
    print("Press 3 for TXT File")
    print("Press 4 for XLS File")

    return int(input("Enter the number according to the file you want to upload : "))

def loadFiles():
    file = menu()
    path = input(f"Enter the path of the file you want to upload : ")

    if file == 1:
        df = pd.read_csv(path)
    
    elif file == 2:
        with open(path,'r') as jsonFile:
            df = json.load(jsonFile)
    
    elif file == 3:
        with open(path,'r') as txtFile:
            df = file.open()

    elif file == 4:
        df = pd.read_excel(path)

    else:
        return "The file type is not supported."
    
    return df



