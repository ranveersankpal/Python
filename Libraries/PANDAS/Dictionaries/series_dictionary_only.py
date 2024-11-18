import pandas as pd

a = {"day1" : "Sunday", "day2" : "Monday", "day3" : "Tuesday"}

myvar = pd.Series(a, index = ["day1","day3"])
print(myvar)