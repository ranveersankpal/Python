with open("sample.txt", "r+") as f:
    content = f.read()
    f.write(" Something more added")
