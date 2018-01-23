__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import requests

api_key = "074b2fc170173ee60f72"  #
g_api_key = 'AIzaSyA-sYtg9oJPJS2D99mQiqesFQ2ybkIS8io'
# g_api_key = 'AIzaSyCxV95FhWcBkzGs9X21mZJSMTDw-D1nTMg'


def geo(ulica, nr_domu):
    adres = '{0},{1}, Wrocław, Polska'.format(nr_domu, ulica)
    loc_path = 'https://maps.googleapis.com/maps/api/geocode/json?address={1}&key={0}' .format(g_api_key, adres)
    results = requests.get(loc_path).json()

    if len(results['results']) == 0:
        output = {
            "latitude": None,
            "longitude": None
        }
    else:
        answer = results['results'][0]
        output = {
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng')
        }
    street_view = 'http://maps.google.com/maps?q=&layer=c&cbll={0},{1}' .format(output["latitude"], output["longitude"])
    return street_view
