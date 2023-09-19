import sys

import pandas as pd
df=pd.read_csv("list.csv")

def entry(df):
    name=input("Enter Name:")
    phno=int(input("\nEnter Number:"))
    email=input("\nEnter Email")
    address=input("Enter Address")
    if len(str(phno))==10:
        new_data = [
            {'Name': name, 'Number': phno, 'Email': email,'Address':address}
            ]
        df=df.append(new_data,ignore_index=True)
        df.to_csv("list.csv", index=False)
        print("want to make entry again?")
        cmd=int(input("enter 1 for yes\n0 for No"))
        if cmd==1:
            main(df)
        else:
            print("Thanks.. hope you like our service")
    else:
        print("Your Phone number is invalid")
        entry()

def find(df):
    f=input("Enter The Name You want to find")
    try:
        if f in df["Name"].values:
            print(df[df["Name"] == f])
            print("\nDo you want to Find another number")
            cmd = int(input("enter 1 for yes\n0 for No"))
            if cmd == 1:
                find(df)
            else:
                main(df)
    except:
        print("No Contact with name ", f, " Found\nEnter the name Again")
        find(df)

def find1(df):
    p=int(input("Enter The Number You Want To Find"))

    try:
        if p in df["Number"].values:
            print(df[df["Number"]==p])
            print("\nDo you want to Find another number")
            cmd = int(input("enter 1 for yes\n0 for No"))
            if cmd == 1:
                find1(df)
            else:

                main(df)
        else:
            print("Number not found")
            find1(df)
    except:
        print("Number Not found \nEnter again")
        find1(df)

def delete_number(df):
    d=int(input("Enter The Number to be deleted"))

    try:
        if d in df["Number"].values:
            df=df.loc[df['Number'] != d]
            df.to_csv("list.csv", index=False)
            print("\nDo you want to Delete another number")
            cmd = int(input("enter 1 for yes\n0 for No"))
            if cmd == 1:
                delete_number(df)
            else:
                main(df)
        else:
            print("number not found\n Enter Number again")
            delete_number()
    except Exception as e:
        print("Number Not found")
        delete_number(df)

def update_number(df):
    d=input("Enter the name of the person ")

    try:
        if d in df["Name"].values:
            print("Select what you want to update\n"
                  "1 for Number\n"
                  "2 for Address\n"
                  "3 for Email")
            cmd=int(input())

            if  cmd==1:
                n=int(input("Enter New number"))
                df.loc[df['Name'] == d, 'Number'] = n
                df.to_csv("list.csv", index=False)
            elif cmd==2:
                ad=input("Enter New address")
                df.loc[df['Name'] == d, 'Address'] = ad
                df.to_csv("list.csv", index=False)
            elif cmd==3:
                email=input("Enter new Email")
                df.loc[df['Name'] == d, 'Email'] = email
                df.to_csv("list.csv", index=False)
            else:
                print("Enter the correct option")
                update_number()
            print("\nDo you want to Update another number")
            cmd = int(input("enter 1 for yes\n0 for No"))
            if cmd == 1:
                update_number(df)
            else:
                main(df)
        else:
            print("No Contact was found\n Enter Name again")
    except Exception as e:
        print(e)

def main(df):

    print("""Press 1 for number Entry
    Press 2 for finding a number
    Press 3 for finding a number through name
    Press 4 for updating a number details
    Press 5 for Deleting a number
    Press 6 for Exit\n""")
    cmd=int(input("SELECT : "))
    if cmd==1:
        entry(df)
    elif cmd==2:
        find1(df)
    elif cmd==3:
        find(df)
    elif cmd==4:
        update_number(df)
    elif cmd==5:
        delete_number(df)
    elif cmd==6:
        sys.exit(0)
    else:
        print("Select the appropriate option")




print("WELCOME TO CONTACT BOOK")
main(df)