import requests
import pandas as pd

url ="https://jsonplaceholder.typicode.com/posts"
reponse = requests.get(url)

if reponse.status_code == 202:
    data = reponse.json()
    df = pd.DataFrame(data)
    print(df.head())

    df.to_csv("./data/api_data.csv",index=False)
    print("Data saved to api_data.csv")

else:
    print(f"failed to fetch api. status code {reponse.status_code}")



