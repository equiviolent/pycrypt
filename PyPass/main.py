import os.path
import sys
from crypt import *

## Core logic

def appendPass():
    file = open("pass.txt", 'a')

    print("Welcome to the PyPass version: 1.0.0")

    userName = input("Enter your name: ")
    password = input("Enter your pass: ")
    shift = input("Enter your shift: ")
    app = input("Enter the name of the app: ")

    usrnm = "UserName: " + userName + "\n"
    pwd = "Pass: " + encryption(password, int(shift)) + "\n"
    web = "Website: " + app + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def readPasswords():
    #TODO: decrypt the password
    file = open('pass.txt', 'r')
    content = file.read()
    file.close()
    print(content)

def usage():
    print("\n\tUsage: python3 main.py OPTION")
    print("\tOptions:")
    print("\t\tenc\n\t\tdec")
    exit()

if not (len(sys.argv) == 2):
    usage()

arg = sys.argv[1]

if (arg == "enc"):
    appendPass()
elif (arg == "dec"):
    readPasswords()
else:
    usage()

