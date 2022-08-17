import requests


def get_data(url):
    """Get data from API
    url: url address of API service
    """
    response = requests.get(url)  # get the address using requests
    json_data = response.json()
    # json_data = json.loads(response.text)  # alternative option, requires to import json

    return json_data
