import weather

weatherAPI = weather.API("d16186fae1c84a3a9af24827241106")

RM_KEYS = set([
    'dewpoint_c',
    'heatindex_c',
    'is_day',
    'pressure_mb',
    'snow_cm',
    'tz_id',
    'uv',
    'windchill_c',
    'wind_degree'
])

RM_SUFFIXES = (
    '_epoch',
    'it_rain',
    'it_snow',
    'precip_mm'
)

IMPERIAL_SUFFIXES = (
    '_f',
    '_mph',
    '_in',
    '_miles'
)

def get_weather_today(location, imperial=False):
    if not imperial:
        global RM_SUFFIXES
        RM_SUFFIXES += IMPERIAL_SUFFIXES

    forecast = weatherAPI.forecast(location, days=1)
    day_and_hourly = forecast['forecast']['forecastday'][0]
    del day_and_hourly['astro']

    forecast['forecast'] = day_and_hourly

    for w_dict in [
        forecast['current'],
        forecast['location'],
        forecast['forecast'],
        forecast['forecast']['day'],
        *forecast['forecast']['hour']
    ]:
        for key in list(w_dict.keys()):
            if key.endswith(RM_SUFFIXES) or key in RM_KEYS:
                del w_dict[key]
            elif key == 'condition':
                w_dict[key] = w_dict[key]['text']

    return {
        f"Today's weather forecast at {location}": forecast,
    }
