with open("sample.txt","r")as file:
    file.seek(5)  #Skip the initial 5 characters
    print(file.read())