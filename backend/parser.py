import urllib.request, json
with urllib.request.urlopen("https://declarator.org/api/v1/search/sections/?person=63") as url:
    data = json.loads(url.read().decode())
    print(list(data)))
