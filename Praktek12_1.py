import pandas as pd

data = pd.read_csv('Negara.csv', index_col=0)
df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean(numeric_only=True)
deviasi = df.groupby(['Benua']).std(numeric_only=True)

print("Berikut Dataframe nya: ")
print(df)

print("Berikut Mean Benua nya: ")
print(mean)

print("Berikut Standard Devisasi nya: ")
print(deviasi)