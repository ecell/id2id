import requests

tmp = []
for i in requests.get("https://registry.api.identifiers.org/restApi/namespaces?size=9999").json()['_embedded']['namespaces']:
    tmp.append(i['prefix'])
tmp.sort()
f = open("identifiersorg_all_prefix.txt", "a")
for i in tmp:
    f.write(i)
    f.write("\n")
f.close()
