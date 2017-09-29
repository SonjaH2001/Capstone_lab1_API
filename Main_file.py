#fetch data from a web server using open API. Specific dta to fetch.
#pip install --user requests  (to install locally, without admin)

import os #clicked on os when it was red, it imports for you!!

import requests #ignore red squiggle
from urllib.parse import quote #handles the q= in the API string
import json
key = os.environ.get("key") # I put the value into the evironment variable and named it key

def get_temp(city, country):
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s' \
                 % (quote(city), quote(country), key))
    parsed_json = resp.json()
    tempInKelvin = parsed_json['main']['temp']
    return tempInKelvin

def main():

    city = input("Enter the city to search for")
    country = input("What country is that in?")
    temp = get_temp(city, country)
    if temp is not None:
        print('The temperature in %s %s is %f degrees C ' % (city, country, temp))
    else :
        print('Unable to get the temperature.')

#need to do error handling, cache locally, etc

main()