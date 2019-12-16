import pandas as pd

#read combined csv
df = pd.read_csv("/home/mpiuser/Downloads/data/combined.csv")
print(df)

#select specific country records
df2 = df.loc[(df['Actor1CountryCode'] == "LKA") & (df['Actor2CountryCode'] == "LKA")]
print(df2)

#write to a new csv
df2.to_csv("/home/mpiuser/Downloads/data/dropCountry.csv", index = False, header=True)


