import pandas

mydataset = {
    'cars' : ["bmw", "mercedes", "bentley"],
    'passing' : [2,3,9],
    'price' : [100000,30000000,32784]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)