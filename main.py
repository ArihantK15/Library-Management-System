import csv
import pandas as pd
df = pd.read_csv("books_cleaned.csv", sep=';',on_bad_lines='skip')

def menu():
    print("What Would You Like To Do?..")
    print()
    print(" 1. Search For A Book")
    print(" 2. See The Current Books Borrowed")
    print(" 3. Borrow A Book")
    print(" 4. Return A Book")
    print(" 5. Change Login")
    print()
    op = int(input("Enter Your Option: "))
    match op:
        case 1:
            find = input("Enter The Book You Want To Find: ")
            filtered_df = df[df["Book-Title"].str.contains(find, case=False, na=False)]

            if not filtered_df.empty:
                print("\n--- Search Results ---")
                print(filtered_df[["Book-Title", "Book-Author"]].to_string(index=False))
            else:
                print()
                print()
                print()
                print(f"No books found matching '{find}'.")
        
            print()
            print()
            print()
            menu()
        
        case 2:

            pass





def welcome():
    print("===================Welcome to Library Management Interface===================")
    print()
    menu()


def login():
    print("Hi User, Please Login To Proceed")

    while True:
        u = input("Enter Your Username: ")
        p = input("Enter Your Password: ")

        login = False

        with open('cred.csv', mode='r') as file:
            reader = csv.reader(file)

            for row in reader:
                if u.strip() == row[0].strip() and p.strip() == row[1].strip():
                    login = True
                    print(f"Welcome {row[0]}")
                    welcome()
                    break

        if login:
            break
        else:
            print("Incorrect Credentials, Try Again")


login()