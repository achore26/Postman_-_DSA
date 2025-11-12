import requests
import json

'''
For Postman:
1.Create a Postman collection with 3–4 endpoints (GET + POST).
2.Export the collection and share the link.
3.Write a short script (Python or JS) that fetches API data and prints filtered results.
Deliverable: Postman collection + GitHub repo with code.
Submit this to myself and cc trudeau@zynamis.co.ke
'''
def get_data_from_api(url):
    req = requests.get(url)
    data = req.json()
    return data

def filter_data(data, filter_key, filter_value ):
    for item in data:
        if filter_key == "id" and item.get("id") == filter_value:
            print(item.get("title"))
        elif filter_key == "title" and item.get("title") == filter_value:
            print(item.get("titile"))



example = get_data_from_api("https://my-json-server.typicode.com/typicode/demo/posts")
filter_data( example, "id", 1)






