from weather import get_weather
from glyphs import *
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(
    prog="ascii-weather",
    description="Gets the local weather."
)

parser.add_argument("-d", "--debug", action="store_true", help="Output debug information.")

args = parser.parse_args()

PADDING = " " * 2
NEWLINE = '\n'
DEBUG_MSGS = []

def is_nighttime():
	hour = datetime.now().hour
	# naive approach - day-time defined as 6:00 AM -> 8:00 PM
	nighttime = not (6 <= hour <= 19)
	return nighttime

def select_glyph(condition_id, wind_speed):
    category, subcategory = condition_id // 100, condition_id % 100
    nighttime = is_nighttime()

    match category, subcategory, nighttime:
        case 8, 0, True: glyph = night.fullcolor()
        case 8,(1|2|3),True: glyph = partial_clouds_night.fullcolor()
        case 2,_,_: glyph = thunderstorm.fullcolor()
        case 5,_,_: glyph = rain.fullcolor()
        case 8,(1|2|3),_: glyph = partial_clouds.fullcolor()
        case 8,4,_: glyph = clouds.fullcolor()
        case _,_,_: glyph = "?"
    
    DEBUG_MSGS.append(f'DEBUG: category: {category}, subcategory: {subcategory}, nighttime: {nighttime}')

    return glyph

def main():

    weather = get_weather()
    glyph = select_glyph(weather.condition_id, 10)
    time = datetime.today().strftime("%I:%M %p")

    weather_text = [
		'{:<13} feels like {}'.format(weather.temp, weather.feels_like),
		'{:<13} wind {}'.format(weather.condition, weather.wind_speed),
        '{:<13} thanks to https://openweathermap.org'.format(time)
	]
    
    print(f'The current conditions at {time} in {weather.city} are:')

    for row in zip(glyph, weather_text):
        combined = PADDING.join(row)
        print(combined)
    
    DEBUG_MSGS.append("DEBUG: ")
    DEBUG_MSGS.append(weather)
    # print(NEWLINE.join(glyph))

    if args.debug:
        for msg in DEBUG_MSGS:
            print(msg)
main()
