import pandas as pd

#open and transform to dataframe
file = pd.read_csv("games_dataset.csv")
df = pd.DataFrame(file)

#load all columns and rows
pd.set_option("display.max_rows",None)


#delete all rows, where value equals None
df = df.dropna()

#change colmn name 
df.rename(columns={"Game Name":"Name"}, inplace=True)

#filt year
df = df[df['Release Year'] > 2014]

df.sort_values(by='Name',inplace=True)

print(df)

#print(df['User Rating'].mean())
# print(df.groupby(["Platform"]).mean())
# print(df['Platform'])
