import pandas as pd

a = {
    "name" : ["yash", "panav", "prince"],
    "age" : [23,45,12]
}

myvar = pd.DataFrame(a)
print(myvar)