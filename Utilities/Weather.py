import discord
from pprint import pprint
import requests
import json
import datetime

import Constants

async def get_weather(message, client):
    #.weather christchurch
    query = message.content[8:].strip(' ')
    print('Providing weather for: ' + query)
    r = requests.get(Constants.BASE_WEATHER_URL + query + Constants.WEATHER_API_KEY)
    weather_data = r.json()

    try:
        msg = '```Current weather for ' + weather_data['name'] + ', ' + weather_data['sys']['country'] + '\n\n'
    except KeyError:
        msg = 'No results. Try modifying your search query!'
        # await client.send_message(message.channel, msg)
        return msg

    try:
        msg += 'Description: ' + weather_data['weather'][0]['main'] + '; ' + weather_data['weather'][0]['description'] + '\n'
    except KeyError:
        msg += 'Description: Unavailable\n'

    try:
        temp_f = convert_to_fahrenheit(float(weather_data['main']['temp']))
        temp_c = convert_to_celsius(float(weather_data['main']['temp_max']))
        msg += 'Temperature: ' + '%.2f' % temp_c + ' C / ' + '%.2f' % temp_f + ' F\n'
    except KeyError:
        msg += 'Temperature: Unavailable\n'

    try:
        msg += 'Cloudiness: ' + str(weather_data['clouds']['all']) + '%\n'
    except KeyError:
        msg += 'Cloudiness: Unavailable\n'

    try:
        msg += 'Humidity: ' + str(weather_data['main']['humidity']) + '%\n'
    except KeyError:
        msg += 'Humidity: Unavailable\n'

    try:
        wind_direction = calc_wind_direction(weather_data['wind']['deg'])
        msg += 'Wind Direction: ' + wind_direction + '\n'
    except KeyError:
        msg += 'Wind Direction: Unavailable\n'

    try:
        msg += 'Wind Speed: ' + str(weather_data['wind']['speed']) + ' m/s\n'
    except KeyError:
        msg += 'Wind Speed: Unavailable\n'

    try:
        'Air Pressure: ' + str(weather_data['main']['pressure']) + ' hPa\n'
    except KeyError:
        msg += 'Air Pressure: Unavailable\n'

    '''try:
        sunrise = datetime.datetime.fromtimestamp(int(weather_data['sys']['sunrise'])).strftime('%H:%M:%S')
        sunset = datetime.datetime.fromtimestamp(int(weather_data['sys']['sunset'])).strftime('%H:%M:%S')
        msg += 'Sunrise: ' + sunrise + ' / Sunset: ' + sunset + '```'
    except:
        msg += 'Sunrise/Sunset: Unavailable\n'''

    msg += '```'
    return msg


def convert_to_celsius(temp_kelvin):
    return temp_kelvin - Constants.KELVIN_CONSTANT

def convert_to_fahrenheit(temp_kelvin):
    return 1.8 * (temp_kelvin - Constants.KELVIN_CONSTANT) + 32

def calc_wind_direction(deg):
    if deg <= 22.5 or deg > 337.5:
        return 'North'
    elif deg > 22.5 and deg <= 67.5:
        return 'North-East'
    elif deg > 67.5 and deg <= 112.5:
        return 'East'
    elif deg > 112.5 and deg <= 157.5:
        return 'South-East'
    elif deg > 157.5 and deg <= 202.5:
        return 'South'
    elif deg > 202.5 and deg <= 247.5:
        return 'South-West'
    elif deg > 247.5 and deg <= 292.5:
        return 'West'
    elif deg > 292.5 and deg <= 337.5:
        return 'North-West'


#############################################
'''{u'base': u'cmc stations',
 u'clouds': {u'all': 68},
 u'cod': 200,
 u'coord': {u'lat': 51.50853, u'lon': -0.12574},
 u'dt': 1383907026,
 u'id': 2643743,
 u'main': {u'grnd_level': 1007.77,
           u'humidity': 97,
           u'pressure': 1007.77,
           u'sea_level': 1017.97,
           u'temp': 282.241,
           u'temp_max': 282.241,
           u'temp_min': 282.241},
 u'name': u'London',
 u'sys': {u'country': u'GB', u'sunrise': 1383894458, u'sunset': 1383927657},
 u'weather': [{u'description': u'broken clouds',
               u'icon': u'04d',
               u'id': 803,
               u'main': u'Clouds'}],
 u'wind': {u'deg': 158.5, u'speed': 2.36}}'''
