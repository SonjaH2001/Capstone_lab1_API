#fetch data from a web server using open API. Specific dta to fetch.
#pip install --user requests  (to install locally, without admin)

import os #clicked on os when it was red, it imports for you!!

import requests #ignore red squiggle
from urllib.parse import quote #handles the q= in the API string/ sanitize the odd characters in the URL%<&
import json
key = os.environ.get("key") # I put the value into the evironment variable and named it key
# key = "bananas"
def get_temp(city, country):
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s' \
                 % (quote(city), quote(country), key))
    if resp.status_code == 200:
        parsed_json = resp.json() # gets the json from the resp. parses json from response body aka content
        tempInKelvin = parsed_json['main']['temp']  #json in python is a dictionary, main is a dictionary of stuff.
        return tempInKelvin
    if resp.status_code == 401:
        print("Access denied, invalid API key")
        #add more of these!!!
    else:
        return None

    #googlin' = python requests DNS fail. exception handling.

def main():

    city = input("Enter the city to search for: ")
    country = input("What country is that in? ")
    is_valid(city, country) #data validation function
    temp = get_temp(city, country)
    if temp is not None:
        print('The temperature in %s %s is %f degrees K ' % (city, country, temp))
        clesius = convert_temp(temp)
        # print('The temperature in %s %s is %f degrees celsius' % (city, country, temp))
        print("Celsius is ", clesius )
        #addd farenheit
    else :
        print('Unable to get the temperature.')

#need to do error handling, cache locally, etc
# You should handle errors, such as access denied, no network connection, invalid response....
def is_valid(city, country):
    if city == "":
        print("enter the city or country dammit ")

def convert_temp(temp): #T(°C) = T(K) - 273.15
    celsius_temp = temp - 273.15
    return celsius_temp

main()
