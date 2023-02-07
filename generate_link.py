import requests
import pandas as pd

CATEGORY = "Beauty"

df = pd.read_csv(f"{CATEGORY}.csv")
df = df["link"].values.tolist()

result = []
session = requests.Session()

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
df_result.to_csv(f"{CATEGORY}_clean.csv")
print(df_result)