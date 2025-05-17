import os

print("~ceb encoder~")
print("|===========|")
print("|1.encrypt  |")
print("|2.decrypt  |")
print("|===========|")
option = input("pick one:")

os.system("cls")

if option == "1":
    print("~ceb encoder~")
    print("|===========|")
    print("|1.text     |")
    print("|2.file     |")
    print("|===========|")
    option = input("pick one:")
    if option == "1":
        import demo_encrypt
        demo_encrypt
    elif option == "2":
        import file_encrypt
        file_encrypt

elif option == "2":
    print("~ceb encoder~")
    print("|===========|")
    print("|1.text     |")
    print("|2.file     |")
    print("|===========|")
    option = input("pick one:")
    if option == "1":
        import demo_decrypt
        demo_decrypt
    elif option == "2":
        import file_decrypt
        file_decrypt