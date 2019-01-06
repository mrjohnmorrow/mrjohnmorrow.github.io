import os
import json
from botocore.vendored import requests

def lambda_handler(event, context):

    # you should probably reduce this in your code, but this was just broken down for readability
    full_url = "https://api.trello.com/1/lists/" + os.environ.get('list_id') + "/cards?fields=id,name"
    full_url = full_url + "&key=" + os.environ.get('trello_key')
    full_url = full_url + "&token=" + os.environ.get('trello_token')
    response = requests.get(full_url)

    cards = response.json()
    names = []
    for card in cards:
        names.append(card["name"])
    output= {}
    output["value1"] = "<html><body><br><ul><li>" + "</li><li>".join(names) + "</li></ul></body></html>"

    # send to the printer's ifttt hook
    printer_result = requests.post("https://maker.ifttt.com/trigger/todo_ready/with/key/" + os.environ.get('maker_key'), data = output)

    # So, you obviously should be doing some error handling here, but for a small
    # personal project like this, I'd rather cross that bridge when I get to it
    return {
        'statusCode': 200,
        'body': str(printer_result),
    }
