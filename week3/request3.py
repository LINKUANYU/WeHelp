import urllib.request as req
import json
url1 = "https://cwpeng.github.io/test/assignment-3-1"
url2 = "https://cwpeng.github.io/test/assignment-3-2"
with req.urlopen(url1) as response:
    data1_raw = response.read().decode("utf-8")
data = json.loads(data1_raw)
print(len(data["rows"]))