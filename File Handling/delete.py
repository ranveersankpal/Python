import os
filename = input("Enter Your File Name : ")

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} Removed Successfully")
else:
    print("File Does not Exist")