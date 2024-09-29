import pandas as pd

df = pd.read_csv("Dokumanlar/18-Pandas/datasets/youtube-ing.csv")

result = df.head(10)
result = df[5:20].head(5)

result = df.head(50)[["title", "likes", "dislikes"]]

print (result)

