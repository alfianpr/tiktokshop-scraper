import requests
import pandas as pd

df = pd.read_csv("manswear.csv")
df = df["link"].values.tolist()

result = []
session = requests.Session()  # so connections are recycled

print ("Unshorted the link ...")
url = []
for i in df:
    resp = session.head(i, allow_redirects=True)
    long = resp.url
    long_final = long.split("?")
    url.append(long_final[0])
    print(long_final[0])

print ("remove duplicate ...")
[result.append(x) for x in url if x not in result]
df_result = pd.DataFrame(result)
df_result.to_csv("mens_clean.csv")
print(df_result)