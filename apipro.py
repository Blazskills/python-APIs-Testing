import urllib2
import json

locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'
def locu_search(query):
    api_key = locu_api
    url ='https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj =urllib2.urlopen(final_url)
    data = json.load (json_obj)
    
    for item in data['objects']:
        print item ['name'], item['phone']











# url ='https://api.locu.com/v1_0/venue/search/?locality=Newport%20Beach&category=restaurant&api_key=9fb8cd70cb34cab8e83690473133f51943b5c93f'
# json_obj = urllib2.urlopen(url)
# data = json.load(json_obj)
# for item in data['objects']:
#     print item ['locality']
#     print item ['phone']
#     print item ['country']
#     print item ['name']
#     print item ['street_address']


