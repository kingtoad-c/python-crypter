print("~ceb encoder~")
print("|===========|")
print("|1.encrypt  |")
print("|2.decrypt  |")
print("|===========|")
option = input("pick one:")

if option == "1":
    import demo_encrypt
    demo_encrypt
elif option == "2":
    import demo_decrypt
    demo_decrypt
