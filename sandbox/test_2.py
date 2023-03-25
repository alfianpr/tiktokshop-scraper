import pandas as pd

df = [{'x': 120, 'y': 948}, {'x': 647, 'y': 948}, {'x': 120, 'y': 1736}, {'x': 647, 'y': 1770}]

df_2 = []
for i in df:
    df_2.append([i["x"], i["y"]])

print(df_2)