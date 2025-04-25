import pandas as rk
file=rk.read_csv('rishu.csv')
file2=rk.read_csv('rishu1.csv')
diff=file.compare(file2)
print (diff)