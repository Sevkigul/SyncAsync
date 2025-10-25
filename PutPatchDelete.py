import requests
import json # to convert a data to json or vice versa


get_url = "https://jsonplaceholder.typicode.com/todos/15"

#get_response = requests.get(get_url)
#print(get_response.json())

#PUT
#General usage : Change all of the items for any id.Ex: Change íd:15 items.
to_do_item_15 = {
    "userId" : 2,
    "title" : "put title",
    "completed" : False,
}
#put_response = requests.put(get_url, json=to_do_item_15)
#print(put_response.json())
#actually it acts like items has changed the items but in reality items do not change.

#PATCH
#General usage : Change on of the item for any id.Ex: Change íd:15 items.
to_do_item_patch_15 = {
    "title" : "Patch Test",
}
#patch_response = requests.patch(get_url, json=to_do_item_patch_15)
#print(patch_response.json())
#title altered

#DELETE
delete_response = requests.delete(get_url)
print(delete_response.status_code)
print(delete_response.json())


