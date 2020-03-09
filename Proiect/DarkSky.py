#Prima metoda cu requests
import requests
import json
import pandas as pd
from datetime import datetime


def darkskyPD(gps_coords,date,api_key):
   json_darksky = requests.get("https://api.darksky.net/forecast/{}/{},{},{}?exclude=currently".format(api_key,gps_coords[0],gps_coords[1],date)).json()
   json_info = json.dumps(json_darksky['daily']['data'])
   df = pd.read_json(json_info)
   df['time']=pd.to_datetime(df['time'],unit='s')
   df['time'] = pd.to_datetime(df['time'])
   df = df.set_index('time')
   return df

def merge_pd(first_pd, second_pd):
   new_df = pd.concat([first_pd, second_pd], axis = 1, join = 'inner')
   new_df.set_index('datetime')
   return new_df


#correlation between moon phase and tides
def moon_phase(moon_phase):
   if moon_phase < .06 : return "new_moon"#0 degree
   if moon_phase < .125 : return "waxin_crescent_moon"
   if moon_phase < .25 : return "first_quarter_moon"#90 degree
   if moon_phase < .48 : return "waxing_gibbous_moon"
   if moon_phase < .52 : return "full_moon"#180 degree
   if moon_phase < .625 : return "waning_gibbous_moon"
   if moon_phase < .75 : return "last_quarter_moon"#90 degree
   if moon_phase < 1 : return "waning_crescent_moon"
   return "crescent_moon"


#correlation between wind direction and cloud cover
def wind_dir(wind_bearing):
   if wind_bearing < 20 : return "north"
   if wind_bearing < 70 : return "north_east"
   if wind_bearing < 110 : return "east"
   if wind_bearing < 160 : return "south_east"
   if wind_bearing < 200 : return "south"
   if wind_bearing < 250 : return "south_west"
   if wind_bearing < 290 : return "west"
   if wind_bearing < 340 : return "north_west"
   return "north"



city = "Iasi"
gps_coords = [47.1585,27.6014]
darksky_api_key = "668ad2afff869e6599b447fbe3391d21"
date = datetime(2018, 10, 23, 10).isoformat()
darksky = darkskyPD(gps_coords, date, darksky_api_key)
windCSV = pd.read_csv(r"C:\Users\Iacob\Desktop\ProiectStrongBytes\WindCSV.csv")
windCSV.set_index('datetime')
merge_pd = merge_pd(windCSV, darksky)
print(darksky.head(10))

#####################################################################
#https://github.com/Detrous/darksky
##pip3 install darksky_weahter
#from darksky.api import DarkSky, DarkSkyAsync
#from darksky.types import languages, units, weather
#from datetime import datetime as dt
#
#API_KEY = "668ad2afff869e6599b447fbe3391d21"
#
#darksky = DarkSky(API_KEY)
#t = dt(2018,4,24,4)
#
#gps_coords = [47.1585,27.6014]
#forecast = darksky.get_time_machine_forecast(
#        gps_coords[0],gps_coords[1],
#        extend = False,
#        lang = languages.ENGLISH,
#        values_units = units.AUTO,
#        exclude = [weather.MINUTELY, weather.ALERTS],
#        timezone = 'UTC',
#        time = t
#        )
#
#
#print(forecast.daily)
###################################################################
##https://github.com/lukaskubis/darkskylib
#from darksky import forecast
#from datetime import datetime as dt
#
#gps_coords = [47.1585,27.6014]
#API_KEY = "668ad2afff869e6599b447fbe3391d21"
#IASI = forecast.Forecast(API_KEY, gps_coords[0], gps_coords[1])
#t = dt(2018,4,3,12).isoformat()
#
#print(IASI.daily)

