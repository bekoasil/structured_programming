import pandas as pd 

datapath = r"/Users/bekirasil/Desktop/HotPoints.csv"
outpath = r"/Users/bekirasil/Desktop/HotPoints.json"

data = pd.read_csv(datapath)

id = data.id
type = data.type
typeTitle = data.typeTitle
color = data.color
capacity = data.capacity
range = data.range
name = data.name
status = data.status
city = data.city
address = data.address
coordinate = data.koordinat

contianer = { }

x = 0

while x < len(id):

    contianer[id[x]] = [
        {"id: ", id[x],
        "type: ", type[x],
        "typeTitle: ", typeTitle[x],
        "color: ", color[x],
        "capacity: ", capacity[x],
        "range: ", range[x],
        "status: ", status[x],
        "city: ", city[x],
        "address: ", address[x],
        "coordinate: ", coordinate[x]
        }
        ]
    x = x + 1

df = pd.DataFrame(contianer)
df.to_json(outpath, indent=4)

