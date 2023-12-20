import pandas as pd

data = pd.read_csv('Negara.csv', index_col=0)
df = pd.DataFrame(data)
print("Berikut Dataframe nya: ")
print(df)

mean = df.groupby(['Benua']).mean(numeric_only=True)
df.to_csv("NegaraMean.csv")
print("Berikut Mean Benua nya: ")
print(mean)

deviasi = df.groupby(['Benua']).std(numeric_only=True)
df.to_csv("NegaraStandarDeviasi.csv")
print("Berikut Standard Devisasi nya: ")
print(deviasi)

print("File Berhasil Dibuat")