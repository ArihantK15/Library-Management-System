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
            filtered_sr = df[df["Book-Title"].str.contains(find, case=False, na=False)]

            if not filtered_sr.empty:
                print("\n--- Search Results ---")
                print(filtered_sr[["ISBN","Book-Title", "Book-Author"]].to_string(index=False))
            else:
                print()
                print()
                print()
                print(f"No books found matching '{find}'.")
            print()
            print()
            print()
            menu()
        
        case 3:
            bor = input("Enter The Book ISBN (refer to book search) You Want To Find: ")
            filtered_br = df[df["ISBN"].str.contains(bor, case=False, na=False)]
            check = df[df["ISBN"].str.contains(bor,case=False,na=False)]
            if check.empty:
                if not filtered_br.empty:
                    print(f" Your Book is: ")
                    print()
                    print(filtered_br[["ISBN","Book-Title"]].to_string(index=False))
                    name = input("Enter The Borrower's Name")
                    new = [bor,name]
                    with open('borrow.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(new)
                        print("Information Saved")
                        print()
                        print()
                    menu()
                else:
                    print("ISBN not found please check again")
                    print()
                    print()
                    menu()
            else:
                print("The Book Is Already Borrowed.")
                print()
                print()
                menu()



def welcome():
    print("=================== Welcome to Library Management Interface ===================")
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