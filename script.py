import requests
import json

'''
For Postman:
1.Create a Postman collection with 3–4 endpoints (GET + POST).
2.Export the collection and share the link.
3.Write a short script (Python or JS) that fetches API data and prints filtered results.
'''
def get_data_from_api(url):
    req = requests.get(url)
    data = req.json()
    return data

def filter_data(data, filter_key, filter_value ):
    # for item in data:
    #     if filter_key == "id" and item.get("id") == filter_value:
    #         print(item)
    #     elif filter_key == "title" and item.get("title") == filter_value:
    #         print(item)

    for item in data:
        if str(item.get(filter_key)) == filter_value:
            print(item)

def get_attributes_of_data (data):
        keys = list(data[0].keys())
        print(f'The following are the available attributes you can choose to filter {keys}:')
        return keys



# info = get_data_from_api("https://my-json-server.typicode.com/typicode/demo/posts")
# filter_data(info, "id", 1)


print("Hi There, Wanna get some data and filter it? \n\n Cool Lets get you started")
input_url = input("Please enter your input url: ")
get_attributes_of_data(get_data_from_api(input_url))
filter_key = input("Please enter your input the attribute you wish to filter by from the above list: ")
filter_val = input("Please enter the value that you want to filter by: ")
filter_data(get_data_from_api(input_url), filter_key, filter_val)

# example = get_data_from_api("https://my-json-server.typicode.com/typicode/demo/posts")
# filter_data( example, "id", 3)






