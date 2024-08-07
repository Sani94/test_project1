import pandas as pd


file = pd.read_csv("games_dataset.csv")
df = pd.DataFrame(file)


pd.set_option("display.max_rows",None)

df = df.dropna()
df.rename(columns={"Game Name":"Name"}, inplace=True)

df = df[df['Release Year'] > 2014]
df_group = df.groupby("Name")

print(df_group.head(5))


# Name            1838
# Genre           1838
# Platform        1838
# Release Year    1838
# User Rating     1838