import requests
import json # to convert a data to json or vice versa

#GET
"""user_input = input("enter id : ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}" #/2 ,/3


get_response = requests.get(get_url)
print(get_response.json())"""

#POST
to_do_item = { #we won`t add an id for an item (outo incremenet)
    "UserId" : 2,
    "title" : "my to do",
    "completed" : False,
}
post_url = "https://jsonplaceholder.typicode.com/todos"
#optional header
headers = {
    "Content-Type": "application/json",

}
#post_response = requests.post(post_url,json = to_do_item,headers=headers)
post_response = requests.post(post_url,data = json.dumps(to_do_item),headers=headers)
print(post_response.json())
#print(json.dumps(to_do_item))



