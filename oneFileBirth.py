import pandas as pd
path = "pydata-book-2nd-edition/datasets/babynames/yob1880.txt"
names1880 = pd.read_csv(path,names=['name','sex','birth'])
names_sex = names1880.groupby('sex').birth.sum()
print(names_sex)
