__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import requests
from geopy.geocoders import Nominatim



api_key = "074b2fc170173ee60f72"  #
g_api_key = 'AIzaSyA-sYtg9oJPJS2D99mQiqesFQ2ybkIS8io'
# g_api_key = 'AIzaSyCxV95FhWcBkzGs9X21mZJSMTDw-D1nTMg'


def geo(ulica, nr_domu):
    adres = '{0},{1}, Wrocław, Polska'.format(nr_domu, ulica)
    adres_osm = 'Polska, Wrocław,{1} {0}'.format(nr_domu, ulica)
    print(adres_osm)
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

    geolocator = Nominatim()
    location = geolocator.geocode(adres_osm)
    if location:
        print(location.raw)
        osm = 'https://www.openstreetmap.org/{0}/{1}' .format(location.raw['osm_type'], location.raw['osm_id'])
    else:
        osm = ''

    street_view = 'http://maps.google.com/maps?q=&layer=c&cbll={0},{1}' .format(output["latitude"], output["longitude"])
    # osm = 'https://www.openstreetmap.org/#map=19/{0}/{1}' .format(location.raw['osm_type'],location.raw['osm_id'])
    return street_view, osm
