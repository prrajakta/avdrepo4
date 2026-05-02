import pandas as pd 

print("extract data")

data = {
    'ID' : [101, 102, 1023],
    'Name' : ['Ram', 'Shyam', 'Raju'],
    'Age' : [29, 30, 24]
}

#to print in tabular format
df = pd.DataFrame(data)
print(df)