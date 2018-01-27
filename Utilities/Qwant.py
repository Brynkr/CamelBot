import discord
import requests
import json
import Constants #Add QWANT_SEARCH_URL = 'https://api.qwant.com/api/search/web?locale=en_US&count=1&q=' to constants.py

#qwant does not allow requests without a user agent. I just pasted in a valid random one for the time being.
async def qwantSearch(message, client):
    query = message.content[7:].replace(' ', '+')
    print ("Searching for \"" + query + "\" on Qwant...")
    r = requests.get(Constants.QWANT_SEARCH_URL + query, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
    try:
        parsedR = r.json()
    except Exception as e:
        print("Error in the JSON serialization/HTTP request; " + e)


    returnMessage = ""

    if parsedR["status"] != "success":
        returnMessage = "Error fetching the Qwant search result."
    else:
        searchResult = parsedR["data"]["result"]["items"][0]
        returnMessage = searchResult["url"]
    return returnMessage