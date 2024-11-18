a=("One","Two","Three")
b= list(a)
b[1]="Five"
a=tuple(b)
print(a)