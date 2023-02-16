import requests
import pandas as pd

CATEGORY = "Muslim fashion"

df = pd.read_csv(f"{CATEGORY}.csv", header=None)
df = df[0]

number_lines = sum(1 for row in df)

rowsize = 10

for i in range(1, number_lines, rowsize):
    df_2 = pd.read_csv(f"{CATEGORY}.csv", header=None, nrows = rowsize, skiprows = i)
    session = requests.Session()
    print ("Unshorted the link ...")


    result = []
    url = []
    for j in df_2[0]:
        resp = session.head(j, allow_redirects=True)
        long = resp.url
        long_final = long.split("?")
        url.append(long_final[0])
        print(long_final[0])

    print ("remove duplicate ...")
    [result.append(x) for x in url if x not in result]
    df_result = pd.DataFrame(result)
    df_result.to_csv(f"{CATEGORY}_tmp.csv", mode='a', index=False, header=False)
    print(df_result)


df_3 = pd.read_csv(f"{CATEGORY}_tmp.csv", header=None)

df_3.head()