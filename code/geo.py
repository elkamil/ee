__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import requests
# import time
# import pandas
# import json
# import re

# try:
#    from urlparse import urlparse
# except ImportError:
#    from urllib.parse import urlparse

api_key = "074b2fc170173ee60f72"  #
g_api_key = 'AIzaSyA-sYtg9oJPJS2D99mQiqesFQ2ybkIS8io'
# g_api_key = 'AIzaSyCxV95FhWcBkzGs9X21mZJSMTDw-D1nTMg'


def geo(ulica, nr_domu):
    # adresy = ['30/32, Podróżnicza, Wrocław']
    # nr_d = str(nr_domu)
    # ul = re.sub(r'(ul\.|AL\.)s?','',ulica)
    # adres =  nr_domu[0] + ', ' + ulica[1] + ', Wrocław, Polska'
    # adres =  nr_domu[0] + ', ' + ulica[0] + ', Wrocław, Polska'
    adres = '{0},{1}, Wrocław, Polska'.format(nr_domu, ulica)
    # print(adres)

    # loc_path = 'http://locationiq.org/v1/search.php?key={0}&format=json&q={1}' .format(api_key, adres)
    loc_path = 'https://maps.googleapis.com/maps/api/geocode/json?address={1}&key={0}' .format(g_api_key, adres)
    adres_geo = {}
    adres_geo['adres'] = adres
    # loc_url = urlparse(loc_path)
    # time.sleep(0.1)
    # data = requests.get(loc_url.geturl()).text
    results = requests.get(loc_path)
    results = results.json()

    if len(results['results']) == 0:
        output = {
            "formatted_address": None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:
        answer = results['results'][0]
        output = {
            "formatted_address": answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components')
                                  if 'postal_code' in x.get('types')])
        }
    street_view = 'http://maps.google.com/maps?q=&layer=c&cbll={0},{1}' .format(output["latitude"], output["longitude"])
    return street_view
