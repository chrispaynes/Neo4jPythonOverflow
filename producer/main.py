import requests

apiUrl = "https://api.stackexchange.com/2.2/questions?pagesize=100&order=desc&sort=creation&tagged=neo4j&site=stackoverflow&filter=!5-i6Zw8Y)4W7vpy91PMYsKM-k9yzEsSC1_Uxlf"

json = requests.get(apiUrl, headers = {"accept":"application/json"}).json()

print(json)
