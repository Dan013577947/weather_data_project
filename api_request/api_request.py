import requests

api_key = '907aab6a73badcfaf30152155cadc0ac'
api_url = f'http://api.weatherstack.com/current?access_key={api_key}&query=New York'


def fetch_data():
    print("Fetching data from API on process..")
    try:    
        response = requests.get(api_url)
        response.raise_for_status()
        print("Fetching data successful")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")
        raise 

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'},
     'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006',
      'timezone_id': 'America/New_York', 'localtime': '2025-09-18 18:51', 'localtime_epoch': 1758221460, 'utc_offset': '-4.0'}, 'current': {'observation_time': '10:51 PM',
       'temperature': 28, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'],
        'astro': {'sunrise': '06:40 AM', 'sunset': '06:59 PM', 'moonrise': '03:07 AM', 'moonset': '05:43 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 15},
         'air_quality': {'co': '516.15', 'no2': '141.525', 'o3': '7', 'so2': '15.725', 'pm2_5': '32.93', 'pm10': '33.115', 'us-epa-index': '2', 'gb-defra-index': '2'},
          'wind_speed': 6, 'wind_degree': 211, 'wind_dir': 'SSW', 'pressure': 1013, 'precip': 0, 'humidity': 37, 'cloudcover': 0, 'feelslike': 29, 'uv_index': 0, 'visibility': 16,
           'is_day': 'yes'}}
