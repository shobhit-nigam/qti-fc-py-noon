import pandas as pd

dfa = pd.read_csv("csv_1.csv", encoding="ISO-8859-1")
print(list(dfa.columns))

print(dfa)
