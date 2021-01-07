from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup(open("G5-d10.svg"), 'xml')

'''
nodes = {}

i = 0
for s in soup.find_all("circle"):
    nodes[i] = {"name":s.get("class")[3:], "x":s.get("cx"), "y":s.get("cy"), "r": s.get("r"), "color":s.get("fill")}
    print(s.get("class")[3:], s.get("cx"), s.get("cy"), s.get("r"), s.get("fill"))
    i+= 1

df = pd.DataFrame.from_dict(nodes, orient='index')
print(df)

df.to_csv("nodes.csv",index=False)
'''

edges = {}

i = 0
for s in soup.find_all("path"):
    params = s.get("d").split(" ")
    print(params)
    names = s.get("class").split(" ")
    mx = params[1].split(",")[0]
    my = params[1].split(",")[1]
    c1x = params[3].split(",")[0]
    c1y = params[3].split(",")[1]
    c2x = params[4].split(",")[0]
    c2y = params[4].split(",")[1]
    c3x = params[5].split(",")[0]
    c3y = params[5].split(",")[1]
    try:
        edges[i] = {"name1":names[0][3:], "name2":names[1][3:], "mx":mx, "my": my, "c1x":c1x, "c1y": c1y, "c2x":c2x, "c2y": c2y,"c3x":c3x, "c3y": c3y, "color":s.get("stroke")}
        i+= 1
    except Exception as e:
        #print(names)
        pass

df = pd.DataFrame.from_dict(edges, orient='index')
print(df)

df.to_csv("edges.csv",index=False)
