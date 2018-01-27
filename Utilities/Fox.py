import requests
import json
import Constants  #Add IMG_FOX_URL = 'https://randomfox.ca/floof/' to constants.py.

#Being a json parse and not a hardcoded url I put it into Utilities.
async def get_fox(client):
    print("fetching fox from https://randomfox.ca/floof/")
    r = requests.get(Constants.IMG_FOX_URL)
    try:
        fox_json = r.json()
        return fox_json['image']
    except Exception as e:
        print("Error fetching result: " + e)

