import requests
import pandas as pd

CATEGORY = "Avoskin"

df = pd.read_csv(f"./csv/{CATEGORY}.csv", header=None)
df = df[0]

number_lines = sum(1 for row in df)

rowsize = 10

for i in range(1, number_lines, rowsize):
    df_2 = pd.read_csv(f"./csv/{CATEGORY}.csv", header=None, nrows = rowsize, skiprows = i)
    session = requests.Session()
    print ("Unshorted the link ...")

    result = []
    url = []
    for j in df_2[0]:
        try:
            resp = session.head(j, allow_redirects=True)
            long = resp.url
            long_final = long.split("?")
            url.append(long_final[0])
            print(long_final[0])
        except:
            pass

    [result.append(x) for x in url if x not in result]
    df_result = pd.DataFrame(result)
    df_result.to_csv(f"./csv/{CATEGORY}_tmp.csv", mode='a', index=False, header=False)
    print(df_result)

print ("remove duplicate ...")
url_2 = pd.read_csv(f"./csv/{CATEGORY}_tmp.csv", header=None)
url_2 = url_2[0].values.tolist()
result_2 = []

[result_2.append(x) for x in url_2 if x not in result_2]
df_result_2 = pd.DataFrame(result_2)
df_result_2.to_csv(f"./csv/{CATEGORY}_clean.csv", mode='a', index=False, header=False)
print(df_result_2)