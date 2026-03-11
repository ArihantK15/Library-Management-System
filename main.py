import csv
import pandas as pd

df = pd.read_csv("books_cleaned.csv", sep=';', on_bad_lines='skip', dtype={"ISBN": str})
df["ISBN"] = df["ISBN"].astype(str).str.strip() # We read the CSV File "books_cleaned" using Pandas.


def menu():
    print("What Would You Like To Do?..")
    print()
    print(" 1. Search For A Book")
    print(" 2. Borrow A Book")
    print(" 3. Return A Book")
    print(" 4. LogOut")
    print()

    try:
        op = int(input("Enter Your Option: ")) # We will use match case here to match options and the expected results with a default case.
    except:
        print("Invalid Input")
        menu()
        return

    match op:
        case 1:
            find = input("Enter The Book You Want To Find: ").strip() # We use the book name and "contain string" to find all the possible data that contains our search to print.
            filtered_sr = df[df["Book-Title"].str.contains(find, case=False, na=False)]

            if not filtered_sr.empty:
                print("\n--- Search Results ---")
                print(filtered_sr[["ISBN","Book-Title", "Book-Author"]].to_string(index=False))
            else:
                print()
                print()
                print()
                print(f"No books found matching '{find}'.") # We handle the chance of the book not being available
            print()
            print()
            print()
            menu()

        case 2:
            bor = input("Enter The Book ISBN (refer to book search) You Want To Borrow: ").strip()

            try:
                bw = pd.read_csv("borrow.csv", dtype={"ISBN": str})

            except:
                bw = pd.DataFrame(columns=["ISBN","Name","Days"])

            bw["ISBN"] = bw["ISBN"].str.strip()

            check = bw[bw["ISBN"] == bor] # We run this code so pandas can read the borrow csv to handle any chances that the user inputs an already borrowed book and prevents it.
            filtered_br = df[df["ISBN"] == bor] # runs the check to see if the ISBN is in books_cleaned.

            if check.empty:
                if not filtered_br.empty:
                    name = input("Enter The Borrower's Name: ").strip()

                    allowed_days = input("Enter allowed days for borrowing: ").strip() #Ask for the allowed duration

                    new = [bor, name, allowed_days] # Save all three to CSV
                    with open('borrow.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(new)
                        print("Information Saved")
                    menu()
                else:
                    print("ISBN not found please check again") # Handling the chance of the book not being found.
                    print()
                    print()
                    menu()
            else:
                print("The Book Is Already Borrowed.") # Handling the chance of the book being borrowed.
                print()
                print()
                menu()

        case 3:
            isbn = input("Enter The ISBN of The Book: ").strip()

            try:
                bw = pd.read_csv("borrow.csv", dtype={"ISBN": str})
            except:
                print("No borrowed books record found")
                menu()
                return

            bw["ISBN"] = bw["ISBN"].str.strip()

            fetched_re = bw[bw["ISBN"] == isbn] # we check if the ISBN is in the borrow.csv

            if not fetched_re.empty: # If yes we approve and remove the old borrow data.
                allowed = int(fetched_re.iloc[0]["Days"])
                actual = int(input("Enter the actual number of days kept: "))

                if actual > allowed:
                    days_over = actual - allowed
                    fine = days_over * 10
                    print(f"Book is late! Extra days: {days_over}. Total Fine: {fine}")
                else:
                    print("Returned on time. No fine.")

                bw = bw[bw["ISBN"] != isbn]
                bw.to_csv("borrow.csv", index=False)

                print("Book Returned and Record Updated.")
                menu()

            else:
                print("Book not found") # handling the issue if there is no book or wrong input
                menu()

        case 4:
            print("Thank You for Using Library Management Interface") # Simple Ending to mimic logging out.
            exit(0)

        case _:
            print("Invalid Input")
            menu()


def welcome():
    print("=================== Welcome to Library Management Interface ===================")
    print()
    menu()


def login():
    print("Hi User, Please Login To Proceed")

    while True:
        u = input("Enter Your Username: ").strip() # Simple Username and Password Input
        p = input("Enter Your Password: ").strip()

        login = False

        with open('cred.csv', mode='r') as file: # Checking the Cred.csv file for the decided credentials, can be changed for a stronger password.
            reader = csv.reader(file)

            for row in reader:
                if u.strip() == row[0].strip() and p.strip() == row[1].strip(): # Checking for Match
                    login = True
                    print(f"Welcome {row[0]}")
                    welcome()
                    break

        if login:
            break
        else:
            print("Incorrect Credentials, Try Again") # Handling the chance of wrong credentials.


login()