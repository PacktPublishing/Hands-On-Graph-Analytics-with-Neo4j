import requests
from pprint import pprint


query = """
query($name:String) {
    User(name: $name) { 
        name 
    }
}
"""

data = {
    "query": query,
    "variables": {
        "name": "my_name"
        }
}


r = requests.post(
    "http://localhost:4001/graphql",
    json=data,
    headers={
    }
)

print(r)
pprint(r.json())
