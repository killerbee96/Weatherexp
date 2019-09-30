import click

import requests

import json

import datetime





api_key = '64315ebd079846c4b15ebd079806c408'

base_url = 'https://api.weather.com/v3/'

search_n_point_url = base_url + 'location/search?query={}&language=en-IN&format=json&apiKey={}'

five_day_forecast = base_url + 'wx/forecast/daily/5day?placeid={}&units=e&language=en-IN&format=json&apiKey={}'

forecast_by_date = 'https://api.weather.com/v2/pws/history/all?stationId=IBANGA20&format=json&units=m&date={}&apiKey={}'

forecast_types = {'today': 0, '5days': 1}

default_forecast_type = 'today'



search_location_data = ['city', 'displayName', 'country',

                        'placeId', 'longitude', 'latitude', 'address']



clickhelp = {

    'name': 'Name of the city',

    'date': 'Date of the weather at given location. Default is today\'s day',

    'ftype': 'Type of forecast (today, 5days). default is \'today\''

}





def get_response(url):

    response = requests.get(url)

    return response.json()





def get_location(place):

    """Gets first result of the location data retrived based on query"""

    location_data = get_response(

        (search_n_point_url).format(place, api_key))

    print(location_data)

    return_data = {}

    if 'errors' not in location_data:

        print('location data found')

        for key in search_location_data:

            return_data[key] = location_data['location'][key][0]

    else:

        print('no location data found')

    return return_data





@click.command()

@click.option('--place', prompt='Please enter a city name',

              help=clickhelp['name'])

@click.option('--date', default=1,

              help=clickhelp['date'])

@click.option('--forecast_type', default=default_forecast_type,

              help=clickhelp['ftype'])

def get_weather(place, date, forecast_type):

    """Gets weather based on location name, date and type of forecast"""

    location_data = get_location(place)

    if bool(location_data):

        weather_data = get_response(

           (five_day_forecast).format(location_data['placeId'], api_key)

        )

        if forecast_types[forecast_type] == forecast_types['today']:

            print(weather_data['daypart'][0])

            print('today')

        elif forecast_types[forecast_type] == forecast_types['5days']:

            print(weather_data)

            print('5days')

        print('weather data found')

    else:

        print('no weather data found')

    tday = datetime.date.today()

    tdelta = datetime.timedelta(days=-1)

    print(tday,tday+tdelta)



if __name__ == '__main__':

    get_weather()