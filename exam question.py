import pandas as pd
d = pd.DataFrame({"name": ["Asha", "Ravi", "Asha", "Meena", None], "city": ["Pune", "Agra", "Pune", "Delhi", "Pune"], "score": [70, None, 70, 85, 60]})

#task 1
print(d.shape, d["name"].isna().sum(), d["score"].isna().sum())

#task 2
d["score"] = d["score"].fillna(d["score"].mean())
print(d["score"].mean())
print(d["city"].value_counts()["Pune"])

#task 3
d = d.dropna(subset=["name"])
print(d.shape)

d = d.drop_duplicates()
print(d.shape, d["city"].value_counts()["Pune"])

#task 4
d = d.sort_values(by="score", ascending=False)
print(d.iloc[0]["name"], d.iloc[0]["score"], d.iloc[2]["name"])