import requests
import json
import sys
import argparse
from lyrics_api import *

def test():
    return "Fuck O'Leary"

def main(artist,track):
    # Parse arguments
    artist_name = str(artist)
    track_name  = str(track)

    # Make API call. Get Data
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    #print("API Call: " + api_call)
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    #print()
    #print(data['lyrics']['lyrics_body'])

    return data['lyrics']['lyrics_body']


#if __name__ == '__main__':
#    main()