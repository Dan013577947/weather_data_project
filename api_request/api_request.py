import requests
#cdb5ee8f81475d08dc1bc557bb838f55 -> reserve key if the 100 limit reached
#907aab6a73badcfaf30152155cadc0ac
api_key = 'cdb5ee8f81475d08dc1bc557bb838f55'
api_url = f'http://api.weatherstack.com/current?access_key={api_key}'
querystring = {"query":"14.662939, 121.015456"}

def fetch_data():
    print("Fetching data from API on process..")
    try:    
        response = requests.get(api_url,params=querystring)
        response.raise_for_status()
        print("Fetching data successful")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")
        raise 

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'},
     'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006',
      'timezone_id': 'America/New_York', 'localtime': '2025-09-22 10:52:00', 'localtime_epoch': 1758221460, 'utc_offset': '8.0'}, 'current': {'observation_time': '10:51 PM',
       'temperature': 50, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Too Hot'],
        'astro': {'sunrise': '06:40 AM', 'sunset': '06:59 PM', 'moonrise': '03:07 AM', 'moonset': '05:43 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 15},
         'air_quality': {'co': '516.15', 'no2': '141.525', 'o3': '7', 'so2': '15.725', 'pm2_5': '32.93', 'pm10': '33.115', 'us-epa-index': '2', 'gb-defra-index': '2'},
          'wind_speed': 25, 'wind_degree': 211, 'wind_dir': 'SSW', 'pressure': 1013, 'precip': 0, 'humidity': 37, 'cloudcover': 0, 'feelslike': 29, 'uv_index': 0, 'visibility': 16,
           'is_day': 'yes'}}
